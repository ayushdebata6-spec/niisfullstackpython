#swapping 2 numbers using 3rd variable
a=10
b=20
print("before swapping a=",a,"b=",b)
t=a
a=b
b=t
print("after swapping a=",a,"b=",b)



#swapping 2 numbers without 3rd variable
a=10
b=20
print("before swapping a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("after swapping a=",a,"b=",b)



#swapping 2 variables in 1 line
a=10
b=20
a,b=b,a
print(a,b)


#swapping 3 numbn3rs l to r using 4th v ariable
a=10
b=20
c=30
print("before swapping a=",a,"b=",b,"c=",c)
t=c
c=b
b=a
a=t
a,b,c=c,b,a