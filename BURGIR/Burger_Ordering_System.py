#                                                                  GROUP 1

# MEMBERS:
# JHON CARLO PALATINO
# JUSTIN CANEDO
# TERRENCE DIONELA


# PROGRAM WILL START FUCTIONS TO PRINT INTRODUCTION
def show_header():
    print("Welcome to CJT BURGERS SHOP Nice to Meat U")
    
# FUNCTIONS TO CALL IF THE CUSTOMER HAS AN ORDER   
def show_burger(burgers):
    if len(burgers)==0:
        print("No order yet.")
        
    else:
        num = 1
        for burger in burgers:
            print(f"{num}: {burger[0]} patties in burger with { ', '.join(burger[1])}")
            num += 1 
# FUNCTIONS USE FOR THE CUSTOMER TO CHOOSE 
def receive_customer_option():
    option = input("(A)dd Order, (R)emove Order,  (S)ave Order, (O)pen Order , (Q)uit: ")[0].upper()
    return option
    
# FUNCTION USED TO ADDING AN ORDER / BURGER    
def add_burger(burgers):    
    pattie = input('please enter how many patties you want (2,3,5): ')[0].upper()
    print("side dishes: ")
    side_dishes = []
 # INFINITE LOOP THE CUSTOMER DECIDE WHEN TO STOP TO ADDING AN SIDE DISH   
    while True:
        side_dish = input('Please choose side dish or drink or enter to stop : ')
        if side_dish == '':break
        side_dishes.append(side_dish)
        
    burger = (pattie,side_dishes)
    burgers.append(burger)

   
# FUNCTION TO REMOVE ORDER/ BURGER 
def remove_burger(burgers):
    
    num_to_remove = int(input('Please enter number of burger to remove: '))
        
    
    if(num_to_remove>=0 and num_to_remove < len(burgers)):
         del burgers[num_to_remove-1]
    else:
        print('That burger does not exist.')
        
# FUNCTION USED TO SAVE CUSTOMER'S ORDER        
def save_burger_order(burgers):
    file_name = input('Please enter file name: ')
    f = open(file_name, 'w')
    for burger in burgers:
        sides_list = '\t'.join(burger[1])
        f.write(f"{burger[0]}\t{sides_list}\n")
    f.close()
    
# FUNCTION USED IF THE CUSTOMER WANTS TO CONTINUE HIS/HER ORDER THAT WAS SAVED    
def open_burger_order(burgers):
    burgers.clear()
    file_name = input('Please enter file name: ')
    f = open(file_name, 'r')
    while True:
        line = f.readline()[:-1]
        if not line :break
        elements = line.split('\t')
        pattie = elements[0]
        side_dishes = elements[1:]
        burger = (pattie,side_dishes)
        burgers.append(burger)

# FUNCTION USED IF THE CUSTOMER DECIDE TO NOT ORDER
def show_goodbye():
    print("Thank you for visiting CJT Restaurant.")

if __name__== "__main__":
   
    show_header()
    
    
    burgers = []
      
    #Start INFINITE LOOP
    while True:

        show_burger(burgers)

        option = receive_customer_option()
        
        # CONDITIONAL IF USER WANTS TO ORDER
        if option == 'A':
            add_burger(burgers)
        
        # CONDITIONAL IF USER WANTS TO REMOVE ORDER
        elif option == 'R':
            remove_burger(burgers)
            
        # CONDITIONAL IF USER WANTS TO SAVE ORDER
        elif option == 'S':
            save_burger_order(burgers)
            
        # CONDITIONAL IF USER WANTS TO OPEN THE SAVED ORDER
        elif option == 'O':
            open_burger_order(burgers)
            
        # CONDITIONAL IF USER WANTS TO QUIT
        elif option == 'Q': break
        
        # CONDITION IF THE USER PICK THE WRONG LETTER
        else:
            print('Please pick among the List')
    

    show_goodbye()