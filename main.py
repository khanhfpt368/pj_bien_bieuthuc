# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### --> Ham import <---
from math import *     # import ham toan tu


### Du Lieu Chuoi ###
## 1.--> Bai Tap Chuoi <---

Chuoi_test = '☯ a Monty Python Realy ☯'
print(Chuoi_test[:2])
print(Chuoi_test[8:])
print(Chuoi_test[:])
print(Chuoi_test[0:4])
print(Chuoi_test[6:7])
print(Chuoi_test[6:20])

## --> Bai Tap Method Chuoi <---

Chuoi_dauhoa = Chuoi_test.title() # dau chuoi hoa
print('Chuoi Title: ', Chuoi_dauhoa)
Chuoi_inhoa = Chuoi_test.upper() # toan bo chuoi in hoa
print('Chuoi Upper: ', Chuoi_inhoa)
Chuoi_thuong = Chuoi_test.lower() # toan bo chuoi thuong
print('Chuoi Lower: ', Chuoi_thuong)
Chuoi_botrangphai = Chuoi_test.rstrip() # chuoi bo trang phai
print('Chuoi bo khoang trang phai: ', Chuoi_botrangphai)
Chuoi_botrangtrai = Chuoi_test.lstrip() # chuoi bo trang trai
print('Chuoi bo khoang trang trai: ', Chuoi_botrangtrai)
Chuoi_botrang2ben = Chuoi_test.strip() # chuoi bo trang 2 ben
print('Chuoi bo trang 2 ben: ', Chuoi_botrang2ben)
Chuoi_replace = Chuoi_test.replace('Monty', 'Super AI') # Chuoi thay the
print('Chuoi thay the moi: ', Chuoi_replace)
Vtri_chuoicantim = Chuoi_test.find('Re') # Tim vi tri chuoi can tim -> Lay vi tri ky tu dau tien i[0]
print('Vi tri chuoi can tim trong mang: ', Vtri_chuoicantim)
Vtri_tuchuoibatdau = Chuoi_test.find('ty', 3) # Tim vi tri chuoi can tim tu vi tri i[3] -> i[vt] = i[3]++
print('Vi tri chuoi can tim tu vtri chuoi bat dau: ', Vtri_tuchuoibatdau)
Chuoi_a, Chuoi_b = 'DUOLING GO', 'Fpt'

Test_hoa = Chuoi_a.isupper() # check chuoi toan in hoa tra ve True/False
print('KQ check chuoi hoa: ', Test_hoa)
Test_thuong = Chuoi_b.islower() # check chuoi toan thuong tra ve True/False
print('KQ check chuoi thuong: ', Test_thuong)
Ho, Ten_lot, Ten = 'Nguyen ', 'Thanh ', 'Long '
Ho_ten = Ho + Ten_lot + Ten # toan tu ghep chuoi '+'
print('Ho ten day du: ', Ho_ten)
Chuoi_c = 'Cat Catch Mouse & '
Chuoi_repeat = Chuoi_c * 5 # toan tu lap lai chuoi '*'
print('Chuoi lap lai: ', Chuoi_repeat)
Chuoi_cantim = input('Nhap chuoi: ')
Check_chuoicon = Chuoi_cantim in Chuoi_test # Check chuoi con trong chuoi lon hon
print('KQ check chuoi con: ', Check_chuoicon)
print(Chuoi_cantim + '\n'+ Chuoi_test) # Toan tu xuong dong
print(Chuoi_cantim + '\t'+ Chuoi_test)  # Toan tu xuong khoang cach

## --> Bai Tap Tim Va In Chuoi <---
## -> BT02: Cho chuoi: sonha@gmail.com; rut trich va in ra kqua gmail.com
Chuoi_d = 'sonha@gmail.com'
Vi_tri = Chuoi_d.find('@') # tim vi tri bat dau rut trich
print('Vi tri rut trich: ', Vi_tri)
Host = Chuoi_d[Vi_tri + 1:] # tim trong khoang rut trich den vi tri cuoi cung
print('--> Chuoi sau khi rut trich: ', Host)

## -> BT03: Cho chuoi: thanhcong@gmail.com  SAT  Jan  9:00AM ; rut trich va in ra kqua gmail.com
Chuoi_e = 'thanhcong@gmail.com  SAT  Jan  9:00AM'
Vtri_batdau = Chuoi_e.find('@') # tim vi tri bat dau rut trich
Vtri_ketthuc = Chuoi_e.find(' ', Vtri_batdau) # tim vi tri ket thuc rut trich
print('Vi tri ket thuc rut trich chuoi 2: ', Vtri_ketthuc)
Host2 = Chuoi_e[Vtri_batdau + 1: Vtri_ketthuc] # tim trong khoang rut trich den vi tri cuoi cung
print('--> Chuoi 2 sau khi rut trich:', Host2)

## -> BT04: Nhap 1 Chuoi bat ky, nhap tu Can Thay The, nhap tu Thay The va in ra kqua cuoi cung
st1 = input('Nhap chuoi bat ky: ')
st2 = input('Nhap tu can thay the: ')
st3 = input('Nhap tu thay the: ')
st1 = st1.replace(st2, st3)
print('--> Chuoi sau khi nhap va thay the: ', st1)

## -> BT05: Nhap 1 Chuoi bat ky, bieu dien chuoi 5 ky tu cuoi cung, 5 ky tu dau tien, 4 chuoi cung dong co khoang cach, 4 chuoi 4 dong va in ra kqua cuoi cung
St_bieudien = input('Nhap chuoi can bieu dien: ')
St_5cuoicung = St_bieudien[:5] + '\n'
St_5dautien = St_bieudien[len(St_bieudien) - 4:] + '\n'
St_4chuoi_khoangcach = 4 * (St_bieudien + '\t') + '\n'
St_4chuoi_xuongdong = 4 * (St_bieudien + '\n')

print('--> KQ cac chuoi duoc bieu dien nhu sau: \n', St_5cuoicung, St_5dautien, St_4chuoi_khoangcach, St_4chuoi_xuongdong)

## 2--> Bai Tap Method Chuoi <---

# Nhap cac so hang
a = float(input('Nhap so thu 1 = '))
print(a)
b = float(input('Nhap so thu 2 ='))
print(b)


# ham phep tinh (luu y thut le phan biet ham def sau ket thuc lenh return)
def Phep_tinh(a, b):
    Tong = a + b    # phep cong
    Hieu = a - b    # phep tru
    Tich = a * b    # phep nhan
    if b != 0:
        Thuong = a / b  # phep chia
    else:
        Thuong = '---> Ko tim duoc Thuong '
    Luythua = a ** b # luy thua
    Canbac2 = float(sqrt(Tich))
    Trituyetdoi = float(abs(Hieu))

    return Tong, Hieu, Tich, Thuong, Luythua, Canbac2, Trituyetdoi


# Goi ham phep tinh
Tong, Hieu, Tich, Thuong, Luythua, Canbac2, Trituyetdoi = Phep_tinh(a, b)

# In ra ket qua
print('Tong = ', Tong)
print('Hieu = ', Hieu)
print('Tich =', Tich)
print('Thuong =', Thuong)
print('KQ Luy thua =', a, '^', b, '= ', Luythua)
print('Can bac 2 cua Tich =', Canbac2)
print('Tri tuyet doi cua Thuong =', Trituyetdoi)


