#!/usr/bin/python
import cPickle as p
shoplistfile ='shoplist.data'
shoplist = ['apple','mango','carrot']
f = file(shoplistfile,mode='w')
p.dump(shoplist,f)
f.close()
del shoplist
f = file(shoplistfile)
storedlist = p.load(f)
print storedliste