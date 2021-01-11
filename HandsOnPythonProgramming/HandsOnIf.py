'''Average score obtained by a student - 68.3

Write a script with if-elif-else blocks to determine the grade obtained by a student based on the total average obtained. Use the following criteria to determine the grade:

if total average >= 90, display "Distinct".
if in range [60, 90), display "Above average".
if in range [40, 60), display "Average".
else display "Fail"'''

tavg = 68.3
if(tavg >= 90):
    print("Distinct")
elif(tavg > 60 and tavg < 90):
    print("Above average")
elif(tavg > 40 and tavg < 60):
    print("Average")
else:
    print("Fail")
