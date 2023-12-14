nama= 'DWICKI HERLAMBANG'
nim = '231031113'
prodi= 'Sistem Informasi D'
meet = 'Praktikum 3'
email= 'dwickyherlambambang4@gmail.com'
print()
print(len(nama))

sp=69
print('-'.center(sp,'-'))
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
paragraf ='Halo, selamat datang perkenalkan Nama saya {} dengan NIM {} dari Prodi {}. Ini adalah file {}.'
a = paragraf.format(nama,nim,prodi,meet)
print(a)

#---------5+++++++9------
x= int(input('Masukkan Nilai ----5+++++++9---- ='))
cek1 =x<5
cek2 =x>9
status= cek1 and cek2
print('Hasilnya adalah', status)

#++++++++++5-------9++++++++
x= int(input('Masukkan Nilai +++5-------9++++ ='))
cek1 =x<=5
cek2 =x>=9
status= cek1 or cek2
print('Hasilnya adalah', status)

#++++++++5-------9+++++++13------
x= int(input('Masukkan Nilai +++5-------9+++++++13---- ='))
cek1 =x<5
cek2 =x>9
cek3 =x<13
status= cek1 or cek2 and cek3
print('Hasilnya adalah', status)

#-------5+++++++9-------13+++++++16----
x= int(input('Masukkan Nilai ------5+++++++9-------13+++++++16---- ='))
cek1 =x>5
cek2 =x<9
cek3 =x>13
cek4=x<16
status= cek1 or cek2 or cek3 and cek4
print('Hasilnya adalah', status)
#+++++++5------9++++++13-----16+++++20-----
x= int(input('+++++++5------9++++++13-----16+++++20-------- ='))
cek1 =x<5
cek2 =x>9
cek3 =x<13
cek4 =x>16
cek5 =x<20
status= cek1 or cek2 and cek3 or cek4 and cek5
print('Hasilnya adalah', status)

print('\n\t Tugas Praktikum')
# tugas 1
# ----5++++9----13++++16----
x= int(input('----5++++9----13++++16---- ='))
cek1 =x>5
cek2 =x<9
cek3 =x>13
cek4 =x<16
status = (cek1 and cek2) or (cek3 and cek4)
print('Hasilnya adalah', status)
print()

# tugas 2
# ----5++++9----13++++16----
x= int(input('++++5----9++++13----16++++ ='))
cek1 =x<5
cek2 =x>9
cek3 =x<13
cek4 =x>16
status = (cek1 and cek2) or (cek3 and cek4)
print('Hasilnya adalah', status)
print()

# tugas 3
# ----5++++9----13++++16----20++++24----
x= int(input('----5++++9----13++++16----20++++24---- ='))
cek1 =x>5
cek2 =x<9
cek3 =x>13
cek4 =x<16
cek5 =x>20
cek6 =x<24
status = (cek1 and cek2) or (cek3 and cek4) or (cek5 and cek6)
print('Hasilnya adalah', status)
print()

# tugas 4
#++++5-----9++++13------16+++++20-----24
x = int(input('Masukkan nilai = ++++5-----9++++13------16+++++20-----24+++++='))
cek1 = x<5
cek2 = x>9
cek3 = x<13
cek4 = x>16
cek5 = x<20
cek6 = x>24
status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
print('hasilnya adalah',status)
