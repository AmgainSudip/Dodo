cost_per_pound = 0.50 #dollar
tax_rate = 6.00 #percent

#adding customer dictionary to store the cumulative total
cust_dict = {"amgain1234": 50}  


#printing welcome message to the owner
print('Welcome to the laundromat senor!')

# asking for customer input to either quit the program or continue it
options = input('Enter any number to contine and quit to exit:\n')

#adding while loop with quit to exit the program
while options != 'quit':
    
    #printing the menues
    print('\nWe have following options in our menues:')
    print('1.The total cost customer owes')
    print('2.Change the price per pound or tax rate')
    print('3.Business made from the customer')
    print('4.Quit\n')
    
    #asking for customer input from the menu
    customer_selection = int(input('Select from:1-4\n'))


#adding if-else statement to print what customer asked
    if customer_selection == 1:
        cont = int(input('If you want to continue type 1 otherwise 0:\n'))
        if cont == 1:
            print('The total cost customer owes\n')
                
        #calculating total cost customer needs to pay    
            weight_of_laundry = float(input('Enter the weight of laundry:\n')) #in pounds
            
            subtotal = weight_of_laundry * cost_per_pound
            tax = subtotal * (tax_rate/100)
            total = subtotal + tax
            
            print(f'\nSubtotal:${subtotal:.2f}')
            print(f'Tax:${tax:.2f}')
            print(f'Total:${total:.2f}')
            
        #adding customer total to the amount they spent earlier and storing in a dictionary
            user_id = input('\nEnter your user id '
                            'which includes your last name '
                            'followed by last four digits of your phone number:\n')
            
            if user_id in cust_dict:
                cust_dict[user_id] += total
                print(f'Cumulative total: ${cust_dict[user_id]:.2f}')
            else:
                cust_dict[user_id] = total
                print(f'Cumulative total: ${cust_dict[user_id]:.2f}')
            
            continue
            
        elif cont == 0:
            continue
            

    elif customer_selection == 2:
        cont = int(input('If you want to continue type 1 otherwise 0:\n'))
        if cont == 1:
            print('Change the price per pound or tax rate\n')
            
            #changing either the cost per pound and tax rate or one of them according to customer
            change = int(input('You have following options(1-3):'
                               '\nEnter 1 to update both.'
                               '\nEnter 2 to update tax rate.'
                               '\nEnter 3 to update cost per pound.\n'))
            
            if change == 1:
                cost_per_pound = float(input('\nEnter new cost per pound:\n'))
                tax_rate = float(input('\nEnter new tax rate in percentage:\n'))
                
                print(f'New cost per pound:{cost_per_pound:.2f}')
                print(f'New tax rate :{tax_rate:.2f}')
                
            elif change == 2:
                tax_rate = float(input('\nEnter new tax rate in percentage:\n'))
                print(f'New tax rate:{tax_rate:.2f}')
                
            elif change == 3:
                cost_per_pound = float(input('\nEnter new cost per pound:\n'))
                print(f'New cost per pound:{cost_per_pound:.2f}')
            
            else:
                print('\nYou need to enter either 1, 2 or 3')
            
            continue
            
        elif cont == 0:
            continue
        
    elif customer_selection == 3:
        cont = int(input('If you want to continue type 1 otherwise 0:\n'))
        if cont == 1:
            print('Business made from the customer')
            continue
        
        elif cont == 0:
            continue
        
        

    elif customer_selection == 4:
        cont = int(input('If you want to quit type 1 otherwise 0:\n'))
        if cont == 1:
            options = 'quit'
            continue
        
        elif cont == 0:
            continue

    else:
        print('You need to choose from 1-4')
        continue
else:
    print('Have a good day.')
