from states import states
import random

print('This is a game to help you memorize the names of the capitals of all 50 states.\n')

for state in states:
    state["correct"] = 0
    state["wrong"] = 0


play_again = 'yes'

while play_again == 'yes':
    random.shuffle(states)
    score = 0

    for index, state in enumerate(states, 1):
        answer = input(f"{index}) What is the capital of " + state["name"] + "?: ").lower()
        if answer == state["capital"].lower():
            print("\nThat's CORRECT!\n")
            state["correct"] += 1
            score += 1
            total = state["correct"] + state["wrong"]
            print(f"You got this right {state['correct']} out of {total} tries.\n\nYour current score is {score} out of 50.\n")


        else:
            print(f"\nThat's INCORRECT! The capital of {state['name']} is {state['capital']}.\n")
            state["wrong"] += 1
            total = state["correct"] + state["wrong"]
            print(f"You got the right answer {state['correct']} out of {total} tries.\n\nYour current score is {score} out of 50.\n")

    play_again = input("Would you like to play again? (yes/no): \n").lower()