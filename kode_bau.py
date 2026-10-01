"""Program sederhana untuk demonstrasi Pylint."""


def hitung_nilai(angka1, angka2):
    """Menghitung penjumlahan dua angka."""
    return angka1 + angka2


def main():
    """Menjalankan program utama."""
    hasil = hitung_nilai(1, 2)
    print(hasil)


if __name__ == "__main__":
    main()
