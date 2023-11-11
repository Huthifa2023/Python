#1 print all int from 0-150
for x in range(151):
    print(x)

#2 all mutiples of 5 from 5-1000
for num in range(5,1000,5):
    print(num)

#3 int from 1-100, if num divisible by 5 (coding), if divisible by 10 print (coding dojoj)
for num in range(1,100):
    if num%10 == 0:
        print('Coding Dojo')
    elif num%5 == 0:
        print('Coding')
    else:
        print(num)

#4 print the sum of odds from 0 - 500,000
sum = 0
for num in range(0,500000):
    if num%2 != 0:
        sum += num
print(sum)

#5 print positive nums from 2018, decrementing by 4
for num in range(2018,0,-4):
    print(num)

#6 three variables: lowNum, highNum, mult. , 
lowNum = 2 
highNum=9  
mult=3
for x in range(lowNum,highNum+1):
    if x%mult == 0:
        print(x)