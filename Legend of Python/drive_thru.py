def Welcome():
    print("Welcome to the Drive thru")
    print('1:🍔 Cheeseburger\n' 
    '2:🍟 Fries \n' 
    '3:🥤 Soda \n' 
    '4:🍦 Ice Cream \n'
    '5:🍪 Cookie' )
    print('please type "done" when finished with your order')




def full_order(orders):
    completed_order = []
    
    while orders != "done" :
        
        if orders == "1":
            completed_order.append('🍔 Cheeseburger')
        elif orders == "2":
            completed_order.append('🍟 Fries')
        elif orders == "3":
            completed_order.append('🥤 Soda')
        elif orders == "4":
            completed_order.append('🍦 Ice Cream')
        elif orders == "5":
            completed_order.append('🍪 Cookie')
        else:
            print("please enter a number 1-5")
        orders = input("Anything else? ")           
    
    print("Thank you here is your full order" + str(completed_order))

Welcome()
print()
orders = input(" Can I take your order please")
print()
full_order(orders)
