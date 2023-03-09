#Gideon Quaye
#CS175L
#AverageFromInput

total=0
nums=0
with open('numbers.txt', 'r') as x:
    for line in x:
        number= float(line)
        total+=number
        nums+=1
        print('I read in', nums, 'number(s). Current number is:', number, 'Total is:', total)
avg=total/nums
print('Average:', avg)

