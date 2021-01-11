
zenPython = "The Zen of Python, by Tim Peters\nBeautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\nFlat is better than nested.\nSparse is better than dense.\nReadability counts.\nSpecial cases aren't special enough to break the rules.\nAlthough practicality beats purity.\nErrors should never pass silently.\nUnless explicitly silenced.\nIn the face of ambiguity, refuse the temptation to guess.\nThere should be one-- and preferably only one --obvious way to do it.\nAlthough that way may not be obvious at first unless you're Dutch.\nNow is better than never.\nAlthough never is often better than *right* now.\nIf the implementation is hard to explain, it's a bad idea.\nIf the implementation is easy to explain, it may be a good idea.\nNamespaces are one honking great idea -- let's do more of those!"

#print(zenPython)

listPython = zenPython.replace("\n", " ").split(" ")
#print(listPython)

#listStrip = [word.strip(',.-*! ') for word in listPython]
#print(listStrip)

#listLower = [word.lower() for word in listPython]
#print(listLower)
#uniquew = []
#uniquew.append(listPython[0])

#for a in listPython:
#    if not a in uniquew:
#         uniquew.append(a);
#print(uniquew)

#dic = dict()
#for word in listPython:
#    if(not dic.get(word) and listPython.count(word) >= 5):
#        dic[word] = listPython.count(word)
#print(dic)

#def fibonacci(n):
#    num = 0
#    numa = 1
#    yield num
#    for i in range(n):
#        numa, num = num, num + numa
#        yield num

#gen = fibonacci(5)
#for i in range(5):
#    print(next(gen))
       
#def fatorial():
#    num = 1
#    aux = 1
#    while(True):
#        aux = 1
#        for j in range(1, num):
#            aux = j * aux
#        yield aux
#        num += 1        
        
#gen = fatorial()
#for i in range(1000):
#    print(next(gen))

    
