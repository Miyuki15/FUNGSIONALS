def hit_nilai_akhir(uts, uas):
    return 0.4 * uts + 0.6 * uas


def hit_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hit_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir


def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hsl Nilai akhir mahasiswa: ")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\nNilai Akhir: {:.2f}".format(nama, nilai_akhir))
        print()


def main():
    data_mahasiswa = {

        'marjoko tachibana': {'uts': 99, 'uas': 69},
        'yudoyono sensei': {'uts': 29, 'uas': 89},
        'mahartotshuka': {'uts': 79, 'uas': 49},
    }

    data_nilai_akhir = hit_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)


if __name__ == "__main__":
    main()
