print "[ chuong trinh kiem tra so chan le]"
number = input("NHAP VAO SO NGUYEN : ")
if not number % 2:
	print "so {} ban nhap la chan".format(number)
else:
	print "so {} ban nhap la so le".format(number)