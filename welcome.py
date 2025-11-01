import time
import sys

def scroll_message(message="Welcome! Press Ctrl+C to exit.", width=40):
    """
    Scrolls a message across the terminal screen.
    """
    
    # Pad the message with spaces for a smooth wrap-around effect
    padding = " " * width
    message_padded = padding + message + padding
    
    # Run the scroll indefinitely
    try:
        while True:
            # Iterate through the padded message to create the sliding window
            for i in range(len(message_padded) - width + 1):
                # Get the "window" of text to display
                display_text = message_padded[i : i + width]
                
                # Use \r to return to the start of the line
                sys.stdout.write(f"\r{display_text}")
                sys.stdout.flush()
                
                # Control the speed
                time.sleep(0.15)
                
    except KeyboardInterrupt:
        print("\n\nScrolling stopped. Goodbye!")

# --- Main execution block ---
if __name__ == "__main__":
    scroll_message()
