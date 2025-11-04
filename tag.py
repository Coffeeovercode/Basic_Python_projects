import random
import math

def get_difficulty():
    """Asks the user for a difficulty level and returns grid size and turns."""
    print("Select a difficulty:")
    print("  1. Easy   (10x10 grid, 20 turns)")
    print("  2. Medium (15x15 grid, 25 turns)")
    print("  3. Hard   (20x20 grid, 30 turns)")
    
    while True:
        choice = input("Enter choice (1-3): ")
        if choice == '1':
            return 10, 20
        elif choice == '2':
            return 15, 25
        elif choice == '3':
            return 20, 30
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def calculate_distance(pos1, pos2):
    """Calculates the Euclidean distance between two [x, y] points."""
    dx = pos1[0] - pos2[0]
    dy = pos1[1] - pos2[1]
    return math.sqrt(dx*dx + dy*dy)

def play_game():
    """Main function to run the Hot/Cold Tag Game."""
    
    grid_size, max_turns = get_difficulty()
    turns_left = max_turns
    
    # Player starts at [0, 0]
    player_pos = [0, 0]
    
    # Target is placed randomly, but not at [0, 0]
    target_pos = [random.randint(1, grid_size), random.randint(1, grid_size)]
    
    # Initial distance
    last_distance = calculate_distance(player_pos, target_pos)
    
    print("\n--- Game Started! ---")
    print(f"You are at {player_pos}. Find the target hidden in the {grid_size}x{grid_size} grid.")
    print("Move with 'w' (up), 'a' (left), 's' (down), 'd' (right).")
    
    while turns_left > 0:
        print("\n" + "="*30)
        print(f"Turns left: {turns_left} | Your position: {player_pos}")
        
        # --- Get Player Move ---
        move = input("Your move (w/a/s/d): ").lower()
        
        # Store old position in case of invalid move
        old_pos = list(player_pos)
        
        if move == 'w':
            player_pos[1] += 1
        elif move == 's':
            player_pos[1] -= 1
        elif move == 'a':
            player_pos[0] -= 1
        elif move == 'd':
            player_pos[0] += 1
        else:
            print("Invalid move. Use w, a, s, or d.")
            continue
            
        # --- Boundary Check ---
        if not (0 <= player_pos[0] <= grid_size and 0 <= player_pos[1] <= grid_size):
            print("Whoops! You hit the edge of the grid. Move back.")
            player_pos = old_pos
            continue

        # --- Check for Win ---
        if player_pos == target_pos:
            print(f"\n🎉 You found it at {player_pos}! You win! 🎉")
            print(f"It took you {max_turns - turns_left + 1} turns.")
            break
            
        # --- Give Hot/Cold Feedback ---
        current_distance = calculate_distance(player_pos, target_pos)
        
        if current_distance < last_distance:
            print("🔥 HOTTER! You're closer.")
        elif current_distance > last_distance:
            print("❄️ COLDER! You're further away.")
        else:
            print("Neutral. No change in distance.")
            
        # Update state for next loop
        last_distance = current_distance
        turns_left -= 1

    # --- End of Game (Loss) ---
    if turns_left == 0 and player_pos != target_pos:
        print("\n" + "="*30)
        print("Game over! You ran out of turns.")
        print(f"The target was hidden at {target_pos}.")

    # --- Ask to play again ---
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

# --- Main execution block ---
if __name__ == "__main__":
    play_game()
