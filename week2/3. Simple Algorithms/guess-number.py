top = 100;
bottom = 0
print("Please think of a number between " + str(bottom) + " and " + str(top) + "! ")
answer = ""

guess = (top - bottom) / 2
while answer != "c" or answer != "l" or "h":
    print("Is your secret number " + str(int(guess)) + "? ")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if answer == "c":
        print("Game over. Your secret number was: " + str(int(guess)))
        break
    elif answer == "h":
        top = guess
        guess = int((bottom + guess) / 2)
    elif answer == "l":
        bottom = guess
        guess += int((top - guess) / 2)
    else:
        print("Sorry, I did not understand your input.")

# End of everything
