#WONG KANG SHIN
#TP068522

#Main Menu
def menu():
    print('\nWelcome to OCEAN Sdn Bhd'
            '\nPlease enter mode of user'
            '\n1. Admin'
            '\n2. New customer'
            '\n3. Registered Customer')
    mode = str(input('\nSelect mode of user (1/2/3): '))

    if mode == '1':
        admin_login()
    elif mode == '2':
        N_cust_menu()
    elif mode == '3':
        R_cust_login()
    else:
        print('\nInvalid input')
        menu()


#Secondary Menu
def admin_login():
    username = str(input('Enter Username: '))
    password = str(input('Enter Password: '))

    if username == 'Admin' and password == 'Admin':
        print('\nAccess Granted!!')
        admin_menu()
        
    else :
        print('\nInvalid Username and Password\n')
        menu()

def admin_menu():
    print('\nAdmin Menu\n'
            '\n1. Upload Medicine Details'
            '\n2. View all Medicine Information'
            '\n3. Modify Medicine Information'
            '\n4. Delete Medicine Information'
            '\n5. Search Specific Medicine Information'
            '\n6. View all orders of Customers'
            '\n7. Search order of specific customer'
            '\n8. Exit')

    option = str(input('\nSelect what action to be done: '))
    if option == '1':
        admin_upload()
    elif option == '2':
        admin_view_med()
    elif option == '3':
        admin_modify()
    elif option == '4':
        admin_delete()
    elif option == '5':
        admin_search()
    elif option == '6':
        admin_view_order()
    elif option == '7':
        admin_view_s_order()
    elif option == '8':
        menu()
    else :
        print('\nInvalid input')
        admin_menu()

def N_cust_menu():
    print('\nNew Customer Menu :'
          '\n1. View all Medicine Details'
          '\n2. Registration'
          '\n3. Exit')
    option = str(input('\nEnter what action you would take (1/2/3): '))

    if option == '1':
        N_cust_view()
    elif option == '2':
        N_cust_register()
    elif option == '3':
        menu()
    else :
        print('Invalid Input')
        N_cust_menu()
        
    

def R_cust_login():
    user = str(input('Username : '))
    password = str(input('Password : '))
    count = 0
    available = 0
    
    c = open('member.txt','r')
    for line in c :
        if count == 0:
            if line.strip('\n') == user :
                count = count + 1

        
        elif count == 1:
            if line.strip('\n') == password :
               print('Access granted')
               available = 1
               count = count + 1
               account = open('account.txt','w')
               account.truncate()
               account.write(user)
               account.close()
            else :
                count = 5
        else :
            break
        
    if available == 0 :
        print('\nInvalid user or password')
        menu()
    else :
        R_cust_menu()

def R_cust_menu():
    print('Registed Customer Menu'
          '\n1. View all Medicine Details'
          '\n2. Place order and payment'
          '\n3. View orders made'
          '\n4. View personal information'
          '\n5. Exit')
    option = str(input('\nEnter what action you would take (1/2/3..): '))

    if option == '1':
        r_cust_view()
    elif option == '2':
        r_cust_order()
    elif option == '3':
        r_cust_record()
    elif option == '4':
        r_cust_info()
    elif option == '5':
        menu()
    else:
        print('Invalid input')
        R_cust_menu()

#Detailed Menu : Admin

def admin_upload():
    med_name = str(input('Enter name of Medicine :'))
    med_des = str(input('Enter Description :'))
    med_price = str(input('Enter Price of Med:'))

    med_file = open('medicine.txt','a+')
    
    med_file.write(med_name)
    med_file.write('\n')
    med_file.write(med_des)
    med_file.write('\n')
    med_file.write(med_price)
    med_file.write('\n')
    med_file.write('\n')

    print('\nInformation uploaded')
    med_file.close()
    admin_menu()

def admin_view_med():
    a = open('medicine.txt','r')
    print(a.read())
    admin_menu()
    
def admin_modify():
    available = 0
    med = str(input('Name of medicine to configure. <enter> to Cancel : '))
    file = open('medicine.txt','r')
    print()

    #Showing medicine written
    count = 0
    if med == '':
        admin_menu()

    elif med != '' :
        for line in file :
            if count == 0:
                if line.strip('\n') == med:
                    print (line,end='')
                    count = count + 1
                    available = 1
        
            elif count <= 2:
                print (line,end='')
                count = count + 1
            else :
                break

    if available == 0:
        print('No medicine found\n')
        admin_modify()
        
    #What info to configure
    option = str(input('\n1. Configure Name'
                       '\n2. Configure Description'
                       '\n3. Configure Price'
                       '\n\nWhat information would you like to configure (1/2/3). <enter> to Cancel: '))
    

    if option == '1':
        new = str(input('Please type new information : '))
        with open('medicine.txt','r') as f:
            lines = f.readlines()
        with open('medicine.txt','w') as f:
            for line in lines:
                    if line.strip('\n') != med :
                        f.write(line)
                    elif line.strip('\n') == med:
                        f.write(new)
                        f.write('\n')
    elif option =='2':
        new = str(input('Please type new information : '))
        with open('medicine.txt','r') as f:
            lines = f.readlines()
        with open('medicine.txt','w') as f:
            count = 0 #to skip 4 lines(related to medicine)
            for line in lines:
                if count == 0:
                    if line.strip('\n') != med :
                        f.write(line)
                    elif line.strip('\n') == med :
                        f.write(line)
                        count = count + 1
                        continue
                    
                elif count == 1:
                    f.write(new)
                    f.write('\n')
                    count = count -1
                    
                else :
                    f.write(line)
                    
    elif option =='3':
        new = str(input('Please type new information : '))
        with open('medicine.txt','r') as f:
            lines = f.readlines()
        with open('medicine.txt','w') as f:
            count = 0 #to skip 4 lines(related to medicine)
            for line in lines:
                if count == 0:
                    if line.strip('\n') != med :
                        f.write(line)
                    elif line.strip('\n') == med :
                        f.write(line)
                        count = count + 1
                        continue
                    
                elif count == 1:
                    f.write(line)
                    count = count + 1

                elif count == 2:
                    f.write(new)
                    f.write('\n')
                    count = 0
                    
                else :
                    f.write(line)

    elif option == '':
        admin_menu()
        
    else :
        print('\nInvalid Input')
        admin_menu()

    print('Changes have been made!')
    admin_menu()
    file.close()
def admin_delete():
    med = str(input('Name of medicine to delete : '))
    available = 0
                 
    with open('medicine.txt','r') as f:
        lines = f.readlines()
    with open('medicine.txt','w') as f:
        count = 4 #to skip 4 lines(related to medicine)
        for line in lines:
            if count == 4 or count == 0:
                if line.strip('\n') != med :
                    f.write(line)
                elif line.strip('\n') == med :
                    available = 1
                    count = count -1
                    continue
            else :
                count = count -1
                continue

    if available == 1:
        print('Medicne data has been deleted.')
    else :
        print('\nNo medicine found')
    admin_menu()
    file.close()  
def admin_search():
    med = str(input('Name of medicine to search: '))
    file = open('medicine.txt','r')
    print()
    available = 0

    count = 0
    for line in file :
        if count == 0:
            abd = line.strip('\n')
            if abd.startswith(med):
                print (line,end='')
                count = count + 1
                available = 1
        
        elif count <= 2:
            print (line,end='')
            count = count + 1
        else :
            break

    if available == 0 :
        print('No medicine name found')

    admin_menu()
    file.close()
def admin_view_order():
    file = open('order.txt','r')
    print(file.read())
    admin_menu()

    
def admin_view_s_order():
    order = open('order.txt','r')
    order.seek(0)
    name = str(input('Enter Name of Customer : '))
    available = 0

    print()
    count = 0
    for line in order:
        if count == 0:
            if line.strip('\n') == name :
                print(line)
                count = 1
                available = 1
            else :
                continue
            
            
        elif count == 1:
            if line.strip('\n') != '---------------':
                print(line)
                
            elif line.strip('\n') == '---------------':
                print(line)
                count = 0
            else :
                print('no')
        else:
            print('no')
    if available == 0 :
        print('No name found')

    order.close()
    admin_menu()

#New Customer functions

def N_cust_view():
    file = open('medicine.txt','r')
    print(file.read())
    N_cust_menu()
    file.close()

def N_cust_register():
    name = str(input('Enter Username : '))
    ic = str(input('Enter IC Number xxxxxx-xx-xxxx : '))
    phone = str(input('Enter phone number : '))

    right = 0
    while right == 0:
        password1=str(input('Enter Password (<ENTER> TO CANCEL) : '))
        if password1 != '':
            password2=str(input('Enter Confirm Password : '))

        elif password1 == '':
            menu()

        if password1 == password2:
            right = 1
            break
        else :
            print('\nPassowrd do not match\n')

    c_file = open('member.txt','a+')

    c_file.write('\n')
    c_file.write('\n')
    c_file.write(name)
    c_file.write('\n')
    c_file.write(password1)
    c_file.write('\n')
    c_file.write(ic)
    c_file.write('\n')
    c_file.write(phone)
    
    c_file.close()

    print('\nAccount Registered')
    menu()
    c_file.close()

#Registered Customer Functions
def r_cust_view():
    file = open('medicine.txt','r')
    print(file.read())
    R_cust_menu()
    file.close() 

def r_cust_order():
    m_file = open('medicine.txt','r')
    print(m_file.read())
    print()

    order = 0
    temp = open('t.order.txt','a+')
    temp.seek(0)
    temp.truncate()
    
    account = open('account.txt','r')
    account.seek(0)
    
    for line in account:
        temp.write(line)

    tprice = 0
    avai = 0
    while order == 0:
        item = str(input('Enter name of medicine wanted ("Enter when complete"): '))
        if item.strip() != '':
            quantity = int(input('Enter quantity wanted [ONLY NUMBERS]: '))
            
            printprice = str(quantity)
            store = open('medicine.txt','r')

            #Find price of item
            count = 0
            for line in store :
                if count == 0:
                   if line.strip('\n') == item:
                        count = 1
                        avai = 1
                elif count == 1:
                    count = 2
                elif count == 2:
                    a = []
                    a.append(line.strip('\n'))
                    tag = int(a[0])
                    tprice = tprice + tag*quantity
                    count = count + 1
                    
                else :
                    continue
            if avai == 1:
                store.close()

            #Copy information into temp order
                temp.write('\n')
                temp.write(item)
                temp.write(':\n')
                temp.write(printprice)
                temp.write('\n')
                temp.write('\n')

            elif avai == 0 :
                print('No Medicine Found')
        elif item.strip() == '':
            order = 1

    #Write price       
    temp.write('Total price : ')
    tprice1 = str(tprice)
    temp.write(tprice1)
    print()
    temp.seek(0)
    print(temp.read())


    while True:
        pay = float(input('Enter amount you are paying :'))
        if pay - tprice < 0:
            print('Insufficient amount. Please retry: ')
        elif pay-tprice >= 0 :
            print("Thank you for ur purchase! Here's your balance : RM,",pay-tprice)
            temp.write('\nAmount paid : ')
            temp.write(str(pay))
            temp.write('\nBalance : ')
            temp.write(str(pay-tprice))
            temp.write('\n---------------\n')
            break

    #Record everything into Order history
    temp.seek(0)
    history = open('order.txt','a+')
    for line in temp:
        history.write(line)


    temp.close()
    account.close()
    history.close()
    R_cust_menu()
    
def r_cust_record():
    order = open('order.txt','r')
    name = open('account.txt','r')
    order.seek(0)
    account1= name.read()

    print()
    print('---------------')
    
    count = 0
    for line in order:
        if count == 0:
            if line.strip('\n') == account1 :
                print(line)
                count = 1
            else :
                continue
            
            
        elif count == 1:
            if line.strip('\n') != '---------------':
                print(line)
                
            elif line.strip('\n') == '---------------':
                print(line)
                count = 0
            else :
                print('no')
        else:
            print('no')

    order.close()
    name.close()
    R_cust_menu()

    
def r_cust_info():
    name = open('account.txt','r')
    member = open('member.txt','r')
    
    account = name.read()

    count = 0
    print()
    for line in member:
        if count == 0:
            if line.strip('\n') == account :
                print(line.strip())
                count = 1
            else :
                continue
        elif count == 1:
            if line != '\n':
                print(line.strip())
            elif line == '\n':
                print(line)
                count = 0
        else:
            continue
        
    name.close()
    member.close()
    R_cust_menu()

menu()

