print()
print('\tpraktikum-2')
print()
print('Nama Lengkap  = Dwicki Herlambang')
print('NIM           = 231031113')
print('Prodi         = Sistem Informasi')
print('Angkatan 2023')
print()
print('\tOPERATOR LOGIKA')
print()
print('=========================IN AND =========================')
a=True
b=False
hasil=a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil=a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil=b and b
print('Nilai',b,'and',b,'adalah',hasil)
hasil=b and a
print('Nilai',b,'and',a,'adalah',hasil)
print('=========================IN OR =========================')
hasil=a or a
print('Nilai',a,'or',a,'adalah',hasil)
hasil=a or b
print('Nilai',a,'or adalah',hasil)
hasil=b or b
print('Nilai',b,'or',b,'adalah',hasil)
hasil=b or a
print('Nilai',b,'or',a,'adalah',hasil)
print('=========================IN NOT =========================')
hasil= not a
print('Nilai not',a,'adalah',hasil)
hasil= not b
print('Nilai not',b,'adalah',hasil)
print('=========================IN XOR =========================')
hasil=a ^ a
print('Nilai',a,'XOR',a,'adalah',hasil)
hasil=a ^ b
print('Nilai',a,'XOR adalah',hasil)
hasil=b ^ b
print('Nilai',b,'XOR',b,'adalah',hasil)
hasil=b ^ a
print('Nilai',b,'XOR',a,'adalah',hasil)
print('=========================IN NAND =========================')
hasil= not (a and a)
print('Nilai',a,'and',a,'adalah',hasil)
hasil= not (a and b)
print('Nilai',a,'and',b,'adalah',hasil)
hasil=not (b and b)
print('Nilai',b,'and',b,'adalah',hasil)
hasil=not (b and a)
print('Nilai',b,'and',a,'adalah',hasil)
print('=========================IN NOR =========================')
hasil=not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil=not (a or b)
print('Nilai',a,'nor adalah',hasil)
hasil=not (b or b)
print('Nilai',b,'nor',b,'adalah',hasil)
hasil=not (b or a)
print('Nilai',b,'nor',a,'adalah',hasil)
print('=========================IN NNOT =========================')
hasil= not (not a)
print('Nilai Nnot',a,'adalah',hasil)
hasil= not (not b)
print('Nilai Nnot',b,'adalah',hasil)
print('=========================IN NXOR =========================')
hasil=not (a ^ a)
print('Nilai',a,'NXOR',a,'adalah',hasil)
hasil=not (a ^ b)
print('Nilai',a,'NXOR adalah',hasil)
hasil=not (b ^ b)
print('Nilai',b,'NXOR',b,'adalah',hasil)
hasil=not (b ^ a)
print('Nilai',b,'NXOR',a,'adalah',hasil)
print()
print('\tOPERATOR IDENTITAS')
print()
print('=========================IS')
a=5
b=6
print('Nilai','Memiliki identitas',hex(id(a)))
print('Nilai','Memiliki identitas',hex(id(b)))
hasil= a is b
print('a is b =',hasil)
a=6
b=6
print('Nilai','Memiliki identitas',hex(id(a)))
print('Nilai','Memiliki identitas',hex(id(b)))
hasil= a is b
print('a is b =',hasil)
print('========================= IS NOT')
a=5
b=6
print('Nilai','Memiliki identitas',hex(id(a)))
print('Nilai','Memiliki identitas',hex(id(b)))
hasil= a is b
print('a is not b =',not hasil)
a=6
b=6
print('Nilai','Memiliki identitas',hex(id(a)))
print('Nilai','Memiliki identitas',hex(id(b)))
hasil= a is b
print('a is not b =',not hasil)
print()
print('\tOPERATOR MEMBERSHIP')
print()
print('=========================IN')
nama='Bachraruddin Jusuf Habibie'
test='rud'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='bach'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='ib'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='a'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='i'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='u'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='e'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='o'
cek=test in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))
print()
print('=========================NOT IN')
# Tugas Buat Nama Menjadi Nama Lengkap Masing2
print('\n\tTugas 1\nBuat nama lengkap(Not In)')
print('\nNama \t= Dwicki Herlambang\n')
nama='Dwicki Herlambang'
test='Dwi'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='iky'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='cki'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='bang'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='asep'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='Dwi'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='HERLAMBANG'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='DWICKI'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='a'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='i'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='u'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='e'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))

test='o'
cek=test not in nama
print(test,'Terdapat di',nama,'Adalah '+str(cek))
print()
data=['Institut',
      'Teknologi',
      'Bacharuddin',
      'Jusuf',
      'Habibie']
print()
print('Data adalah',data)
test1='Habibie'
test2='Parepare'
test3='Kampus'
test4='Institut'
print()
cek=test1 in data
print(test1,'Terdapat di data adalah',cek)
cek=test2 in data
print(test2,'Terdapat di data adalah',cek)
cek=test3 in data
print(test3,'Terdapat di data adalah',cek)
cek=test4 in data
print(test4,'Terdapat di data adalah',cek)
print()


print('=========================NOT IN')
# Tugas dengan cara yang sama buat operator untuk not in
print('\tTugas 2\nTugas yang sama untuk Operator Not in')
data=['Institut',
      'Teknologi',
      'Bacharuddin',
      'Jusuf',
      'Habibie']
print()
print('Data adalah',data)
test1='Habibie'
test2='Parepare'
test3='Kampus'
test4='Institut'
print()
cek=test1 not in data
print(test1,'Terdapat di data adalah',cek)
cek=test2 not in data
print(test2,'Terdapat di data adalah',cek)
cek=test3 not in data
print(test3,'Terdapat di data adalah',cek)
cek=test4 not in data
print(test4,'Terdapat di data adalah',cek)
print()

# INI OPERATOR BITWISE
a=23 #Tanggal Lahir
b=12 #Bulan Lahir
b +=80
print()
print('=========================AND')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------AND')
c= a & b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))
print()
print('=========================OR')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------OR')
c= a | b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator XOR c= a^n
print('\n\tTugas 3 XOR c= a^b\n')
print('=========================XOR')
print('Nilai',a,'Dalam biner           =',format(a,'08b'))
print('Nilai',b,'Dalam biner           =',format(b,'08b'))
print('-----------------------------------------------------XOR')
c= a ^ b
print('Nilai',a,'&',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT c= ~a
print('\n\tTugas 4 NOT c= ~a\n')
print('=========================NOT a')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------NOT a')
c= ~a
print('Nilai','~','\b',a,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT c= ~b
print('\n\tTugas 5 NOT c= ~b\n')
print('=========================NOT a')
print('Nilai',b,'Dalam biner         =',format(b,'08b'))
print('-----------------------------------------------------NOT a')
c= ~b
print('Nilai','~','\b',b,'Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator Geser Kanan, c= a>>2
print('\n\tTugas 6 Geser Kekanan c= a>> 2\n')
print('=========================>>')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('----------------------------------------------------->>')
c= a>>2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator Geser kiri , c= a<<2
print('\n\tTugas 7 Geser Kiri c= a<<2\n')
print('=========================<<')
print('Nilai',a,'Dalam biner         =',format(a,'08b'))
print('-----------------------------------------------------<<')
c= a<<2
print('Nilai',a,'>>','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT and, c= ~(a&b)
print('\n\tTugas 8 not and c=~(a & b)\n')
print('=========================not and')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------not and')
c=~(a&b)
print('Nilai','~(',a,'&',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator NOT or, c= ~(a|b)
print('\n\tTugas 9 not or c=~(a | b)\n')
print('=========================not OR')
print('Nilai',a,'Dalam biner                 =',format(a,'08b'))
print('Nilai',b,'Dalam biner                 =',format(b,'08b'))
print('-----------------------------------------------------OR')
c= ~(a|b)
print('Nilai','~(',a,'|',b,')','Dalam Biner Adalah',format(c,'08b'))

# Tugas Untuk Operator not xor, c = ~(a^b)
print('\n\tTugas 10 not xor c=~(a ^ b)\n')
print('=========================not XOR')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('Nilai',b,'Dalam biner                =',format(b,'08b'))
print('-----------------------------------------------------not XOR')
c= ~(a ^ b)
print('Nilai ~(',a,'^',b,')Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk Operasi not geser kanan, c = ~(a >> 2)
print('\n\tTugas 11 not Geser Kanan c=~(a >> 2)\n')
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kanan')
c= ~(a >> 2)
print('Nilai ~(',a,'>> 2)','Dalam Biner Adalah',format(c,'08b'))

# Tugas untuk Operasi not geser Kiri, c = ~(a << 2)
print('\n\tTugas 12 not Geser Kiri c=~(a << 2)\n')
print('=========================not Geser kanan')
print('Nilai',a,'Dalam biner                =',format(a,'08b'))
print('-----------------------------------------------------not geser kiri')
c= ~(a << 2)
print('Nilai ~(',a,'<< 2)','Dalam Biner Adalah',format(c,'08b'))

