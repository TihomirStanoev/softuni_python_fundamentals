quantity_kg = [float(input())*1000 for x in range(4)]



quantity_food , quantity_hay, quantity_cover, guinea_weight = quantity_kg


month = range(1,31)
no_food = False

for day in month:


    quantity_food -= 300

    if day % 2 == 0:
        needed_hay = quantity_food * 0.05
        quantity_hay -= needed_hay

    if day % 3 == 0:
        needed_cover = guinea_weight * (1 / 3)
        quantity_cover -= needed_cover
        quantity_cover = round(quantity_cover,2)
    #print(quantity_food, quantity_hay, quantity_cover)
    
    if quantity_food <= 0 or quantity_hay <= 0 or quantity_cover <= 0:
        no_food = True
        break


quantity_food , quantity_hay, quantity_cover = round(quantity_food/1000,2), round(quantity_hay/1000,2), round(quantity_cover/1000,2)


if no_food:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_food:.2f}, Hay: {quantity_hay:.2f}, Cover: {quantity_cover:.2f}.')