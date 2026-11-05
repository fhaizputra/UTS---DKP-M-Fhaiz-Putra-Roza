"""UTS Dasar Komputer dan Pemrograman - Kelompok A (Tenaga)
Monitoring Beban/Daya Listrik menggunakan model P = V x I.
"""

TEGANGAN = 220          # volt
BATAS_NORMAL = 700      # watt
BATAS_WARNING = 1000    # watt

# 15 data inti dari soal + 5 data tambahan (ditandai pada komentar)
data_arus = [
    1.6, 2.2, 3.5, 4.1, 5.4, 2.8, 6.0, 3.9, 1.9, 4.8, 5.1, 2.6, 3.2, 4.4, 5.8,
    0.5, 3.1, 3.3, 4.5, 4.6,   # 5 data tambahan
]

DAFTAR_STATUS = ["NORMAL", "WARNING", "BEBAN TINGGI"]


def hitung_daya(tegangan, arus):
    """Menghitung daya listrik (watt) dengan P = V x I."""
    return tegangan * arus


def status_beban(daya):
    """Menentukan status beban berdasarkan daya (watt)."""
    if daya <= BATAS_NORMAL:
        return "NORMAL"
    elif daya <= BATAS_WARNING:
        return "WARNING"
    else:
        return "BEBAN TINGGI"


def rata_rata(data):
    """Menghitung nilai rata-rata dari sebuah list angka."""
    return sum(data) / len(data)


def main():
    daftar_daya = []
    jumlah_status = {status: 0 for status in DAFTAR_STATUS}

    print("===== MONITORING BEBAN/DAYA LISTRIK (V = 220 V) =====")
    for nomor, arus in enumerate(data_arus, start=1):
        daya = hitung_daya(TEGANGAN, arus)
        status = status_beban(daya)
        daftar_daya.append(daya)
        jumlah_status[status] += 1
        print(f"{nomor:02d}  I = {arus:4.1f} A  P = {daya:7.1f} W  -> {status}")

    print("\n===== RINGKASAN =====")
    print(f"Total data    : {len(data_arus)}")
    for status in DAFTAR_STATUS:
        print(f"{status:<13} : {jumlah_status[status]}")
    print(f"Rata-rata P   : {rata_rata(daftar_daya):.2f} W")
    print(f"Maksimum P    : {max(daftar_daya):.1f} W")
    print(f"Minimum P     : {min(daftar_daya):.1f} W")


if __name__ == "__main__":
    main()
