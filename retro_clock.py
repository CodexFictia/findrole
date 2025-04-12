import os
import time
from datetime import datetime

# Define the ASCII art for each digit and colon
digits = {
    "0": [
        " __ ",
        "|  |",
        "|  |",
        "|  |",
        "|__|"
    ],
    "1": [
        "    ",
        "   |",
        "   |",
        "   |",
        "   |"
    ],
    "2": [
        " __ ",
        "   |",
        " __|",
        "|   ",
        "|__ "
    ],
    "3": [
        " __ ",
        "   |",
        " __|",
        "   |",
        " __|"
    ],
    "4": [
        "    ",
        "|  |",
        "|__|",
        "   |",
        "   |"
    ],
    "5": [
        " __ ",
        "|   ",
        "|__ ",
        "   |",
        " __|"
    ],
    "6": [
        " __ ",
        "|   ",
        "|__ ",
        "|  |",
        "|__|"
    ],
    "7": [
        " __ ",
        "   |",
        "   |",
        "   |",
        "   |"
    ],
    "8": [
        " __ ",
        "|  |",
        "|__|",
        "|  |",
        "|__|"
    ],
    "9": [
        " __ ",
        "|  |",
        "|__|",
        "   |",
        " __|"
    ],
    ":": [
        "   ",
        " o ",
        "   ",
        " o ",
        "   "
    ]
}

def print_retro_clock():
    # Get current time in HH:MM:SS format
    now = datetime.now().strftime("%H:%M:%S")
    
    # Prepare a list to hold each of the 5 lines of the ASCII art
    lines = [""] * 5
    
    # Build each line by appending the corresponding ASCII art of each character
    for char in now:
        # Get the ASCII art for the current character (digit or colon)
        art = digits.get(char, ["    "] * 5)
        for i in range(5):
            lines[i] += art[i] + "  "  # Adding a gap between characters
    
    # Print each line to display the full clock
    for line in lines:
        print(line)

# Main loop to update the clock every second
try:
    while True:
        # Clear the screen (works for Windows and UNIX-like systems)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_retro_clock()
        time.sleep(1)
except KeyboardInterrupt:
    # Allow the user to exit the clock using Ctrl+C
    print("\nClock stopped.")