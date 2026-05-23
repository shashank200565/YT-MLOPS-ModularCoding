lst = [1,2,3]
my_str = 'MLOps is fun'
my_int = 42

print(type(lst))
print(type(my_str))
print(type(my_int))

#as you can see list string and integer are all classes in python and these classes have few methods
lst2 = lst.clear()
print(lst2)

#you can't use methods of one class into another...basically u cant do lst.lower()

my_str1 = my_str.lower()
print(my_str1)