# Data nama
nama ="MUHAMMAD ALIF FIRANSYAH"

# Ubah jadi array  dan urutkan
data =['M','U','H','A','M','M','A','L','I','F','F','I','R','A','N','S','Y','A','H']
data.sort()
print("Data setelah diurutkan:", data)

# Nilai yang dicari
cari = 'A'

# Binary search
kiri = 0
kanan = len(data) - 1
ditemukan = False
while kiri <= kanan:
    tengah = (kiri + kanan) // 2

    if data[tengah] == cari:
        ditemukan = True
        print("Huruf A ditemukan di index ke-", tengah)
        break
    elif data[tengah] < cari:
        kiri = tengah + 1
    else:
        kanan = tengah - 1

if not ditemukan:
    print("Huruf A tidak ditemukan")