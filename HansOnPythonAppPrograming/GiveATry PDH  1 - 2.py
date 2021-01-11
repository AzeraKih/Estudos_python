import io
import re

##fileWaifus = open('Waifus.txt')
##
##Waifus = fileWaifus.readlines()
##
##fileWaifus.close()
##Waifus = [w.strip('\n') for w in Waifus]
##Waifus = [w.split(';') for w in Waifus]
##header = Waifus.pop(0)
##Waifus = [dict(zip(header, w)) for w in Waifus]
##
##
##mStr = ""
##for Waifu in Waifus:
##    mStr += Waifu["Nome"] + '''{
##\t Nome: ''' + Waifu["Nome"] + ''':,
##\t idade: ''' + Waifu["idade"] + ''',
##\t anime: ''' + Waifu["anime"] + ''',
##\t cor do cabelo: ''' + Waifu["cor do cabelo"] + ''',
##\t altura: ''' + Waifu["altura"] + "\n\t},\n"
##
##
##mStr = mStr[:len(mStr)-2]
##fileWaifus = open('sWaifus.txt', 'w+')
##fileWaifus.write(mStr)
##fileWaifus.close()


##zenPython = '''
##The Zen of Python, by Tim Peters    
##Beautiful is better than ugly.
##Explicit is better than implicit.
##Simple is better than complex.
##Complex is better than complicated.
##Flat is better than nested.
##Sparse is better than dense.
##Readability counts.
##Special cases aren't special enough to break the rules.
##Although practicality beats purity.
##Errors should never pass silently.
##Unless explicitly silenced.
##In the face of ambiguity, refuse the temptation to guess.
##There should be one-- and preferably only one --obvious way to do it.
##Although that way may not be obvious at first unless you're Dutch.
##Now is better than never.
##Although never is often better than *right* now.
##If the implementation is hard to explain, it's a bad idea.
##If the implementation is easy to explain, it may be a good idea.
##Namespaces are one honking great idea -- let's do more of those!
##'''
##
##fp = io.StringIO(zenPython)
##zenlines = fp.readlines()
##zenlines = [z.strip("\n ") for z in zenlines]
##
##zenlines = [re.findall(r'\*.+\*|\-.+\-',z) for z in zenlines ]
##zenlines = [z[0].strip("*") for z in zenlines if z]
##zenlines = [z.strip("-") for z in zenlines if z]
##zenlines = [z.strip(" ") for z in zenlines if z]
##
##
##print(zenlines)


#!/bin/python3

#!/bin/python3

##import sys
##import os
##import io
##import re
##
##
### Complete the function below.
##def subst(pattern, replace_str, string):
##    return re.sub(pattern, replace_str, string)
##
##
##def main():
##    addr = ['100 NORTH MAIN ROAD',
##            '100 BROAD ROAD APT.',
##            'SAROJINI DEVI ROAD',
##            'BROAD AVENUE ROAD']
##    new_address = [subst("(^ROAD)|(ROAD$)", "RD.", a) for a in addr]
##    new_address = [subst("( ROAD )", " RD. ", a) for a in new_address]
##    
##
##    return new_address
##
##'''For testing the code, no input is required'''
##
##if __name__ == "__main__":
