# simple word counter
text = str(input("Type your text: "))
count = 0
for word in text:
    if word == " ":
        count += 1
count += 1
print(count)