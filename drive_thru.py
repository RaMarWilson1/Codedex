welcome = input("Welcome to the Drive thru can i take your order")
print('please type done when finished with your order')

def full_order(welcome):
    while welcome != "done" :
        completed_order = []
        order = int(welcome)
        if order == 1:
            completed_order.append('🍔 Cheeseburger')
        elif order == 2:
            completed_order.append('🍟 Fries')
        elif order == 3:
            completed_order.append('🥤 Soda')
        elif order == 4:
            completed_order.append('🍦 Ice Cream')
        elif order == 5:
            completed_order.append('🍪 Cookie')
    return "Thank you here is your full order" + completed_order

