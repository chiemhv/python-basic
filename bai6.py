data = {
		'website' : "trang web",
		'world' : "the gioi",
		'programming' : "laptrinh",
		'study' : "hoc tap, nghien cuu",
		'work' : "lam viec"
	}
#truy xuat
data['website']
# check khoa website 
data.has_key('website')
# 
data.keys()
#
data.values()

# thay doi value of key 
data['website'] = "mot trang web"
# lay ra gia tri
data['website']
data.get('website')
# xoa 1 khoá
del data['website']
# them 1 khoa 
data['singer']= "haogiwg"
# tra ve 1 cap khoa
data.items()
# tra ve cap key-value so 0
data.items()[0]
# tra ve
data.items()[0][0]
# rieng vơi kieu du lieu dict thì pop phai truyen vao bien
data.pop('work')

# xoá cả data 
del data




















