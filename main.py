from states import states
import random

print('This is a game to help you memorize the names of the capitals of all 50 states.\n')

for state in states:
    state["correct"] = 0
    state["wrong"] = 0


play_again = 'yes'

while play_again == 'yes':
    random.shuffle(states)

    for state in states:
        answer = input("What is the capital of " + state["name"] + "?: ").lower()
        if answer == state["capital"].lower():
            print("\nThat's CORRECT!\n")
            state["correct"] += 1
            total = state["correct"] + state["wrong"]
            print(f"You got the right answer {state['correct']} out of {total} tries.\n")
        else:
            print(f"\nThat's INCORRECT! The capital of {state['name']} is {state['capital']}.\n")
            state["wrong"] += 1
            total = state["correct"] + state["wrong"]
            print(f"You got the right answer {state['correct']} out of {total} tries.\n")

    play_again = input("Would you like to play again? (yes/no): \n").lower()