'''Create an empty list 'emplist1' using list operation.
Print 'emplist1'
Append to empty list 'emplist1' created above with element 9.
Append another element 10 to 'emplist1'
Print 'emplist1'
Create an empty list 'emplist2' using [].
Print 'emplist2'
Extend the empty list 'emplist2' created above with elements 'a', 'b', 'c'.
Print 'emplist2'
Extract the last element of 'emplist2' and assign it to variable 'e'.
Print 'emplist2'
Print the variable 'e'.'''
emplist1=[]
print(emplist1)
emplist1.append(9)
emplist1.append(10)
print(emplist1)
emplist2=[]
print(emplist2)
emplist2.extend(['a', 'b', 'c'])
print(emplist2)
e=emplist2[2]
print(emplist2)
print(e)
