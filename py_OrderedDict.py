#Python标准库
# 键—值对的添加顺序类OrderedDict，在将信息关联起来的同时保留原来的顺序
from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
 print(name.title() + "'s favorite language is " +
 language.title() + ".")

#随机数
from random import randint
x = randint(1, 6)
print(x)