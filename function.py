# functions
def my_fuction():
    print("my name is jeeva")

my_fuction()

# arguments
def student(fname):
    print(fname,"student")


student("jeeva")
student("sanjay")
student("yogesh")
student("madhan")

# number of arguments
def gold(store_name,price):
    return(f"store:{store_name},prc={price}")

print(gold("sks",2500))
print(gold("jck",3000))

# Arbitary arguments
def school(*name):
    return (f"the kids name was:{name[0]}")

print(school("jeeva","sanjay"))

# keyvalue arguments
def school(child1,child2,child3):
    return (f"the kids name was:{child3}")

print(school(child1="jeeva",child3="sanjay",child2="dhanush"))

# Arbitrary  keyword argument
def school(**kids):
    return ("the kids name was:"+kids["fname"])

print(school(fname="jeeva",lname="sanjay"))

# default parameter value

def my_function(contry="norway"):
    return ("my country is:" +contry)

print(my_function("Sweden"))
print(my_function("india"))
print(my_function())
print(my_function("Brazil"))

# passing a list as an argument
def my_fuction(food):
    for x in food:
        print(x)

furits=["apple","banana","orange"]

my_fuction(furits)

def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)































