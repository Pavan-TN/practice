system_number = 37
attempts = 7
count = 0

while count < attempts:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess > system_number:
        print("Too High")
    elif guess < system_number:
        print("Too Low")
    else:
        print("Correct! You guessed in", count, "attempts.")
        break

if count == attempts and guess != system_number:
    print("Game Over")
    print("The correct number was", system_number)
    print("Attempts used:", count)