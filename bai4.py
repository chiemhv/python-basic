#kieu du lieu list - dac diêm, gia tri co the thay doi duoc 
# 1 list trong python co nhieu du lieu khac nhau
data = [0, 1, 3]
# hien thi ra 
data
# dem so phan tu 
len(data)
# truy xuat phan tu vi tri 1 
data[1]
# thanh doi gia tri
data[1] = 10 
# them phan tu vao data, vi tri cuoi
data.append(2015)
data
# insert phan tu 
data.insert(2, 177) # truoc phan tu 2
data
# xoa phan tu su dung ham del , trong python ham 1 tham so ko can dau ()
del data[3]
data
#xoa phan tu cuoi cung 
data.pop()
#xoa dung ham remove 
data.remove(10) # truyen vao gia tri, no xoa phan tu dau tien tim thay 
# LAP LAI kieu list 
data * 3

# TOAN TU CONG list 
another = ['one', 'two', 'three']
data + anothe 

# TOAN TU THEM list vao list 
data.extend(another)

# DANH SACH LONG TRONG DANH SACH 
data = [another, 0, 2, 'something'] # another la kieu danh sach 

# truy xua danh sach trong kieu danh sach 
data[0][1]

# HAM DAO VI TRI CAC PHAN TU TRONG list
data.reverse()
 # HAM SAP XEP 
data.sort()





