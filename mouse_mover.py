import pyautogui
import time
import random

def move_mouse():
    """
    Moves the mouse cursor slightly every few seconds to simulate activity.
    """
    print("🖱️  Auto Mouse Mover is running...")
    print("Press Ctrl+C in the terminal to stop the script.")

    # Get the screen size
    screen_width, screen_height = pyautogui.size()
    
    try:
        while True:
            # --- Move mouse slightly to a random new position ---
            # Define a small box around the current mouse position
            current_x, current_y = pyautogui.position()
            move_range = 20
            new_x = current_x + random.randint(-move_range, move_range)
            new_y = current_y + random.randint(-move_range, move_range)

            # Make sure the new position is still on the screen
            new_x = max(0, min(screen_width - 1, new_x))
            new_y = max(0, min(screen_height - 1, new_y))

            # Move the mouse with a slight duration to make it look more natural
            pyautogui.moveTo(new_x, new_y, duration=0.25)
            
            # --- Wait for a random interval ---
            sleep_duration = random.randint(10, 20)
            time.sleep(sleep_duration)

    except KeyboardInterrupt:
        print("\n✅ Script stopped by user. Your mouse is free!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    move_mouse()
