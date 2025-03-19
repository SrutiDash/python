# implicit and explicit type conversion

name = 'sruti'
age = 24
print(type(name))
print(type(age))



a=23
b=22.22
print(type(a))
print(type(b))
c=a+b
print(c) 
#python automatically typecasts two different data types e.g int and float
print(type(c))


# explicit typecasting
d = '23'
print(type(d))
e = 22.3
print(type(e))
d = int(d)
print("after conversion", type(d))
f=d+e
print(f)
print(type(f))

x = 22.9
y = int(x)

print(y)  # Output: 22
print(type(y))  # Output: <class 'int'>


