# title aja
print("\n\t==============================")
print("\t == KALKULATOR KABAGTAKUR ==")
print("\t==============================\n")

# Proses input nilai/data
nilai1=int(input("Masukan Angka Pertama \t: "))
nilai2=int(input("Masukan Angka Kedua \t: "))

# Menu Pilihan
print("\n1. Penjumlahan\n")
print("2. Pengurangan\n")
print("3. Perkalian\n")
print("4. Pembagian\n")

#Proses pemilihan proses perhitungan
pilih=int(input("Pilih Proses Perhitungan : "))

if(pilih == 1):
    nilai3 = nilai1+nilai2
    print("Hasil Penjumlahan ",nilai1,"dan ",nilai2," adalah ",nilai3)
elif(pilih == 2):
    nilai3 = nilai1-nilai2
    print("Hasil Pengurangan ",nilai1," dan ",nilai2," adalah ",nilai3)
elif(pilih == 3):
    nilai3 = nilai1*nilai2
    print("Hasil Perkalian ",nilai1," dan ",nilai2," adalah ",nilai3)
elif(pilih == 4):
    nilai3 = nilai1/nilai2
    print("Hasil Pembagian ",nilai1," dan ",nilai2," adalah ",nilai3)
else:
    print("Maaf Pilihan Anda tidak tersedia")