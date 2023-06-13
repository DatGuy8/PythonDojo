for i in range(151):
    print(i)

for j in range(5,1001,5):
    print(j)


for counting in range (1,101):
    if counting%10 == 0:
        print('Coding Dojo')
    elif counting%5 == 0:
        print('Coding')
    else:
        print(counting)

sum = 0
for i in range(0,500001):
    if i%2 == 1:
        sum += i
print(sum)

countbyfour = 2018
while countbyfour > 0:
    print(countbyfour)
    countbyfour -= 4

lowNum=2
highNum=25
mult=2
for i in range(lowNum,highNum+1):
    if i%mult == 0:
        print(i)