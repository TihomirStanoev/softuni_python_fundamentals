# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l

budget = float(input()) # 20.50
flour_price = float(input()) #1.25

egg_price = flour_price * .75 #0.9375
milk_price = (flour_price * 1.25)/4 #0.390625

bread_price = egg_price + flour_price + milk_price
total_breads = budget//bread_price
money_left = ((budget / bread_price) - total_breads) * bread_price

egg_counter = 0
bread_counter = 0
egg_subtract = 0
for bread in range(0, int(total_breads)):
    egg_counter += 3
    bread_counter += 1
    if bread_counter % 3 == 0:
        egg_subtract = bread_counter - 2
        egg_counter -= egg_subtract



print(f"You made {bread_counter:.0f} loaves of Easter bread! Now you have {egg_counter} eggs and {money_left:.2f}BGN left.")
