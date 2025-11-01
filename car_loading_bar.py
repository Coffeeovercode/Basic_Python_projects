import time
import sys

def simulate_driving(duration=20, bar_length=40):
    """
    Simulates a loading process by driving a car
    across the terminal.
    """
    print(f"\nSimulating a task for {duration} seconds...")
    
    car_emoji = "🚗"
    track_char = "─"
    
    # Iterate from 0 to 100 (inclusive)
    steps = 100 
    for i in range(steps + 1):
        # Calculate percentage
        percent = i
        
        # Calculate the car's position on the track
        # We use (bar_length - 1) so the car stops *at* the last position
        car_pos = int((bar_length - 1) * i // steps)
        
        # Create the track string
        track_before = track_char * car_pos
        track_after = track_char * (bar_length - car_pos - 1)
        
        # Combine the track and the car
        bar = f"{track_before}{car_emoji}{track_after}"
        
        # Create the output string
        # \r moves the cursor to the start of the line
        # end="" prevents it from adding a new line
        output_string = f'\rProgress: |{bar}| {percent}% Complete'
        
        sys.stdout.write(output_string)
        sys.stdout.flush()
        
        # Simulate work by sleeping
        time.sleep(duration / steps)
        
    print("\n\n✅ Task complete! Arrived at destination.")

# --- Main execution block ---
if __name__ == "__main__":
    try:
        simulate_driving()
    except KeyboardInterrupt:
        print("\n\nDriving cancelled by user.")
