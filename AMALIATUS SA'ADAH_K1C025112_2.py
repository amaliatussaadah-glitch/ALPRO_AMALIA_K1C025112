def hitung_rx(r1, r2, r3):
    """Fungsi untuk menghitung Rx berdasarkan rumus Jembatan Wheatstone"""
    return r2 * (r3 / r1)

def main():
    print("--- Program Perhitungan Jembatan Wheatstone ---")
    print("Rumus: Rx = R2 * (R3 / R1)\n")

    try:
        # Prosedur: Validasi Input
        r1 = float(input("Masukkan nilai R1 (Ohm): "))
        r2 = float(input("Masukkan nilai R2 (Ohm): "))
        r3 = float(input("Masukkan nilai R3 (Ohm): "))

        if r1 <= 0 or r2 <= 0 or r3 <= 0:
            print("\nKesalahan: Nilai hambatan harus lebih besar dari nol!")
        else:
            # Memanggil fungsi hitung
            rx = hitung_rx(r1, r2, r3)
            
            # Prosedur: Tampil Hasil
            print("-" * 40)
            print(f"Hasil Perhitungan Rx adalah: {rx:.2f} Ohm")
            print("-" * 40)

    except ValueError:
        print("\nKesalahan: Mohon masukkan angka yang valid.")

if __name__ == "__main__":
    main()