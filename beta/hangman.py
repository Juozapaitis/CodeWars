# Hangman

def Hangman(guess, word):
    ans = ""
    for letter in word.lower():
        if letter == guess.lower():
            ans += letter
        else:
            ans += "_"
    return ans