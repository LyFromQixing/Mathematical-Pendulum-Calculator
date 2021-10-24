# Kalkulator untuk menghitung periode bandul matematis dengan sudut awal tertentu
# Credit: Rafli Rizaldi/16021150 a.k.a QueenLy/LyFromQixing

import math

l = float(input("Masukkan panjang tali dalam cm: "))
g = float(input("Masukkan g: "))
a = float(input("Masukkan sudut dalam derajat: "))

l_0 = l/100 # Ubah panjang tali ke dalam satuan meter 
rad = ((a)/180) * math.pi # Ubah satuan sudut ke dalam radian 
T_0 = (2*math.pi)*((l_0/g)**(1/2)) # Hitung nilai T sebelum ada ekspansi
ekspansi = (1+((1/4)*(math.sin(rad/2)**2)))+(((9/64)*(math.sin(rad/2)**4))) # Hitung nilai ekspansinya
T = T_0 * ekspansi # Nilai periode bandul dengan sudut awal dapat ditentukan dengan mengalikan nilai T awal dengan nilai ekspansi

print("Periode teoritis bandul dengan sudut awal " + str(a) + " adalah " + str(T))
