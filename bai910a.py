data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in data:
	if i % 2:
		continue 
	else:
		print(i)
print "----"
x = 0
while x <10:
	x +=1
	if x % 3 ==0: continue
	if x == 5: break
	print x