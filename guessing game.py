secretword = "diamond"
guess = ""
guesscount = 0
guesslimit = 3
outofguesses = False
while secretword != guess and not (outofguesses):
    if guesscount < guesslimit:
        guess = input("enter guess : ")
        guesscount += 1
    else:
        outofguesses = True

if outofguesses:
    print ("out of Guesses, you lose")
else:
    print("you win")
