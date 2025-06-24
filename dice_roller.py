import random
import time

# Unicode characters for dice faces (⚀ to ⚅)
DICE_FACES = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

def roll_dice():
    print("Rolling the dice", end="")
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    result = random.randint(1, 6)
    print(f"\nYou rolled a {result} {DICE_FACES[result]}\n")

# Main loop
while True:
    user_input = input("Press Enter to roll the dice or type 'exit' to quit: ").strip().lower()
    if user_input == 'exit':
        print("Thanks for playing! 🎲")
        break
    roll_dice()
