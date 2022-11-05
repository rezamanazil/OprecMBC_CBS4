total_belanja=int(input("Masukan total belanja Anda\t  : Rp."))
member=str(input("Apakah Anda sudah member (yes/no) : "))

if(total_belanja>=500000 and total_belanja<=1000000):
    if(member=="yes" or member=="Yes" or member=="YES"):
        print("Selamat Anda mendapatkan diskon 7%")
    else:
        print("Selamat Anda mendapatkan diskon 2%")
elif(total_belanja>1000000):
    if(member=="yes" or member=="Yes" or member=="YES"):
        print("Selamat Anda mendapatkan diskon 8%")
    else:
        print("Selamat Anda mendapatkan diskon 3%")
else:
    if(member=="yes" or member=="Yes" or member=="YES"):
        print("Selamat Anda mendapatkan diskon 5%")
    else:
        print("Maaf Anda tidak mendapatkan diskon :)")