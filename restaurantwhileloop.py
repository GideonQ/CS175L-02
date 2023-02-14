#CS175L
#GideonQuaye
#restaurantWhileLoop

keep_going = 'y'
while keep_going == 'y' and keep_going != 'no':
    vegetarian=False
    vegan=False
    glutenFree=False
    response=str(input('Is anyone in your party vegetarian?  '))
    if response.lower()=='yes':
        vegetarian=True
    response=str(input('Is anyone in your party vegan?  '))
    if response.lower()=='yes':
        vegan=True
    response=str(input('Is anyone in your party gluten-free?  '))
    if response.lower()=='yes':
        glutenFree=True
    print('\nHere are your restaurant choices.')
    print('Corner Café')
    print('The Chef\'s Kitchen')
    if not vegetarian and not vegan and not glutenFree:
        print('Joe\'s Gourment Burgers')
    if not vegan:
        print('Main Street Pizza Company')
    if not vegan and not glutenFree:
        print('Mama\'s Fine Italian')
    keep_going=input("Enter 'y' if you would like to do another restaurant search (enter 'no' to end): ")

    

