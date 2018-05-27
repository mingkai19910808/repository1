# encoding: utf-8
print('111');

arr = ["b","c","d","a"];
print(arr);

print (sorted(arr));

arr.sort(reverse=True);
print (arr);

arr.append("e");
print (arr);

arr.insert(0,"f");
print (arr);

print (arr[-1]);

str = "mingkai";
print (str.title());

for str in arr:
    print (str);
print (str+"1");

for val in range(1,5):
    print (val);

for val in range(2,11,2):
    print (val);

numbers = list(range(1,5));
print (numbers);

# **表示乘方
squares = []
for value in range(1,11):
 square = value**2;
 squares.append(square)
 print(squares)

print (min(squares))
print (max(squares))
print (sum(squares))

squares = [value**2 for value in range(1,11)]
print(squares)

print(squares[0:3])

print(squares[:4])

print(squares[2:])

print(squares[-3:])

for player in squares[:3]:
    print(player)

#复制列表
squares_bak = squares[:]
print(squares_bak)

squares2 = [[1,2],[4,5]]
for v1 in squares2:
   for v2 in v1:
       print(v2)

#元组，不可变的列表被称为元组，修改的值称为不可变的
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#可以重新给存储元组的变量赋值
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw' or car == 'audi':
    print(car.upper())
  elif car.lower() == 'subaru' and car == 'subaru':
    print(car.upper())
  else:
    print(car.title())

if 'bmw' in cars:
 print(True)
if 'dazhong' not in cars:
 print(True)

if cars:
    print(True)

