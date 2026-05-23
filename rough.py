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

#function
lst = [1,2,3]
print(len(lst))

from oops_proj import chatbook

#method
user1 = chatbook()
#user1.send_msg()

#print(user1.__confidential) This will throw error but
print(user1._chatbook__confidential) #this will work but it is not recommended to use hidden attributes outside the class
print(user1.get_name())
user1.set_name("I love MUJ")
print(user1.get_name())
print(user1.id)

chatbook.set_id(100)
user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)
