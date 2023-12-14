
a=[2,3,1,0,3,1,1,1,3]
# akses item
print(a)
print(f'itemindeks-0 = {a[0]}')
print(f'itemindeks-3 = {a[3]}')
print(f'item indeks-Terakhir = {a[len(a)-1]}')
# akses item indeks negatif
print(f'itemindeks:terakhuir (-1) = {a[-1]}')
print(f'itemindeks:pertama  (-9) = {a[-len(a)]}')
print(f'itemindeks:terakhuir (-8) = {a[-8]}')
print(f'itemindeks:terakhuir (-4) = {a[-4]}')
# akses indeks batas
print(f'itemindeks :1,2,3 = {a[1:4]}')
print(f'itemindeks :1,2,... = {a[1:]}')
print(f'itemindeks :3,4,... = {a[3:]}')
print(f'itemindeks :0,1,2 = {a[:3]}')
print(f'itemindeks :0,1,2 = {a[:3]}')
print(f'itemindeks :0,1,2,3,4 = {a[:5]}')
print(f'itemindeks :Semua  = {a[:]}')
# pengirisan indeks
print(f'itemindeks :1,2,3 = {a[1:4]}')
print(f'itemindeks :2,3,4 = {a[2:5]}')
print(f'itemindeks :[1;8] = {a[1:-1]}')

print('\n')
# Nested List
kelas = [('Agama',2),
         ('Pancasila',2),
         ('Bahasa indonesia',2)]
print(f'Data Kelas {kelas}\n')

print('Tambahan kelas')
kelas.append(('Kalkulus',3))
print(f'Data Kelas {kelas}\n')

#tambah matkul 5 dan jumlah sks
print('Tambahan kelas')
kelas.append(('Cinta',3))
print(f'Data Kelas {kelas}\n')

      # Nama Mata kuliah 1: Matkul1 dengan jumlah sks:3
print(f'Nama Mata Kuliah 1: {kelas[0][0]} dengan jumlah sks :{kelas[0][1]}\n')
      # Nama Mata kuliah 2: Matkul2 dengan jumlah sks:2
print(f'Nama Mata Kuliah 2: {kelas[1][0]} dengan jumlah sks :{kelas[1][1]}\n')
      # Nama Mata kuliah 3: Matkul3 dengan jumlah sks:2
print(f'Nama Mata Kuliah 2: {kelas[2][0]} dengan jumlah sks :{kelas[2][1]}\n')
      # Nama Mata kuliah 4: Matkul4 dengan jumlah sks:3
print(f'Nama Mata Kuliah 2: {kelas[3][0]} dengan jumlah sks :{kelas[3][1]}\n')
      # Nama Mata kuliah 5: Matkul5 dengan jumlah sks:3
print(f'Nama Mata Kuliah 2: {kelas[4][0]} dengan jumlah sks :{kelas[4][1]}\n')

data = [('Dwicki Herlambang',2023,'Aktif'), 
        (90,89,93,97,100), 
        (20,22), 
        ('S1-Reguler','Sistem Informasi D','Ganjil')]

      #  Nama Mahasiswa:
print(f'Nama Mahasiswa: {data[0][0]}')
      #  NIM Dwicky Herlambang: 60020101
astr= str(a)
nim = astr.replace(',','').replace('[','').replace(']','').strip('')
print (f'NIM {data[0][0]} : {nim}')
      #  Program pendidikan Dwicky Herlambang: Sistem Informasi D S1-Reguler
print(f'program Pendidikan {data[0][0]} :{data[3][1::-1]}')
      #  Angkatan Dwicky Herlambang: 2023-Ganjil
print(f'Angkatan {data[0][0]} :{data[0][1]}-{data[3][-1]}')
      #  Jumlah nilai Dwicky Herlambang adalah: 5
nilaiSD= len(data[1])
print(f'Jumlah Nilai {data[0][0]} Adalah : {nilaiSD} ')
      #  Data terbesar Dwicky Herlambang adalah: 100
nilaiMax= max(data[1])
print(f'Data terbesar {data[0][0]} Adalah : {nilaiMax} ')
      #  Data terkecil Dwicky Herlambang adalah: 89
nilaiMin= min(data[1])
print(f'Data terkecil {data[0][0]} Adalah : {nilaiMin} ')
      #  Rata-rata nilai Dwicky Herlambang adalah: 92.25 
JumlahNilai= sum(data[1])
hasil = JumlahNilai / nilaiSD
print(f'Rata rata nilai {data[0][0]} Adalah : {hasil}')










