import curses
import math
import time
import sys

# --- 3D Sphere Data ---
SPHERE_RADIUS = 1.5
LATITUDE_LINES = 10
LONGITUDE_POINTS_PER_LINE = 20

VERTICES = []
EDGES = []

# --- Generate Vertices ---
# Iterate from 0 to pi (latitude)
for i in range(LATITUDE_LINES + 1):
    phi = math.pi * i / LATITUDE_LINES
    # Iterate from 0 to 2*pi (longitude)
    for j in range(LONGITUDE_POINTS_PER_LINE):
        theta = 2 * math.pi * j / LONGITUDE_POINTS_PER_LINE
        
        # Spherical to Cartesian coordinates
        x = SPHERE_RADIUS * math.sin(phi) * math.cos(theta)
        y = SPHERE_RADIUS * math.cos(phi) # Use cos(phi) for Y to make it "upright"
        z = SPHERE_RADIUS * math.sin(phi) * math.sin(theta)
        
        VERTICES.append([x, y, z])

# --- Generate Edges ---
# Latitude edges (rings)
for i in range(LATITUDE_LINES + 1):
    for j in range(LONGITUDE_POINTS_PER_LINE):
        p1_idx = i * LONGITUDE_POINTS_PER_LINE + j
        p2_idx = i * LONGITUDE_POINTS_PER_LINE + (j + 1) % LONGITUDE_POINTS_PER_LINE
        EDGES.append((p1_idx, p2_idx))

# Longitude edges (spokes)
for j in range(LONGITUDE_POINTS_PER_LINE):
    for i in range(LATITUDE_LINES): # Stop one line early to avoid wrapping
        p1_idx = i * LONGITUDE_POINTS_PER_LINE + j
        p2_idx = (i + 1) * LONGITUDE_POINTS_PER_LINE + j
        EDGES.append((p1_idx, p2_idx))


def draw_line(stdscr, y1, x1, y2, x2, char='.'):
    """
    Draws an ASCII line from (y1, x1) to (y2, x2)
    using Bresenham's line algorithm.
    """
    # Ensure coordinates are integers
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    dx = abs(x2 - x1)
    dy = -abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx + dy
    
    h, w = stdscr.getmaxyx()

    while True:
        # Draw the character if it's within screen bounds
        if 0 <= y1 < h and 0 <= x1 < w:
            try:
                stdscr.addch(y1, x1, char)
            except curses.error:
                pass # Ignore errors at screen edge
                
        if x1 == x2 and y1 == y2:
            break
            
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x1 += sx
        if e2 <= dx:
            err += dx
            y1 += sy

def run_sphere(stdscr):
    """Main animation function"""
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(15) # ~60 FPS
    
    angle_x = angle_y = 0

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break
            
        h, w = stdscr.getmaxyx()
        stdscr.clear()
        
        # --- Update Angles ---
        angle_x += 0.01
        angle_y += 0.02
        
        # --- Precompute Sin/Cos ---
        sin_x, cos_x = math.sin(angle_x), math.cos(angle_x)
        sin_y, cos_y = math.sin(angle_y), math.cos(angle_y)
        
        projected_points = []
        
        # --- 3D Rotation and 2D Projection ---
        for vertex in VERTICES:
            x, y, z = vertex
            
            # Rotate around Y-axis
            rot_y_x = x * cos_y - z * sin_y
            rot_y_z = x * sin_y + z * cos_y
            
            # Rotate around X-axis
            rot_x_y = y * cos_x - rot_y_z * sin_x
            rot_x_z = y * sin_x + rot_y_z * cos_x
            
            # Orthographic projection (ignore z for perspective)
            projected_x = rot_y_x
            projected_y = rot_x_y
            
            # --- Scale and Center ---
            # Scale the sphere. 0.5 factor on Y to account for non-square
            # terminal characters (they are taller than they are wide).
            scale = 15
            char_aspect_ratio = 0.5
            screen_x = int(projected_x * scale + w // 2)
            screen_y = int(projected_y * scale * char_aspect_ratio + h // 2)
            
            projected_points.append((screen_y, screen_x))

        # --- Draw Edges ---
        for edge in EDGES:
            p1 = projected_points[edge[0]]
            p2 = projected_points[edge[1]]
            draw_line(stdscr, p1[0], p1[1], p2[0], p2[1])

        stdscr.addstr(0, 0, "Rotating 3D Sphere - Press 'q' to quit")
        stdscr.refresh()

def main():
    """Wrapper function to safely start and stop curses."""
    
    # The 'curses' module is imported globally at the top.
    # We only need to provide a helpful message if we are on
    # Windows and the import failed.
    
    try:
        curses.wrapper(run_sphere)
    except KeyboardInterrupt:
        print("Sphere animation stopped.")
    except (ImportError, NameError) as e:
        # Catch if 'curses' failed to import at the top
        if sys.platform == "win32":
            print("="*50)
            print("ERROR: The 'curses' library failed to import.")
            print("On Windows, this script requires 'windows-curses'.")
            print("Please run: pip install windows-curses")
            print("="*50)
        else:
            print(f"An error occurred: {e}")
            print("The 'curses' library is typically built-in on macOS and Linux.")

if __name__ == "__main__":
    main()
