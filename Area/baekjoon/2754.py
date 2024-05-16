"""

"""
score = input()

res = 0
def word(n):
    if n == "+":
        return 0.3
    elif n == "0":
        return 0
    else:
        return -0.3
if score[0] == "A":
    res = 4.0 + word(score[1])
elif score[0] == "B":
    res = 3.0 + word(score[1])
elif score[0] == "C":
    res = 2.0 + word(score[1])
elif score[0] == "D":
    res = 1.0 + word(score[1])
else:
    res = 0.0
print(res)