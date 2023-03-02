#Gideon Quaye
#CS175L
#Average and Grade Assignment

score=0
def calc_average(total):
    return (score1+score2+score3+score4+score5)/5

def determine_grade(score):
    if score1 or score2 or score3 or score4 or score5 >= 90:
        return 'A'
    elif score1 or score2 or score3 or score4 or score5 >= 80:
        return 'B'
    elif score1 or score2 or score3 or score4 or score5 >= 70:
        return 'C'
    elif score1 or score2 or score3 or score4 or score5 >= 60:
        return 'D'
    else:
        return 'F'

def repeat():
    while True:
        y_n=input("Enter 'yes' if you would like to do another calculation: ")
        if y_n== 'yes':
            return True
        elif y_n== 'no':
            return False
        else:
            print('Please reenter: ')

while True:
    total = 0
    score1=int(input('Enter score 1: '))
    score2=int(input('Enter score 2: '))
    score3=int(input('Enter score 3: '))
    score4=int(input('Enter score 4: '))
    score5=int(input('Enter score 5: '))
    average= calc_average(total)
    grade= determine_grade(score)
    print("Score      Numeric Grade         Letter Grade")
    print('----------------------------------------------')
    print('Score 1: ', score1, grade)
    print('Score 2: ', score2, grade)
    print('Score 3: ', score3, grade)
    print('Score 4: ', score4, grade)
    print('Score 5: ', score5, grade)
    print('Average Score:', average, grade)
    if not repeat():
        break
