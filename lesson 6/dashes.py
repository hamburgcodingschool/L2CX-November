# ask the user for a word
# seperate the letters with dashes:
# ex: banana becomes b-a-n-a-n-a

def dashifyWord(word):
    dashedWord = ""
    firstTime = True

    for letter in word:
        if firstTime:
            firstTime = False
        else:
            dashedWord += "-"
        dashedWord += letter

    return dashedWord


print("What's the word YO?")
userWord = input()


print(dashifyWord(userWord))