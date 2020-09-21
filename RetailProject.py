stock = dict()
listSales = [0]

#Function to add item to stock
def AddItem():
    k = 0
    print ("  ")
    no = int(input("How many items do you need to add?: "))
    while (k < no):
        name = str(input("Item Name: "))
        qtty = int(input("Quantity: "))
        price = int(input("Price per Unit: "))
        List2 = [qtty, price]
        stock[name] = List2
        k += 1

    print("Item added successfully")
    print(" ")

    rs = str(input("Do you need to return to the Admin Page (Y/N)?: "))
    if rs == 'Y':
        AdminPage()
    elif rs == 'N':
        AddItem()
                  
    return dict

#Function to change/update price of item(s)      
def ChangePrice():
    print ("________________________________________________________  ")
    print ("  ")
    item = str(input("Item Name: "))
    price = int(input("Enter New Price: "))
    List2 = stock[item]
    stock[item] = [int(List2[0]), price]
    print("Price updated successfully")

    print(" ")
    rs = str(input("Do you need to return to the Admin Page (Y/N)?: "))
    if rs == 'Y':
        AdminPage()
    elif rs == 'N':
        ChangePrice()
    return dict


#Function to get total gain per day
def GainPerDay():
    total = 0
    gain = 0
    total += sum(listSales)
    gain = 0.15*total
    print ("________________________________________________________  ")
    print ("  ")
    print("Total Sales for today is : ",total,"Naira")
    print(" ")
    print("Total Gain for today is : ",gain,"Naira")

    rs = str(input("           Press any key to go back to Admin Page: "))
    if rs == 'Y':
        AdminPage()
    else:
        AdminPage()
    return 

#Function to view lists of available items in stock
def ViewStock():
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("                 MR. ADAMU RETAIL MARKET")
    print("                      STOCK LIST")
    print("ITEMS              QUANTITY   UNIT PRICE")
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for key, value in stock.items():
        print(key, '                ',value)

    print(" ")
    print(" ")

    rs = str(input("Do you need to return to the Home Page (Y/N)?: "))
    if rs == 'Y':
        HomePage()
    elif rs == 'N':
        ViewStock()
    return 

#Function to compute goods purchased and generate receipt
def Purchase():
    totalPrice = 0
    grandTotal = 0
    j = 0
    vat = 0
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    custname = str(input("Customer Name: "))
    n = int(input("How many item(s) do you need to purchase?: "))
    
    while (j < n):
        try:
            item = str(input("Item Name: "))
            List = stock[item] 
        except:
            print("Item not available, Please Retry")

        x = List[0]
        y = List[1]

        try:
            qtty = int(input("Unit/Quantity: "))
            if qtty <= x :
                x -= qtty
        except:
            print("Quantity not available, try lower quantity") 
        
        totalPrice = qtty*y
            
        grandTotal +=totalPrice
        j+= 1
        
    if n < 5 :
        vat = grandTotal*0.2
        grandTotal += vat
    elif n > 10:
        vat = grandTotal*0.3
        grandTotal += vat
    elif n>10 and totalPrice >= 100 :
        grandTotal -= 800
    
    listSales.append(grandTotal)


    print ('    ')
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ('                 MR ADAMU RETAIL MARKET')
    print ('                 SALES RECEIPT/INVOICE') 
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ('Customer Name:  ',custname)
    print ('Item Purchased: ' ,item)
    print ('Units:          ',qtty, '\nTotal (VAT Inclusive):          ',grandTotal,'Naira')
    print ('                     Thank you for your patronage, Good bye')
    stock[item] = [x, y] #update stock

    print ("  ")
    rs = str(input("Do you need to return to Customer Page (Y/N)?: "))
    if rs == 'Y':
        CustomerPage()
    elif rs == 'N':
        Purchase()
    return

#Function to add item to stock
def AddItem1(name, qtty, price):
        List2 = [qtty, price]
        stock[name] = List2
        return dict

def HomePage():
    print (" ")
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ("              WELCOME TO MR. ADAMU RETAIL MARKET")
    print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print ("  ")
    print ("                   Automated Inventory System ")
    print ("  ")
    print ("1 .....  CUSTOMER")
    print ("  ")
    print ("2 .....  ADMIN")
    print ("  ")
    print ("3 .....  EXIT")
    print ("  ")
    ans = int(input("                      Select your identity (1-3): "))
    try:
        if ans == 1:
            CustomerPage()
        elif ans == 2:
            AdminPage()
        elif ans == 3:
            exit
    except:
        print ("  ")
        print ("Please, enter a valid choice between 1 to 3")
        CustomerPage()

    return

def CustomerPage():
    print ("____________________________________________________________  ")
    print ("  ")
    print ("                     MR. ADAMU RETAIL MARKET")
    print ("  ")
    print ("                      Self Customer Service ")
    print ("  ")
    print ("1 .....    VIEW AVAILABLE ITEMS")
    print ("  ")
    print ("2 .....    PURCHASE ITEM(S)")
    print ("  ")
    print ("3 .....    Back to Home Page? ")
    print ("  ")
    ans = int(input("                      Select your choice(1-3): "))
    try:
        if ans == 1:
            ViewStock()
        elif ans == 2:
            Purchase()
        elif ans == 3:
            HomePage()
    except:
        print ("  ")
        print ("Please, enter a valid choice between 1 to 3")
        CustomerPage()
    return

def AdminPage():
    print ("____________________________________________________________  ")
    print ("  ")
    print ("              WELCOME TO MR. ADAMU ADMIN PAGE")
    print ("  ")
    print ("1 .....    ADD ITEM TO STOCK")
    print ("  ")
    print ("2 .....    CHANGE PRICE OF ITEM(S)")
    print ("  ")
    print ("3 .....    VIEW STOCK")
    print ("  ")
    print ("4 .....    VIEW TOTAL GAIN PER DAY")
    print ("  ")
    print ("5 .....    Return to Home Page")
    print ("  ")
    ans = int(input("                             Select your choice(1-5): "))
    try:
        if ans == 1:
            AddItem()
        elif ans == 2:
            ChangePrice()
        elif ans == 3:
            ViewStock()
        elif ans == 4:
            GainPerDay()
        elif ans == 5:
            HomePage()
    except:
        print ("  ")
        print ("Please, enter a valid choice between 1 to 5")
        AdminPage()

    return


                    
AddItem1('Sugar', 131, 50)
AddItem1('Bread(sliced)', 311, 200)
AddItem1('Bread(unsliced)', 229, 150)
AddItem1('Egg', 545, 50)
AddItem1('Three crown(tin)', 201, 150)
AddItem1('Peak milk(tin)',230, 120)
AddItem1('Peak milk(sachet)', 791, 50)
AddItem1('Bournvita(sachet)', 611, 50)
AddItem1('Milo(tin)', 367, 500)
AddItem1('Peak milk(large sachet)', 889, 700)
AddItem1('Milo(large sachet)', 934, 700)
AddItem1('Bournvita(large sachet)', 758, 100)
AddItem1('Custard (small sachet)', 383, 200)
AddItem1('Corn flakes(small sachet)', 647, 150)
AddItem1('Golden morn(small sachet)', 121, 100)
AddItem1('Detergent(small wawu)', 198, 120)
AddItem1('Detergent(small aerial)', 354, 116)
AddItem1('Detergent(big wawu)', 323, 200)
AddItem1('Detergent(big aerial)', 222, 250)
AddItem1('Corn flakes(big sachet)', 341, 750)
AddItem1('Golden morn(large sachet)', 458, 650)
AddItem1('Sprite(small)', 134, 80)
AddItem1('Pepsi (small)', 674, 80)
AddItem1('Fanta (small)', 757, 80)
AddItem1('Lacasera (small)', 127, 80)
AddItem1('Sprite (big)', 956, 150)
AddItem1('Pepsi (big)', 374, 150)
AddItem1('Fanta (big)', 267, 150)
AddItem1('Lacasera (big)', 786, 150)
AddItem1('Coke (big)', 546, 150)


HomePage()



