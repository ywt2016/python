#!/usr/bin/python
ab = {'Swaroop'  : 'Swaroop@qq.com',
      'Larry'    : 'Larry@qq.com',
      'Matsumoto': 'Matsumoto@qq.com',
      'Spammer'  : 'Spammer@qq.com',
     }
print ("Swaroop's address is %s" % ab['Swaroop'])
ab['Guido'] = 'guido@qq.com'
del ab['Spammer']
print ('\nThere are %d contacts in the address-book\n' % len(ab))
for name,address in ab.items():
    print ('Contact %s at %s' % (name,address))
if 'Guido' in ab:
    print ("\nGuido's address is %s" %ab['Guido'])
