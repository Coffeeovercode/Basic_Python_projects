def run_quiz():
    """
    Main function to run the quiz game.
    """
    
    # A list of dictionaries, where each dictionary represents a question
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
            "answer": "C"
        },
        {
            "question": "Which language is this script written in?",
            "options": ["A. Java", "B. Python", "C. C++", "D. JavaScript"],
            "answer": "B"
        },
        {
            "question": "What does 'CPU' stand for?",
            "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Program Unit", "D. Core Power Utility"],
            "answer": "A"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
            "answer": "C"
        }
    ]

    score = 0
    
    print(" Welcome to the Goblet Game! 🧠\n")

    # Loop through each question
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        # Get user's answer
        while True:
            user_answer = input("Your answer (A, B, C, or D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        
        # Check if the answer is correct
        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")
            
    # --- End of Game ---
    print("="*30)
    print("🎉 Quiz Finished! 🎉")
    print(f"Your final score is: {score}/{len(questions)}")
    print("="*30)

# Start the game
if __name__ == "__main__":
    run_quiz()
