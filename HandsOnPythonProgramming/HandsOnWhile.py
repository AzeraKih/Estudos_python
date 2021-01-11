'''
Consider the string 's' having the value 'tata consultancy services limited'

Determine the no. of vowels present in it, using While loop. Store the number in variable 'count' and print it.
'''
s='tata consultancy services limited'
count = 0
vowels = set("aeiou")
i=len(s)-1
while i >= 0:
  if s[i]in vowels:
        count += 1
  i-=1
print(count)
