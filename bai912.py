# ham 

def hello():
	print("xin chao")
print("tao ham")
hello()

# them tham so 
def hello2(name):
	print("xin chao"+ name +"!")
# goi 
hello2("kim")

#vd2 
def tong(ds):
	tong =0
	for i in ds:
		tong +=i
		return tong
# goi ham tong
ket_qua = tong([1, 2, 4])
	print ket_qua