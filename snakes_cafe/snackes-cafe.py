print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
>
""")

newcount=0
newlist = []
newinput=''
while newinput != 'quit' :
    
    newinput = input('> ')
    newlist.append(newinput)
    newcount= newcount+1
    if newinput == 'quit':
       break
    print(f'** { newlist.count(newinput)} orders of {newinput } have been added to your meal **')
   


