a = range(1,10)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

for i in range(2,10):
    print("===============" + str(i)+ "단" + "===============")
    for j in range(1,10):
        print(str(i) + " * " + str(j) + " = " + str(j * i))
        
print("hel",end="")
print("lo")