# STEP 1:
# ask the user for some text, explode the text into an array of strings

userText = "Hello World in a frame"
arrayOfWords = userText.split()

# STEP 2:
# get the length of the lenghtiest word

maxLen = 0
for word in arrayOfWords:
    if len(word) > maxLen:
        maxLen = len(word)

#STEP 3:
# actually print the thing...

newString = ""
for i in range(0, maxLen + 4):
    newString += "*"

print(newString)

# 3.1
# do the lines with words

for word in arrayOfWords:
    extraSpace = ""
    for i in range(0, maxLen - len(word)):
        extraSpace += " "
    print("* " + word + extraSpace + " *")

print(newString)