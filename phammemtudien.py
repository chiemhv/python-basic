# tao pham mem tu dien 
database = {
	'home': 'ngoi nha',
	'baby': 'em be',
	'sex': 'tinh duc',
	'girl': 'con gai'
}
def show_menu():
	print("-------------------")
	print("CHUONG TRINH TU DIEN")
	print("1. them tu")
	print("2. tim tu")
	print("3. xoa tu")
	print("4. xem all")
	print("an 0 de thoat chuong trinh")
	print("-------------")
# hien thi 
show_menu()
# ham them tu 
def add():
	word = input("tu moi:")
	mean = input("nghia cua tu: ")
	database[word] = mean
	print("+ tu moi da duoc them")
def find():
	print("+ tim tu")
def delete():
	print("+ xoa tu")
def view_all():
	print("will")
# main 
choice = int(input("ban muon lam gi: "))
while choice !=0:
	if choice ==0:
		break
	elif choice ==1:
		add()
 	elif choice ==2:
 		find()
 	elif choice ==3:
 		delete()
 	elif choice ==4:
 		view_all()
 	else:
 		print("khong co lua chon nay")
 		choice = input("ban muon lam gi: ")
print("hen gap lai")










