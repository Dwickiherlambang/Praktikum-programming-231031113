#Input bilangan dari pengguna
bilangan = int(input("Masukkan sebuah bilangan: "))

#Periksa apakah bilangan ganjil atau genap
if bilangan % 2 == 1:
    print(f"{bilangan} adalah bilangan ganjil.")
else:
    print(f"{bilangan} bukan bilangan ganjil.")

print()
