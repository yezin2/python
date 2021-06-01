import random


mine = input("가위/바위/보 중 선택하세요")
pc = ""
result = ""

rand = random.random()
if rand < 0.33:
    pc = "가위"
elif rand > 0.33 and rand < 0.66:
    pc = "바위"
else:
    pc = "보"
    

if pc == "가위":
    if mine == "가위":
        result = "비김"
    elif mine == "바위":
        result = "이김!!!"
    elif mine == "보":
        result = "짐ㅠㅜㅠ"
elif pc == "바위":
    if mine == "가위":
        result = "짐ㅠㅜㅠ"
    elif mine == "바위":
        result = "비김"
    elif mine == "보":
        result = "이김!!!"
else: #pc == 보 
    if mine == "가위":
        result = "이김!!!"
    elif mine == "바위":
        result = "짐ㅠㅜㅠ"
    elif mine == "보":
        result = "비김"
    
print("pc : ", pc)
print("mine : ", mine)
print("result : ", result)