print('-----------------------------')
print('------- MONEY TRACKER -------')
print('-----------------------------')

total_expenses = []
class Expense:
    def __init__(self, name, value):
        self.name = name
        self.value = value
def add_amount():
    total_expenses.append(Expense(input('Name of the expense: '), input('value of the expense: $')))
    check_ans()
def show_res():
    print('Name ---------- Value')
    for x in total_expenses:
        print(f'{x.name} ---------- ${float(x.value)}')
def check_ans():
    ans = input('Add new amount? (y/n) ')
    if (ans == 'y'):
        add_amount()
    elif ans == 'n':
        show_res()
    else:
        print('ERROR;')
        check_ans()


add_amount()

