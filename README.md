import random
import os
import time

# ======================
#   DATA MENU
# ======================

menu_makanan = {
    "Nasi Goreng"   : 18000,
    "Ayam Geprek"   : 17000,
    "Mie Ayam"      : 15000,
    "Soto Ayam"     : 16000,
    "Bakso"         : 14000,
    "Nasi Padang"   : 22000,
    "Gado-Gado"     : 13000,
    "Ayam Panggang" : 25000,
    "Mie Goreng"    : 12000
}

menu_minuman = {
    "Es Teh Manis"     : 8000,
    "Es Jeruk"         : 9000,
    "Teh Hangat"       : 7000,
    "Kopi Hitam"       : 10000,
    "Cappuccino"       : 15000,
    "Air Mineral"      : 5000,
    "Jus Mangga"       : 12000,
    "Jus Alpukat"      : 13000
}

# ======================
#   FUNGSI
# ======================

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tampilkan_daftar(jenis, data):
    """
    data: dict expected (nama->harga)
    """
    print(f"\n=== DAFTAR MENU {jenis.upper()} ===")
    if isinstance(data, dict):
        for i, (nama, harga) in enumerate(data.items(), start=1):
            print(f"{i}. {nama} - Rp{harga:,}")
    else:
        # fallback: list of tuples
        for i, item in enumerate(data, start=1):
            if isinstance(item, tuple) and len(item) >= 2:
                nama, harga = item[0], item[1]
                print(f"{i}. {nama} - Rp{harga:,}")
            else:
                print(f"{i}. {item}")
    print()

def header():
    print("===================================")
    print(" 🍽️  APLIKASI PILIH MAKANAN & MINUMAN  🥤 ")
    print("===================================")

def pilih_manual(data):
    tampilkan_daftar("PILIH", data)
    try:
        nomor = int(input("Pilih berdasarkan nomor: "))
        daftar = _to_items(data)
        if 1 <= nomor <= len(daftar):
            nama, harga = daftar[nomor - 1]
            print(f"\n🎉 Kamu memilih: {nama}")
            print(f"💰 Harga: Rp{harga:,}\n")
        else:
            print("\nNomor tidak ada!")
    except (ValueError, IndexError):
        print("Input tidak valid!")

def pilih_beberapa_manual(data, jumlah):
    daftar = _to_items(data)
    if jumlah < 1 or jumlah > len(daftar):
        print(f"Jumlah harus antara 1 dan {len(daftar)}")
        return

    tampilkan_daftar("PILIH BEBERAPA", data)
    pilihan = []
    for i in range(jumlah):
        try:
            nomor = int(input(f"Pilih item ke-{i+1}: "))
            if not (1 <= nomor <= len(daftar)):
                print("Nomor tidak ada! Batalkan proses.")
                return
            nama, harga = daftar[nomor - 1]
            pilihan.append((nama, harga))
        except ValueError:
            print("Input harus angka! Batalkan proses.")
            return
    
    print("\n🎉 Pilihanmu:")
    for n, h in pilihan:
        print(f"- {n} (Rp{h:,})")

def acak_satu(data):
    items = _to_items(data)
    nama, harga = random.choice(items)
    print(f"🎲 Hasil acak: {nama} (Rp{harga:,})")

def acak_beberapa(data, jumlah):
    items = _to_items(data)
    if jumlah < 1 or jumlah > len(items):
        print(f"Jumlah harus antara 1 dan {len(items)}")
        return
    hasil = random.sample(items, jumlah)
    print("\n🎉 Hasil acak:")
    for nama, harga in hasil:
        print(f"- {nama} (Rp{harga:,})")

def _to_items(data):
    """
    Normalize input to a list of (nama, harga).
    Accepts:
      - dict -> list(dict.items())
      - list of tuples -> returned as-is
    """
    if isinstance(data, dict):
        return list(data.items())
    elif isinstance(data, list):
        # assume list of tuples (nama, harga) or single strings
        normalized = []
        for it in data:
            if isinstance(it, tuple) and len(it) >= 2:
                normalized.append((it[0], it[1]))
            elif isinstance(it, str):
                normalized.append((it, 0))
            else:
                # unknown format, try to coerce
                try:
                    normalized.append((str(it[0]), int(it[1])))
                except Exception:
                    pass
        return normalized
    else:
        raise TypeError("Data harus dict atau list")

# ======================
#   PROGRAM UTAMA
# ======================

def main():
    while True:
        clear()
        header()
        print("1. Pilih item (manual/acak/beberapa)")
        print("2. Acak beberapa (demo cepat)")
        print("3. Keluar")
        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            clear()
            print("=== PILIH ITEM ===")
            print("1. Pilih makanan (manual)")
            print("2. Pilih minuman (manual)")
            print("3. Acak makanan")
            print("4. Acak minuman")
            print("5. Acak makanan + minuman (1 makanan + 1 minuman)")
            print("6. Pilih beberapa makanan (manual)")
            print("7. Pilih beberapa minuman (manual)")
            print("8. Acak beberapa makanan")
            print("9. Acak beberapa minuman")
            print("10. Acak beberapa (campuran makanan+minuman)")
            
            sub = input("\nPilih opsi: ")
            clear()

            # Manual single
            if sub == "1":
                pilih_manual(menu_makanan)
            elif sub == "2":
                pilih_manual(menu_minuman)

            # Acak single
            elif sub == "3":
                acak_satu(menu_makanan)
            elif sub == "4":
                acak_satu(menu_minuman)
            elif sub == "5":
                # acak 1 makanan + 1 minuman
                makanan = random.choice(list(menu_makanan.items()))
                minuman = random.choice(list(menu_minuman.items()))
                print("🎉 Pilihan Acak Kamu:")
                print(f"🍽️ Makanan : {makanan[0]} (Rp{makanan[1]:,})")
                print(f"🥤 Minuman : {minuman[0]} (Rp{minuman[1]:,})")

            # Manual beberapa
            elif sub == "6":
                try:
                    jumlah = int(input("Berapa item makanan? "))
                    pilih_beberapa_manual(menu_makanan, jumlah)
                except ValueError:
                    print("Input harus angka!")

            elif sub == "7":
                try:
                    jumlah = int(input("Berapa item minuman? "))
                    pilih_beberapa_manual(menu_minuman, jumlah)
                except ValueError:
                    print("Input harus angka!")

            # Acak beberapa makanan/minuman/campuran
            elif sub == "8":
                try:
                    jumlah = int(input("Berapa item acak (makanan)? "))
                    acak_beberapa(menu_makanan, jumlah)
                except ValueError:
                    print("Input harus angka!")

            elif sub == "9":
                try:
                    jumlah = int(input("Berapa item acak (minuman)? "))
                    acak_beberapa(menu_minuman, jumlah)
                except ValueError:
                    print("Input harus angka!")

            elif sub == "10":
                try:
                    jumlah = int(input("Berapa item acak (campuran)? "))
                    campuran = list(menu_makanan.items()) + list(menu_minuman.items())
                    acak_beberapa(campuran, jumlah)
                except ValueError:
                    print("Input harus angka!")

            else:
                print("Pilihan tidak valid!")

            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2":
            # demo cepat: acak 3 item campuran
            clear()
            campuran = list(menu_makanan.items()) + list(menu_minuman.items())
            acak_beberapa(campuran, 3)
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "3":
            print("Terima kasih! Sampai jumpa 👋")
            break
        
        else:
            print("Pilihan tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
