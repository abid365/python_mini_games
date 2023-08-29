yourName = input("Type your name: ")
theirName = input("Type their name: ")
# True love
lowerCaseString = (yourName + theirName).lower()
t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")
true = t + r + u + e

l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")
e = lowerCaseString.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
lvScoreInteger = int(love_score)

if lvScoreInteger < 10 or lvScoreInteger > 90:
    print(f"Your score is {lvScoreInteger} you go together like coke and mentos")
elif lvScoreInteger <= 40 or lvScoreInteger >= 50:
    print(f"Your score is {lvScoreInteger}, you are alright together")
else:
    print(f"Your score is {lvScoreInteger}")
