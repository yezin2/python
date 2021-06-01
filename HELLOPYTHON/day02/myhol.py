import random


mine = input("홀/짝을 선택하세요")
pc = ""
result = ""

rand = random.random()
if rand < 0.5:
    pc = "홀"
else:
    pc = "짝"
    

if mine == pc:
    result = "이김!"
else:
    result = "짐ㅠㅠ"
    
print("pc : ", pc)
print("mine : ", mine)
print("result : ", result)