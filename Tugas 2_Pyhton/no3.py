hari=str(input("Masukan Hari : "))

if(hari=="senin" or hari=="SENIN"):
    print("Seragam Hari senin adalah Merah")
elif(hari=="selasa" or hari=="SELASA" or hari=="rabu" or hari=="RABU"):
    print("Seragam Hari selasa/rabu adalah Putih")
elif(hari=="kamis" or hari=="KAMIS" or hari=="sabtu" or hari=="SABTU"):
    print("Seragan Hari kamis/sabtu adalah Bebas")
elif(hari=="jumat" or hari=="JUMAT"):
    print("Seragan Hari jumat adalah Batik")
elif(hari=="minggu" or hari=="MINGGU"):
    print("LIBUR TURU AJA")
else:
    print("HARI YANG ANDA INPUT TIDAK ADA")
