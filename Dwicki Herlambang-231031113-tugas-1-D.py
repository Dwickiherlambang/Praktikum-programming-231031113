
print('\n')
biodata = { 'nama'  : 'Dwicki Herlambang',
'nim'   : '231031113',
'kelas' : 'S123D',
'agama' : 'islam',
'alamat': 'Jln Jati, Perumnas Wekke"e',
'kewarganegaraan' : 'WNI',
'email' : 'dwickiherlambang4@@gmail.com'
}

print(biodata['nama'],biodata['nim'],biodata['email'])
print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:4])
print(selected_biodata)




