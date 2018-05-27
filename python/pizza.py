def make_pizza(size,*toppings):
 print(toppings)
 print("\nMaking a pizza with the following toppings:")
 for topping in toppings:
    print(str(size)+"- " + topping)