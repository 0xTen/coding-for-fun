import random

print()
print("          # WELCOME TO THE GUESSER #")
print("          THE MOST BORING GAME EVER!!")
print("----------------------------------------------------#")
print("I'll pick a number from 1 to 10 and you can guess")
print("three times. If the answer is correct you score 10")
print("points. For every wrong guess you'll get a hint")
print("and the score, for this round, will be reduced by 3.")
print("----------------------------------------------------#")
print()


# HINT 1 -- EVEN OR ODD

def factorization(number):
    fact = []
    i = 2
    while i <= number:
        if number % i == 0:
            fact.append(i)
            number //= i
        else:
            i += 1
    return fact


# HINT 2 -- PRIME OR NOT

def prime_check(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print("not a prime number")
                break
        else:
            print("prime number")

    else:
        print("not a prime number")


# VALIDATE INPUT

def validate():
    while True:
        answer = input("==>")
        try:
            int_answer = int(answer)
            if 1 <= int_answer <= 10:
                return int_answer
            else:
                print("Invalid Input! must be between 1 and 10!")
        except ValueError:
            if answer == "exit" or answer == "q" or answer == "quit":
                print("Bye!")
                exit(0)
            else:
                print("Invalid Input! Must be a number!")


# START GAME

def start():
    a = input("Do you want to start the game?(y/n)")
    return a


def run():
    current_round = 1
    score = 0
    while current_round <= 10:
        print()
        print(f"ROUND {current_round}/10")
        print(f"SCORE {score}")
        print("exit/quit/q to exit")
        print("###################")
        number = random.randint(1, 10)
        # DEBUB -- PRINT NUMBER
        # print(number)
        print("Guess my number:")
        answer = validate()
        # 1st TRY
        if answer == number:
            print("Correct!")
            current_round = current_round + 1
            score = score + 10
            print("You scored 10 points")
        else:
            print("Wrong answer! 1/3")
            print("Hint 1:")
            fac = factorization(number)
            if 2 in fac:
                print("Even number!")
            else:
                print("Odd number!")
            answer = validate()
            # 2nd TRY
            if answer == number:
                print("Correct!")
                current_round = current_round + 1
                score = score + 7
                print("You scored 7 points")
            else:
                print("Wrong answer! 2/3")
                print("Hint 2:")
                prime_check(number)
                answer = validate()
                # 3rd TRY
                if answer == number:
                    print("Correct!")
                    score = score + 4
                    print("You scored 4 points")
                    current_round = current_round + 1
                else:
                    print("Wrong answer! 3/3")
                    print("You scored 0 points :(")
                    current_round = current_round + 1
    else:
        # END GAME
        print("Your Final Score is ", score)
        exit(1)


launch = start()
# EXIT GAME
while True:
    if launch == "n" or launch == "N" or launch == "no" or launch == "NO":
        print("See you next time! Bye!")
        exit(0)
    else:
        # BEGIN
        if launch == "y" or launch == "Y" or launch == "yes" or launch == "YES":
            run()
        else:
            # LOOP
            launch = start()
