import random
import json
import os
from utils import Colors, type_effect

# Default quiz questions
DEFAULT_QUESTIONS = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
    ("Which programming language is known as the 'Snake Language'?", ["Java", "Python", "C++", "Ruby"], 2),
    ("What does CPU stand for?", ["Central Processing Unit", "Computer Personal Unit", "Central Power Unit", "Control Processing Unit"], 1),
    ("What is 2 + 2?", ["3", "4", "5", "6"], 2),
    ("Which company created the iPhone?", ["Samsung", "Google", "Apple", "Microsoft"], 3),
]

CUSTOM_QUESTIONS_FILE = "custom_questions.json"

# Ensure custom questions file exists
if not os.path.exists(CUSTOM_QUESTIONS_FILE):
    with open(CUSTOM_QUESTIONS_FILE, "w") as file:
        json.dump([], file)

# Load custom questions
def load_custom_questions():
    with open(CUSTOM_QUESTIONS_FILE, "r") as file:
        return json.load(file)

# Save custom questions
def save_custom_questions(questions):
    with open(CUSTOM_QUESTIONS_FILE, "w") as file:
        json.dump(questions, file, indent=4)

# Allow users to add custom questions
def add_custom_question(username):
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}=== ADD CUSTOM QUESTION ==={Colors.RESET}")
    question = input(f"{Colors.YELLOW}Enter your question: {Colors.RESET}").strip()
    options = []
    for i in range(4):
        option = input(f"{Colors.YELLOW}Enter option {i+1}: {Colors.RESET}").strip()
        options.append(option)
    correct_answer = int(input(f"{Colors.YELLOW}Enter the correct answer (1-4): {Colors.RESET}"))
    custom_questions = load_custom_questions()
    custom_questions.append((question, options, correct_answer))
    save_custom_questions(custom_questions)
    print(f"{Colors.GREEN}Question added successfully! Thank you, {username}.{Colors.RESET}")

# Choose quiz type (default, custom, or both)
def choose_quiz_type():
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}=== CHOOSE QUIZ TYPE ==={Colors.RESET}")
    print(f"{Colors.CYAN}1. Default Questions")
    print("2. Custom Questions")
    print("3. Both Default and Custom Questions")
    choice = input(f"{Colors.YELLOW}Enter your choice (1-3): {Colors.RESET}")
    if choice == "1":
        return "default"
    elif choice == "2":
        return "custom"
    elif choice == "3":
        return "both"
    else:
        print(f"{Colors.RED}Invalid choice! Defaulting to 'Default Questions'.{Colors.RESET}")
        return "default"

# Run the quiz
def run_quiz(username, quiz_type="default"):
    default_questions = DEFAULT_QUESTIONS
    custom_questions = load_custom_questions()

    if quiz_type == "default":
        questions = default_questions
    elif quiz_type == "custom":
        questions = custom_questions
    elif quiz_type == "both":
        questions = default_questions + custom_questions

    if not questions:
        print(f"{Colors.RED}No questions available! Please add custom questions.{Colors.RESET}")
        return 0

    score = 0
    total_questions = len(questions)
    random.shuffle(questions)  # Shuffle questions for variety
    type_effect(f"{Colors.BOLD}{Colors.MAGENTA}Welcome to the Quiz, {username}! Prove your skills.{Colors.RESET}")
    for idx, (question, options, correct_answer) in enumerate(questions, start=1):
        print(f"\n{Colors.BOLD}{Colors.BLUE}Question {idx}/{total_questions}{Colors.RESET}")
        user_choice = display_question(question, options)
        if evaluate_answer(user_choice, correct_answer):
            score += 1
        # time.sleep(1)
    type_effect(f"{Colors.BOLD}{Colors.CYAN}Quiz completed! Calculating your score...{Colors.RESET}")
    # time.sleep(2)
    display_score(score, total_questions)
    return score

# Display a question
def display_question(question, options):
    print(f"\n{Colors.YELLOW}{question}{Colors.RESET}\n")
    for idx, option in enumerate(options, start=1):
        print(f"{Colors.CYAN}{idx}. {option}{Colors.RESET}")
    while True:
        try:
            choice = int(input(f"{Colors.BOLD}{Colors.MAGENTA}Enter your choice (1-{len(options)}): {Colors.RESET}"))
            if 1 <= choice <= len(options):
                return choice
            else:
                print(f"{Colors.RED}Invalid choice! Try again.{Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Please enter a number!{Colors.RESET}")

# Evaluate the answer
def evaluate_answer(user_choice, correct_answer):
    if user_choice == correct_answer:
        print(f"{Colors.GREEN}Correct! You're a genius.{Colors.RESET}")
        return True
    else:
        print(f"{Colors.RED}Wrong! The correct answer was: {correct_answer}.{Colors.RESET}")
        return False

# Display the final score
def display_score(score, total_questions):
    print(f"\n{Colors.BOLD}{Colors.CYAN}=== FINAL SCORE ==={Colors.RESET}")
    print(f"{Colors.YELLOW}You scored {score} out of {total_questions}.{Colors.RESET}")
    if score == total_questions:
        print(f"{Colors.GREEN}Perfect! You're a true hacker.{Colors.RESET}")
    elif score >= total_questions // 2:
        print(f"{Colors.YELLOW}Not bad! Keep practicing.{Colors.RESET}")
    else:
        print(f"{Colors.RED}Better luck next time!{Colors.RESET}")