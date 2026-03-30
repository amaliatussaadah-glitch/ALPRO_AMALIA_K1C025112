def hitung_fisika_sepeda(m, g, theta, v):
    """
    Menghitung gaya turun, gaya naik, dan daya berdasarkan rumus di foto.
    m: massa (kg)
    g: gravitasi (m/s^2)
    theta: sudut (dalam radian)
    v: kecepatan (m/s)
    """
    import math

    # 1. Fase Turun (mencari gaya gesek/hambat f_fr)
    # Rumus: f_fr = m * g * sin(theta)
    f_fr = m * g * math.sin(theta)

    # 2. Fase Naik (mencari gaya pedal f_p)
    # Rumus: f_p = f_fr + m * g * sin(theta)
    # Karena f_fr = m * g * sin(theta), maka f_p = 2 * m * g * sin(theta)
    f_p = 2 * m * g * math.sin(theta)

    # 3. Daya (P)
    # Rumus: P = f_p * v
    daya = f_p * v

    return f_fr, f_p, daya

# --- Prosedur: Langkah + Hasil ---

# Input Parameter
massa = 70      # kg
gravitasi = 9.8 # m/s^2
kecepatan = 5   # m/s
sudut_deg = 10  # derajat
sudut_rad = (sudut_deg * 3.14159) / 180 # Konversi ke radian

# Eksekusi Fungsi
turun, naik, p_output = hitung_fisika_sepeda(massa, gravitasi, sudut_rad, kecepatan)

# Menampilkan Hasil
print("--- Hasil Perhitungan Fisika Pesepeda ---")
print(f"Gua Hambat (Fase Turun) : {turun:.2f} N")
print(f"Gaya Pedal (Fase Naik)  : {naik:.2f} N")
print(f"Daya yang Dihasilkan    : {p_output:.2f} Watt")