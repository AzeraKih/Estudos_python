a = set(('10','20','30','40'))

b = set(('30','60'))

u=a.union(b)
print(u)

i=a.intersection(b)
print(i)

d=a-b
print(d)

sd=a.symmetric_difference(b)
print(sd)

'''
Create two sets 'a', and 'b' with following values.

a = ('10','20','30','40')

b = ('30','60')

Determine the following

Union; store the output in variable 'u' and print it.
Intersection; store the output in variable 'i' and print it.
Difference between set 'a' and 'b'; store the output in variable 'd' and print it.
Symmetric difference; store the output in variable 'sd' and print it.

'''
