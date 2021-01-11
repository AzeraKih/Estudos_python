'''
Create an empty Dictionary, 'd1' using 'dict' function
print 'd1'
Create a Dictionary 'd2' with Key values p-play , t-talk in the same order
print 'd2'.
Add two new key values : v-vibe, d-docs in the same order
print 'd2'
Remove the key value pair, 'v' - vibe, from 'd2'
print 'd2'
'''
d1=dict()
print(d1)
d2=dict(p='play',t='talk')
print(d2)
d2['v']='vibe'
d2['d']='docs'
print(d2)
del(d2['v'])
print(d2)
