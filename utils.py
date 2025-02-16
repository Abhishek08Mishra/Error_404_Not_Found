import time
import sys
import argparse

# ANSI escape codes for colors and styles
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to simulate typing effect
def type_effect(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Function to display a hacker-style loading animation
def hacker_loading(duration=3):
    symbols = ['|', '/', '-', '\\']
    end_time = time.time() + duration  # Run for specified duration
    while time.time() < end_time:
        for symbol in symbols:
            sys.stdout.write(f"\r{Colors.RED}[{symbol}] ERROR 404: BRAIN NOT FOUND... {Colors.RESET}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\r" + " " * 40 + "\r", end="")  # Clear the line

# Enhanced Title Screen
def display_title(text_speed=0.02, loading_time=3):
    print(f"{Colors.BOLD}{Colors.RED}")
    
    border = "=" * 50
    print(border)
    
    type_effect("    A    BBBBB   H   H  III  SSSSS  H   H  EEEEE  K   K", text_speed)
    type_effect("   A A   B    B  H   H   I   S       H   H  E      K  K ", text_speed)
    type_effect("  A   A  BBBBB   HHHHH   I   SSSSS   HHHHH  EEEE   KKK  ", text_speed)
    type_effect(" AAAAAA  B    B  H   H   I      S    H   H  E      K  K ", text_speed)
    type_effect("A     A  BBBBB   H   H  III  SSSSS   H   H  EEEEE  K   K", text_speed)


    print(border)
    
    type_effect(f"{Colors.YELLOW}=== ERROR 404: BRAIN NOT FOUND ==={Colors.RESET}", text_speed)
    type_effect(f"{Colors.MAGENTA}Created by: {Colors.BOLD}Abhishek Mishra{Colors.RESET}", text_speed)
    type_effect(f"{Colors.CYAN}Powered by: Python - The Snake Language{Colors.RESET}", text_speed)
    type_effect(f"{Colors.GREEN}Challenge your knowledge and find your missing brain!{Colors.RESET}", text_speed)
    
    hacker_loading(loading_time)
    
    print(f"{Colors.RESET}\n")
    input(f"{Colors.BOLD}{Colors.BLUE}Press any key to exit...{Colors.RESET}")

# Command-line argument parser
def main():
    parser = argparse.ArgumentParser(description="Display a hacker-style 404 error screen.")
    parser.add_argument("--speed", type=float, default=0.02, help="Typing speed (seconds per character)")
    parser.add_argument("--loadtime", type=int, default=3, help="Loading animation duration (seconds)")
    
    args = parser.parse_args()
    display_title(args.speed, args.loadtime)

if __name__ == "__main__":
    main()
