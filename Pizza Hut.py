#Pelanggan masuk ke website
print("="*30)
print("Selamat Datang Di PIzza Hut")
print("="*30)
#dictionary daftar topping
topping = {
    1: "Frankfurter",
    2: "Meat Monsta",
    3: "Super Supreme",
    4: "Super Supreme Chicken"
}
#Pelanggan akan memilih toping
print()
print("+======================================================+")
print("|               Silakan pilih toping Anda              |")
print("|===========================|==========================|")
print("|           Toping          |           Harga          |")
print("|===========================|==========================|")
print("|  1. Frankfurter           |  Rp. 43.637              |")
print("|  2. Meat Monsta           |  Rp. 43.637              |")
print("|  3. Super Supreme         |  Rp. 43.637              |")
print("|  4. Super Supreme Chicken |  Rp. 43.637              |")
print("|===========================|==========================|")
pilih = int(input("  Silakan Pilih Pesanan Anda ( Masukan angka 1-4) : "))
topping_name = topping [pilih]
print("|======================================================|")
print()
#harga awal
harga = 0;

#pilihan topping
if pilih == 1 or 2 or 3 or 4:
    harga += 43637
else:
    print("INVALID NUMBER!!")

#pelanggan memilih crust
print("|======================================================|")
print("|                      Pilih crust                     |")
print("|======================================================|")
print("|   1. pan                                             |")
print("|   2. Stuffedcrust Cheese                             |")
print("|   3. Stuffedcrust Sausage                            |")
print("|   4. Cheesy Bites                                    |")
print("|======================================================|")
crust = int(input("  Silakan Pilih Pesanan Anda ( Masukan angka 1-4) : "))
print("|======================================================|")
print()

#dictionary crust
crustt = {
    1: "pan",
    2: "Stuffedcrust Cheese",
    3: "Stuffedcrust Sausage",
    4: "Cheesy Bites"
}
crust_name = crustt[crust]
#Pemilihan crust
if crust == 1:
    harga += 0
    #pemilihan ukuran
    print("pilih ukuran")
    print("1. Personal")
    print("2. Regular")
    print("3. Large")
    ukuran=int(input("Masukan ukuran: "))
    if ukuran == 1:
        harga += 0
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 13636
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 2:
        harga += 57273
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 16364
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 3:
        harga += 89091
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 19091
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")

elif crust == 2:
    harga += 11818
    #pemilihan ukuran
    print("pilih ukuran")
    print("1. Personal")
    print("2. Regular")
    print("3. Large")
    ukuran=int(input("Masukan ukuran: "))
    if ukuran == 1:
        harga += 0
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 13636
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 2:
        harga += 65455
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 16364
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 3:
        harga += 104545
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 19091
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
elif crust == 3:
    harga += 9091
    #pemilihan ukuran
    print("pilih ukuran")
    print("1. Personal")
    print("2. Regular")
    print("3. Large")
    ukuran=int(input("Masukan ukuran: "))
    if ukuran == 1:
        harga += 0
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 13636
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 2:
        harga += 64545
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 16364
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 3:
        harga += 102727
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 19091
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
elif crust == 4:
    harga += 13636
    #pemilihan ukuran
    print("pilih ukuran")
    print("1. Personal")
    print("2. Regular")
    print("3. Large")
    ukuran=int(input("Masukan ukuran: "))
    if ukuran == 1:
        harga += 0
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 13636
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 2:
        harga += 66364
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 16364
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 3:
        harga += 107273
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 19091
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
elif crust == 5:
    harga += 11818
    #pemilihan ukuran
    print("pilih ukuran")
    print("1. Personal")
    print("2. Regular")
    print("3. Large")
    ukuran=int(input("Masukan ukuran: "))
    if ukuran == 1:
        harga += 0
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 13636
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 2:
        harga += 65455
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 16364
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
    elif ukuran == 3:
        harga += 104545
        cheese = input("Extra Cheese(y/n): ")
        if cheese == "y":
            harga += 19091
        elif cheese == "n":
            harga += 0
        else:
            print("Invalid")
else:
    print("Invalid Number (Tolong masukan antara nomor 1-5)")

print()
print("===========================================================================================")
print ("Terima Kasih Telah Memesan Pizza Di Pizza HUT")
print (f"pizza yang Anda pesan adalah : {topping_name} dengan pilihan crust {crust_name}",)
print(f"Total tagihan belanjaan Anda adalah: Rp. {harga}")
print("===========================================================================================")
