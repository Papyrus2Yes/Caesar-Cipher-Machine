alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
rearrangedAlphabet = []
firstInput = str(input("A is equal to: "))
firstInput = firstInput.upper()
thirdInput = str(input("Convert cipher into binary? "))
if thirdInput.lower() == "yes":
    thirdInput = True
else:
    thirdInput = False
if not firstInput in alphabet:
    print("Input not in alphabet. Default value is 'R'")
    firstInput = "R"
if len(firstInput) > 1:
    print("Input is not a single character. Default value is 'Z'")
    firstInput = "Z"
secondInput = str(input("Move forwards? "))
if secondInput.lower() == "yes":
    secondInput = True
else:
    secondInput = Frsalse
location = alphabet.index(firstInput)
if secondInput:
    for x in range(len(alphabet)):
        if location > 25:
            location = 0
            rearrangedAlphabet.append(alphabet[location])
            location = location + 1
        else:
            rearrangedAlphabet.append(alphabet[location])
            location = location + 1
elif not secondInput:
    for y in range(len(alphabet)):
        if location < 0:
            location = 25
            rearrangedAlphabet.append(alphabet[location])
            location = location - 1
        else:
            rearrangedAlphabet.append(alphabet[location])
            location = location - 1
newword = []
word = str(input("Sentence to be ciphered "))
wordsplit = []
wordsplitcon = ""
punctuation = [" ", ",", "!", ":", ";", "?", "."]
for letter in word:
    if letter in punctuation:
        newword.append(punctuation[punctuation.index(letter)])
    else:
        index = alphabet.index(letter.upper())
        newword.append(rearrangedAlphabet[index])
newword.insert(0, " ")
if secondInput:
    newword.insert(0, "T")
else:
    newword.insert(0, "F")
newword.insert(0, rearrangedAlphabet[0])
if not thirdInput:
    for letter in newword:
        wordsplitcon = wordsplitcon + str(letter)
else:
    word2 = ""
    for letter in newword:
        binary = bin(ord(str(letter)))[2:]
        word2 = word2 + str(chr(int(binary, 2)))
        wordsplitcon = wordsplitcon + str(binary) + str(" ")
    print("Ciphered word not in binary:", word2)
print("Ciphered sentence:", wordsplitcon)
