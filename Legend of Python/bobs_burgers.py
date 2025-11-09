class Restaurant:
    name = ''
    category = '' 
    rating = 0.0
    delivery = False


bobs_burgers= Restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False


mcdonald = Restaurant()
mcdonald.name = 'McDonald\'s'
mcdonald.category = 'Fast Food'
mcdonald.rating = 3.0
mcdonald.delivery = True 


Bertuccis = Restaurant()
Bertuccis.name = 'Bertucci\'s'
Bertuccis.category = 'Italian'
Bertuccis.rating = 5.0
Bertuccis.delivery = False


print(vars(Bertuccis))
print(vars(bobs_burgers))
print(vars(mcdonald))
