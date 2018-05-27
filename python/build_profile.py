#使用任意数量的关键字实参
def build_profile(first, last, **user_info):
 profile = {}
 profile['first_name'] = first
 profile['last_name'] = last
 for key, value in user_info.items():
  profile[key] = value
 return profile

#传递任意数量的实参，形参名*toppings 中的星号让Python创建一个名为toppings 的空元组
def make_pizza(size,*toppings):
 print(toppings)
 print("\nMaking a pizza with the following toppings:")
 for topping in toppings:
    print(str(size)+"- " + topping)

#make_pizza(5,'pepperoni')
#make_pizza(5,'mushrooms', 'green peppers', 'extra cheese')

#user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
#print(user_profile)