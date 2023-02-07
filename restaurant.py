#CS175L
#GideonQuaye
#restaurant
vegetarian = False
vegan = False
gluten_free = False
response=input('Is anyone in your party a vegetarian?: ')
if response == 'yes':
    vegetarian = True
response=input('Is anyone in your party a vegan?: ')
if response == 'yes':
    vegan = True
response=input('Is anyone in your party gluten free?: ')
if response == 'yes':
    gluten_free = True

print('Here are your restaurant choices: ')
if response != vegetarian and response != vegan and response != gluten_free:
    print('Joe\'s Gourmet Burgers')

if response != vegan and response != gluten_free:
    print('Mama\'s Fine Italian')

if response != vegan:
    print('Main Street Pizza')
    print('Corner Cafe')
    print('Chef\'s Kitchen')
    
