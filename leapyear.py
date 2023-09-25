def leap():
    return leap % 4 == 0 and(leap% 100 == 0 or leap % 400 == 0)
print(leap())
