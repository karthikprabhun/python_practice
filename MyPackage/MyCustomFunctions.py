from enum import Enum

class Weather(Enum):
     hot = 1
     cold = 2
     rainy = 3

def callYuki():
     print("Dailing to Yuki...")

def giveBathToYuki(sampoo_name, personToHelp, weather: Weather):
     print("Welcome to the toughest task in the world...!")
     print(personToHelp, "will support to give yuki bath ! ")
     if weather == Weather.cold:
          print("Given bath using ",sampoo_name," with hot water")
     elif weather == Weather.hot:
          print("Given bath using ",sampoo_name," with cold water")
     else :
          print("No bath given")

def giveFood(day, food_type):
     if food_type.lower() == "veg":
          print(f"On {day}, Yuki gets vegetarian food.")
     elif food_type.lower() == "non veg":
          print(f"On {day}, Yuki gets non-vegetarian food.")
     else:
          print(f"On {day}, food type not recognized.")

          
     
     
     