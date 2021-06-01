fir = int(input("fir 숫자를 입력하세요"))
sec = int(input("sec 숫자를 입력하세요"))
res = 0

for i in range(fir,sec+1):
    res += i

print("모든 숫자의 합은 {} 입니다".format(res))