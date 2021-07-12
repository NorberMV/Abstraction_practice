
# Model a Restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = str(restaurant_name)
        self.cuisine_type = cuisine_type
        
    def open_restaurant(self):
        print('The restaurant {} is open!'.format(self.restaurant_name))
    
    def describe_restaurant(self):
        print('Restaurant Name: {};\nCuisine Type: {}'.format(self.restaurant_name, self.cuisine_type))

if __name__=='__main__':
    my_restaurant = Restaurant('Mundo Verde', 'Burger King')
    my_restaurant.open_restaurant()
    my_restaurant.describe_restaurant()
