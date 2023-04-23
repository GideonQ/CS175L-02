#Gideon Quaye
#CS175L
#AverageFromInputExceptionHandling

def read_file(file):
    total=0
    nums=0
    try:
        with open('numbers.txt', 'r') as x:
            for line in x:
                  number=float(line)
                  total+=number
                  nums+=1
                  print('I read in', nums, 'number(s). Current number is:', number, 'Total is:', total)
    except (IOError, ValueError) as x:
        print('Error', x)
    return nums

def calc_avg(numbers):
    total=sum(numbers)
    count=len(numbers)
    if count == 0:
        return 0
    else:
        return total/count

def f_average(average):
    avg=calculate_average(numbers)
    print('Average:', average)

def main():
    numbers = read_file('numbers.txt')
    average = calc_avg(numbers)
    f_average(average)

if __name__ == "__main__":
    main()
