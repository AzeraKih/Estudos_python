'''Consider the string 's' having the value 'tata consultancy services limited'

Determine the no. of vowels present in it, using for loop. Store the number in variable 'count' and print it.
'''

s='tata consultancy services limited'
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print(count)
