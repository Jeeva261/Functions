x=lambda a:a
print(x(3))


sum=lambda a,b:a+b
print(sum(2,7))

mulit=lambda a,b,c,d:a*b*c*d
print(mulit(1,2,3,4))


def my_function(n):
    return lambda a:a*n

multi=my_function(10)
alty=my_function(2)
print(multi(3))
print(alty(4))


square=lambda a:a**2
print(square(5))

multiply=lambda a,b:a*b
print(multiply(3,6))

def play(m):
    return lambda a:a*m

plays=play(9*5)
print(plays(7))

my_list=[1,2,3,4,5,6,7,8,9,10]

odd_number=list(filter(lambda a: a%2!=0,my_list))
even_number=list(filter(lambda a:a%2==0,my_list))
print(odd_number)
print(even_number)

my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda a:a**2,my_list))
print(new_list)

my_tuple=(1,2,3,4,5)
new_tuple=tuple(filter(lambda a: a%2==0,my_tuple))
print(new_tuple)

my_list=["jeeva","sanjay","yogesh","madhan"]
new_list=sorted(my_list,key=lambda a:a[1])
print(new_list)

from functools import reduce

my_list = [1, 2, 3, 4]
product = reduce((lambda x, y: x * y), my_list)
print(product)