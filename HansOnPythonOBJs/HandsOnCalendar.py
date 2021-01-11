##import os
##
##for root, dirs, files in os.walk(".", topdown=False):
##    for name in files:
##        if name.endswith(".py"):
##            print(os.path.join(root, name))

##import calendar
##
##c = calendar.TextCalendar()
##coolmonths = dict()
##for mes in range(1, 12):
##    aux = 0
##    for i in c.itermonthdays2(2019, mes):
##        if(i[1] == calendar.SUNDAY and not i[0] == 0):
##            aux += 1
##    if (aux >= 5):
##        coolmonths[calendar.month_name[mes]] = aux
##print(coolmonths)
