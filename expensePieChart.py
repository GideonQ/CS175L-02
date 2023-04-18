#GideonQuaye
#CS175L
#expensePieChart
import matplotlib.pyplot as plt
def main():
    slice_labels = []
    expenses = []
    plt.title('Monthly Expenses')
    
    try:
        infile = open('expenses.txt', 'r')

        for line in infile:
            line = line.rstrip('\n')
            cols = line.split('\t')
            try:
                num = float(cols[1])
                expenses.append(num)
                slice_labels.append(cols[0])
 
                   


            except ValueError:
                print(f"Could not covert line {line.split()}' to a number.")

        print(slice_labels)
        print(expenses)
        plt.pie(expenses, labels=slice_labels)
        plt.show()
        infile.close()

    except IOError:
        print('An error has occurred.')

           


if __name__ == '__main__':
    main()
