import random
import os
import time

# ======================
#       DATA MENU
# ======================

menu_makanan = {
    "Nasi Goreng": 18000,
    "Ayam Geprek": 17000,
    "Mie Ayam": 15000,
    "Soto Ayam": 16000,
    "Bakso": 14000,
    "Nasi Padang": 22000,
    "Gado-Gado": 13000,
    "Ayam Panggang": 25000,
    "Mie Goreng": 12000
}

menu_minuman = {
    "Es Teh Manis": 8000,
    "Es Jeruk": 9000,
    "Teh Hangat": 7000,
    "Kopi Hitam": 10000,
    "Cappuccino": 15000,
    "Air Mineral": 5000,
    "Jus Mangga": 12000,
    "Jus Alpukat": 13000
}

# ======================
#       FUNGSI UMUM
# ======================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_daftar(jenis, data):
    print(f"\n=== DAFTAR MENU {jenis.upper()} ===")
    for i, (nama, harga) in enumerate(data.items(), start=1):
        print(f"{i}. {nama} - Rp{harga:,}")
    print()

def pilih_satu_manual(data):
    try:
        nomor = int(input("Pilih nomor item: "))
        daftar = list(data.items())
        if 1 <= nomor <= len(daftar):
            nama, harga = daftar[nomor - 1]
            print(f"\nKamu memilih: {nama} (Rp{harga:,})")
            print(f"TOTAL: Rp{harga:,}")
        else:
            print("Nomor tidak ada!")
    except ValueError:
        print("Input harus angka!")

def pilih_beberapa_manual(data, jumlah):
    daftar = list(data)

    print("\n=== PILIH BEBERAPA ITEM ===")
    for i, (nama, harga) in enumerate(daftar, start=1):
        print(f"{i}. {nama} - Rp{harga:,}")

    total = 0
    dipilih = []

    for i in range(jumlah):
        try:
            nomor = int(input(f"Pilih item ke-{i+1}: "))
            if 1 <= nomor <= len(daftar):
                nama, harga = daftar[nomor - 1]
                dipilih.append((nama, harga))
                total += harga
            else:
                print("Nomor tidak ada!")
        except ValueError:
            print("Input harus angka!")
            return

    print("\n=== HASIL PILIHAN ===")
    for nama, harga in dipilih:
        print(f"- {nama} (Rp{harga:,})")

    print(f"\nTOTAL HARGA: Rp{total:,}")

def acak_beberapa(data, jumlah):
    hasil = random.sample(list(data.items()), jumlah)
    total = sum([h for _, h in hasil])

    print("\n=== HASIL ACAK ===")
    for nama, harga in hasil:
        print(f"- {nama} (Rp{harga:,})")

    print(f"\nTOTAL HARGA: Rp{total:,}")

# ======================
#     PROGRAM UTAMA
# ======================

def main():
    while True:
        clear()
        print("======================================")
        print(" 🍽️  APLIKASI PILIH MAKANAN & MINUMAN  🥤 ")
        print("======================================\n")

        print("1. Pilih makanan (manual)")
        print("2. Pilih minuman (manual)")
        print("3. Acak makanan 1 item")
        print("4. Acak minuman 1 item")
        print("5. Acak combo 1 makanan + 1 minuman")
        print("6. Pilih beberapa makanan (manual)")
        print("7. Pilih beberapa minuman (manual)")
        print("8. Acak beberapa makanan")
        print("9. Acak beberapa minuman")
        print("10. Acak beberapa campuran")
        print("11. Pilih beberapa campuran (manual)")
        print("12. Keluar\n")

        pilihan = input("Pilih menu: ")

        # --------------------------- MENU 1 ---------------------------
        if pilihan == "1":
            clear()
            tampilkan_daftar("Makanan", menu_makanan)
            pilih_satu_manual(menu_makanan)
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 2 ---------------------------
        elif pilihan == "2":
            clear()
            tampilkan_daftar("Minuman", menu_minuman)
            pilih_satu_manual(menu_minuman)
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 3 ---------------------------
        elif pilihan == "3":
            clear()
            nama, harga = random.choice(list(menu_makanan.items()))
            print("Hasil acak makanan:")
            print(f"- {nama} (Rp{harga:,})")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 4 ---------------------------
        elif pilihan == "4":
            clear()
            nama, harga = random.choice(list(menu_minuman.items()))
            print("Hasil acak minuman:")
            print(f"- {nama} (Rp{harga:,})")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 5 ---------------------------
        elif pilihan == "5":
            clear()
            m1, h1 = random.choice(list(menu_makanan.items()))
            m2, h2 = random.choice(list(menu_minuman.items()))
            print("Combo acak:")
            print(f"- {m1} (Rp{h1:,})")
            print(f"- {m2} (Rp{h2:,})")
            print(f"\nTOTAL: Rp{h1+h2:,}")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 6 ---------------------------
        elif pilihan == "6":
            clear()
            try:
                jumlah = int(input("Berapa item makanan ingin dipilih? "))
                pilih_beberapa_manual(list(menu_makanan.items()), jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 7 ---------------------------
        elif pilihan == "7":
            clear()
            try:
                jumlah = int(input("Berapa item minuman ingin dipilih? "))
                pilih_beberapa_manual(list(menu_minuman.items()), jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 8 ---------------------------
        elif pilihan == "8":
            clear()
            try:
                jumlah = int(input("Berapa makanan acak? "))
                acak_beberapa(menu_makanan, jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 9 ---------------------------
        elif pilihan == "9":
            clear()
            try:
                jumlah = int(input("Berapa minuman acak? "))
                acak_beberapa(menu_minuman, jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 10 (CAMPUR ACAK) ---------------------------
        elif pilihan == "10":
            clear()
            try:
                campuran = list(menu_makanan.items()) + list(menu_minuman.items())
                jumlah = int(input("Berapa item campuran acak? "))
                acak_beberapa(dict(campuran), jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 11 (CAMPUR MANUAL) ---------------------------
        elif pilihan == "11":
            clear()
            try:
                campuran = list(menu_makanan.items()) + list(menu_minuman.items())
                jumlah = int(input("Berapa item ingin dipilih? "))
                pilih_beberapa_manual(campuran, jumlah)
            except ValueError:
                print("Input harus angka!")
            input("\nEnter untuk kembali...")

        # --------------------------- MENU 12 (EXIT) ---------------------------
        elif pilihan == "12":
            print("Terima kasih! 👋")
            break

        else:
            print("Input tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
