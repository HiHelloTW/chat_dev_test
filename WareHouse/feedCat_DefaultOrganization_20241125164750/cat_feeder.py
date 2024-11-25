from food_bowl import FoodBowl
class CatFeeder:
    def feed(self):
        food_bowl = FoodBowl()
        if food_bowl.is_filled:
            print("Feeding the cat...")
            # Add code to actually feed the cat here
            # For example, you can use a library like RPi.GPIO to control a physical cat feeder
        else:
            print("Food bowl is empty. Please fill it before feeding the cat.")