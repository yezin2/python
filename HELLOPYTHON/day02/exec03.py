dan = int(input("출력할 구구단은?"))

print("출력할 구구단 {} 단".format(dan))

for i in range(1,10):
    print(str(dan) + " * " + str(i) + " = " + str(dan*i))