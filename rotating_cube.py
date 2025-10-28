import curses
import math
import time
import sys

# --- 3D Cube Data ---
# Define the 8 vertices (corners) of the cube
VERTICES = [
    [-1, -1, -1], [ 1, -1, -1], [-1,  1, -1], [ 1,  1, -1],
    [-1, -1,  1], [ 1, -1,  1], [-1,  1,  1], [ 1,  1,  1]
]

# Define the 12 edges (lines) by connecting vertex indices
EDGES = [
    (0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3),
    (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)
]

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

def run_cube(stdscr):
    """Main animation function"""
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(15) # ~60 FPS
    
    angle_x = angle_y = angle_z = 0

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
            # Scale the cube. 0.5 factor on Y to account for non-square
            # terminal characters (they are taller than they are wide).
            scale = 20
            char_aspect_ratio = 0.5
            screen_x = int(projected_x * scale + w // 2)
            screen_y = int(projected_y * scale * char_aspect_ratio + h // 2)
            
            projected_points.append((screen_y, screen_x))

        # --- Draw Edges ---
        for edge in EDGES:
            p1 = projected_points[edge[0]]
            p2 = projected_points[edge[1]]
            draw_line(stdscr, p1[0], p1[1], p2[0], p2[1])

        stdscr.addstr(0, 0, "Rotating 3D Cube - Press 'q' to quit")
        stdscr.refresh()

def main():
    """Wrapper function to safely start and stop curses."""
    
    # The 'curses' module is imported globally at the top.
    # We only need to provide a helpful message if we are on
    # Windows and the import failed.
    
    try:
        curses.wrapper(run_cube)
    except KeyboardInterrupt:
        print("Cube animation stopped.")
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

