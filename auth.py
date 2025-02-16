import json
import os
from getpass import getpass
from utils import Colors

USER_DATA_FILE = "users.json"

# Ensure data file exists
if not os.path.exists(USER_DATA_FILE):
    with open(USER_DATA_FILE, "w") as file:
        json.dump({}, file)

# Load user data
def load_users():
    with open(USER_DATA_FILE, "r") as file:
        return json.load(file)

# Save user data
def save_users(users):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)

# Register a new user
def register():
    users = load_users()
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}=== REGISTER ==={Colors.RESET}")
    username = input(f"{Colors.YELLOW}Enter a username: {Colors.RESET}").strip()
    if username in users:
        print(f"{Colors.RED}Username already exists! Try again.{Colors.RESET}")
        return False
    password = getpass(f"{Colors.YELLOW}Enter a password: {Colors.RESET}")
    confirm_password = getpass(f"{Colors.YELLOW}Confirm your password: {Colors.RESET}")
    if password != confirm_password:
        print(f"{Colors.RED}Passwords do not match! Try again.{Colors.RESET}")
        return False
    users[username] = {"password": password, "score": 0}
    save_users(users)
    print(f"{Colors.GREEN}Registration successful! Welcome, {username}.{Colors.RESET}")
    return True

# Log in a user
def login():
    users = load_users()
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}=== LOGIN ==={Colors.RESET}")
    username = input(f"{Colors.YELLOW}Enter your username: {Colors.RESET}").strip()
    if username not in users:
        print(f"{Colors.RED}Username does not exist! Try registering.{Colors.RESET}")
        return None
    password = getpass(f"{Colors.YELLOW}Enter your password: {Colors.RESET}")
    if users[username]["password"] != password:
        print(f"{Colors.RED}Incorrect password! Try again.{Colors.RESET}")
        return None
    print(f"{Colors.GREEN}Login successful! Welcome back, {username}.{Colors.RESET}")
    return username

# Reset a user's password
def reset_password():
    users = load_users()
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}=== RESET PASSWORD ==={Colors.RESET}")
    username = input(f"{Colors.YELLOW}Enter your username: {Colors.RESET}").strip()
    if username not in users:
        print(f"{Colors.RED}Username does not exist! Try registering.{Colors.RESET}")
        return False
    old_password = getpass(f"{Colors.YELLOW}Enter your old password: {Colors.RESET}")
    if users[username]["password"] != old_password:
        print(f"{Colors.RED}Incorrect old password! Try again.{Colors.RESET}")
        return False
    new_password = getpass(f"{Colors.YELLOW}Enter your new password: {Colors.RESET}")
    confirm_password = getpass(f"{Colors.YELLOW}Confirm your new password: {Colors.RESET}")
    if new_password != confirm_password:
        print(f"{Colors.RED}Passwords do not match! Try again.{Colors.RESET}")
        return False
    users[username]["password"] = new_password
    save_users(users)
    print(f"{Colors.GREEN}Password reset successful!{Colors.RESET}")
    return True