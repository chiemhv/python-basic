#ham thao tac voi chuoi
data= "   Hoc lap trinh python that la don gian! YEAH YEAH!"
print("1."+data.strip()) #bo khoang trang 2 dau
print("2."+data.lower()) #chuyen het ve kieu chu thuong 
print("3."+data.upper()) #chuyen het ve kieu chu hoa
print(data.swapcase())   #chuyen chu hoa -> thuong + thuong -> hoa
print(data.find('lap'))  # tim vi tri cua chuoi "lap"
print(data.count('Y'))   # dem so thu tu cua tu Y 
print(len(data))		 # dem so ki tu cua chuoi