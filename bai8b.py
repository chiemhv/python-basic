# vd ve giai ptr b1
# ax + b = 0
print "[]"
a = input('nhap vao so a: ')
b = input('nhap vao so b: ')
if a == 0 and b ==0:
	print "ptr vo so nghiem"
elif a==0 and b !=0:
	print "ptr vo nghiem"
elif a!=0 and b==0:
	print "ptr co nghiem x la {}".format(a)
elif a!=0 and b!=0:
	print "ptr co nghiem la : %.2f " % (-b * 1.0/a)  #
else: print "deo biet"
