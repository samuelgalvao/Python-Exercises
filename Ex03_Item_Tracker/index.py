items = dict()


def menu():
    print('-----------------------------------------')
    print('--------------- ITEMS TRACKER -----------')
    print('-----------------------------------------')
    print('1.Add Item to inventory;')
    print('2.Search Item;')

    option = int(input('What you want? '))
    if option == 1:
        add_item()
    elif option == 2:
        search()
    else:
        print('INVALID RESPONSE;')

def search():
    for key in items:
        print(f'{key}: {items[key]}')

def add_item():
    name = input('Name: ')
    values = {'cost': 0, 'price': 0, 'stock': 0}
    
    for item in values:
        values[item] = input(f'{item}: ')
        


    items[name] = values
    def check():
        ans = input('Add more items? (y/n) ')
        if ans == 'y':
            add_item()
        elif ans == 'n':
            menu()
        else:
            print('ERROR;')
            check()
    check()
        
menu()