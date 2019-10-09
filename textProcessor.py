import string

string1 = " "

f = open('input.txt', 'r')
content = f.read()
length = len(content)
checker = False

n=0
for x in range(length):
    char = content[x]
    if char == '#' or char == '@':
        checker = True

    if checker == True:
        if char == " ":
            n = n-1
            checker = False

    if checker == False:
        if char == "?" or char == ',' or char == '.' or char == '!' or char == '\n':
            string1 = string1[:n] + char
            n = n+1
        if char.isalpha() or char.isspace():
            string1 = string1[:n] + char
            n = n+1

fnew = open('output.txt', 'w')
fnew.write(string1)

f.close()
fnew.close()
