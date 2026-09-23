def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        harga = 200000
    else:
        harga = 350000

    return harga * lama_menginap


jenis_kamar = input("Jenis kamar (Standard/Deluxe): ")
check_in = input("Tanggal check-in: ")
check_out = input("Tanggal check-out: ")
lama_menginap = int(input("Lama menginap (malam): "))

total = hitung_biaya(jenis_kamar, lama_menginap)

print("\n=== PEMESANAN HOTEL ===")
print("Jenis kamar:", jenis_kamar)
print("Check-in:", check_in)
print("Check-out:", check_out)
print("Lama menginap:", lama_menginap, "malam")
print("Total biaya: Rp", total)