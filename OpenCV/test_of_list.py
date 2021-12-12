import collections 

l1 = [10, 20, 30, 40, 50]
l2 = [10, 20, 30, 50, 40, 70]
l3 = [20, 10, 30, 40, 50]

if collections.Counter(l1) == collections.Counter(l3):
	print ("Списки l1 и l3 одинаковые")
else:
	print ("Списки l1 и l3 неодинаковые")
