import time

def run_stopwatch():
    """
    Runs an interactive stopwatch in the terminal.
    """
    print("  Simple Stopwatch")
    print("Press ENTER to Start/Lap.")
    print("Press Ctrl+C to Stop.")
    
    lap_num = 1
    
    try:
        # Wait for the user to start
        input("Press ENTER to begin...")
        start_time = time.time()
        last_lap_time = start_time
        print("Stopwatch started!")

        while True:
            # Wait for user to press Enter for a lap
            input() 
            
            lap_time = time.time()
            total_elapsed = lap_time - start_time
            lap_elapsed = lap_time - last_lap_time
            
            print(f"Lap {lap_num}: {lap_elapsed:7.2f}s  (Total: {total_elapsed:7.2f}s)")
            
            last_lap_time = lap_time
            lap_num += 1

    except KeyboardInterrupt:
        # Handle the stop (Ctrl+C)
        end_time = time.time()
        total_elapsed = end_time - start_time
        
        print("\n\n" + "="*30)
        print("    Stopwatch Stopped.")
        print(f"    Total Elapsed Time: {total_elapsed:.2f}s")
        print("="*30)

# --- Main execution block ---
if __name__ == "__main__":
    run_stopwatch()
