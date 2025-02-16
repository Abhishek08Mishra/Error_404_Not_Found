import sys
from auth import register, login, reset_password
from quiz import run_quiz, add_custom_question
from leaderboard import display_leaderboard
from utils import display_title, hacker_loading, type_effect

def main_menu():
    while True:
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}=== MAIN MENU ==={Colors.RESET}")
        print(f"{Colors.CYAN}1. Login")
        print("2. Register")
        print("3. Reset Password")
        print("4. View Leaderboard")
        print("5. Add Custom Question")
        print("6. Exit")
        choice = input(f"{Colors.YELLOW}Enter your choice (1-6): {Colors.RESET}")
        if choice == "1":
            username = login()
            if username:
                hacker_loading()
                play_quiz(username)
        elif choice == "2":
            register()
        elif choice == "3":
            reset_password()
        elif choice == "4":
            display_leaderboard()
        elif choice == "5":
            username = login()
            if username:
                add_custom_question(username)
        elif choice == "6":
            type_effect(f"{Colors.BOLD}{Colors.BLUE}Thanks for playing! Exiting the system...{Colors.RESET}")
            hacker_loading()
            sys.exit()
        else:
            print(f"{Colors.RED}Invalid choice! Try again.{Colors.RESET}")

def play_quiz(username):
    from quiz import choose_quiz_type
    quiz_type = choose_quiz_type()
    score = run_quiz(username, quiz_type)
    update_leaderboard(username, score)

def update_leaderboard(username, score):
    from leaderboard import update_leaderboard as update_lb
    update_lb(username, score)

if __name__ == "__main__":
    from utils import Colors
    display_title()
    hacker_loading()
    main_menu()