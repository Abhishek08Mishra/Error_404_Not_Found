import json
import os
from utils import Colors, type_effect

LEADERBOARD_FILE = "leaderboard.json"

# Ensure leaderboard file exists
if not os.path.exists(LEADERBOARD_FILE):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump([], file)

# Load leaderboard data
def load_leaderboard():
    with open(LEADERBOARD_FILE, "r") as file:
        return json.load(file)

# Save leaderboard data
def save_leaderboard(leaderboard):
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file, indent=4)

# Update leaderboard
def update_leaderboard(username, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"username": username, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)  # Sort by score (descending)
    save_leaderboard(leaderboard)

# Display leaderboard
def display_leaderboard():
    leaderboard = load_leaderboard()
    print(f"\n{Colors.BOLD}{Colors.CYAN}=== LEADERBOARD ==={Colors.RESET}")
    if not leaderboard:
        print(f"{Colors.YELLOW}No scores yet! Be the first to top the leaderboard.{Colors.RESET}")
        return
    for idx, entry in enumerate(leaderboard, start=1):
        print(f"{Colors.YELLOW}{idx}. {entry['username']} - Score: {entry['score']}{Colors.RESET}")