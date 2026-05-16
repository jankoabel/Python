temp = int(input("What is the forecast for tomorrow? "))
rain = input("Will it rain (yes/no)? ")
print("Wear jeans and a T-shirt")
if temp <= 20:
    print("I recommend a jumper as well")
if temp < 15:
    print("Take a jacket with you")
if temp < 10:
    print("Make it a warm coat, actually")
if temp <= 5:
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
