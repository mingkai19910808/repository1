# encoding: utf-8
#函数
def greet_user():
 print("Hello!")

greet_user()


def greet_user(username):
 print("Hello, " + username.title() + "!")
greet_user('jesse')


#关键字实参
def describe_pet(animal_type, pet_name):
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#形参默认值
def describe_pet(pet_name, animal_type='dog'):
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

#返回值
def get_formatted_name(first_name, last_name):
 full_name = first_name + ' ' + last_name
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
 if middle_name:
  full_name = first_name + ' ' + middle_name + ' ' + last_name
 else:
  full_name = first_name + ' ' + last_name
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#传递列表
def greet_users(names):
 for name in names:
  msg = "Hello, " + name.title() + "!"
  print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#函数修改列表
def print_models(unprinted_designs, completed_models):
 while unprinted_designs:
  current_design = unprinted_designs.pop()
  print("Printing model: " + current_design)
  completed_models.append(current_design)

def show_completed_models(completed_models):
 print("\nThe following models have been printed:")
 for completed_model in completed_models:
  print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#禁止函数修改列表
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#导入函数
import build_profile as b
#导入模块中的所有函数
#from module_name import *
# from build_profile import *

#from module_name import function_0, function_1, function_2
user_profile =  b.build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)

#使用as 给函数指定别名
from build_profile import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

