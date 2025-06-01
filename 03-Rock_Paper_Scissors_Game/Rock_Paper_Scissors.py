import random

print("ROCK , PAPER , SCISSORS".center(100, "-"))
print("Possible choices : rock , paper , scissor")

human_score = 0
comp_score = 0
ch = ["rock", "paper", "scissor"]

while True:
    human_ch = input("Enter choice: ").lower()

    if human_ch not in ch:
        print("Invalid choice. Please choose from rock, paper, or scissor.")
        continue

    comp_ch = random.choice(ch)

    print("Your choice: ", human_ch)
    print("Computer choice: ", comp_ch)

    if human_ch == comp_ch:
        print("It's a tie!")
    elif (human_ch == "rock" and comp_ch == "scissor") or \
         (human_ch == "paper" and comp_ch == "rock") or \
         (human_ch == "scissor" and comp_ch == "paper"):
        print("You won!")
        human_score += 1
    else:
        print("Computer won!")
        comp_score += 1

    repeat = input("Play again? (yes to continue / no to exit): ").lower()
    if repeat == "no":
        break

print("-" * 100)
print("Final Score".center(100))
print(f"Your score: {human_score} | Computer score: {comp_score}")

if human_score > comp_score:
    print("You won the game!")
elif human_score < comp_score:
    print("Computer won the game!")
else:
    print("It's a tie overall!")
