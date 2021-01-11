##Consider the string 's' with value "INfinity". Perform the following tasks, and print their respective output in separate lines.
##
##Check if 's' has alphabets only.
##Check if 's' has digits only.
##Determine the length of 's'.
##Convert all characters of 's' into upper case.
##Convert all characters of 's' into lower case.
##Find how many 'i' s are there in 's'.
##Find the index position of character 't' in 's'.

##Hint: Use string methods isalpha, isdigit, len, lower, upper, count, index.

s = "INfinity"

print(s.isalpha())
print(s.isdigit())
print(len(s))
print(s.lower())
print(s.upper())
print(s.count('i'))
print(s.index('t'))
