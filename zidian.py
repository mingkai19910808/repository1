# encoding: utf-8
#字典，相等于对象Object
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#删除键值对
del alien_0['points']
del alien_0['x_position']
del alien_0['y_position']
print(alien_0)

#遍历字典
for key1, value1 in alien_0.items():
 print("\nKey: " + key1)
 print("Value: " + value1)

#遍历所有键
for name in alien_0.keys():
     print(name.title())


favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

#遍历字典中的所有值
for language in favorite_languages.values():
 print(language.title())

print(favorite_languages.keys());

if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!")


#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
 print(name.title())

#嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

aliens = []
# 创建30个绿色的外星人
for alien_number in range(30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)
# 显示前五个外星人
for alien in aliens[:5]:
 print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# 在字典中存储列表
for topping in pizza['toppings']:
 print("\t" + topping)

#函数input
#message = input("Tell me something, and I will repeat it back to you: ")
#print(message)

intval = int('123')
print(intval)

#while
current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1

active = True
current_number = 1
while active:
 message = '循环'+str(current_number)
 if current_number > 5:
    active = False
 else:
  print(message)
 current_number += 1

#在列表之间移动元素
 unconfirmed_users = ['alice', 'brian', 'candace']
 confirmed_users = []
 # 验证每个用户，直到没有未验证用户为止
 # 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
   current_user = unconfirmed_users.pop() #获取列表删除的最后一个元素
   print("Verifying user: " + current_user.title())
   confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())

#删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
  pets.remove('cat')
print(pets)
