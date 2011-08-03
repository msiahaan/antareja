# contoh3.py
# program untuk menghitung pendapatan per bulan
# dari suatu pedagang ayam + bebek fiktif
# pembeli ayam ke-50 dan bebek ke-50 dapat diskon 25%

# jumlah ayam yang laku bulan ini
ayam = 10 + 15 + 36 / 6 + 45 - 2
print "Jumlah ayam terjual", ayam, "ekor"

# harga jual ayam
harga_ayam = 75000

# jumlah bebek yang laku bulan ini
bebek = 34 + 2 + 24 % 12 + 34 - 2
print "Jumlah bebek terjual", bebek, "ekor"

# harga bebek
harga_bebek = 55000

# diskon
diskon = 0.25

#menghitung pendapatan
pendapatan = 0
ayam_ke = 1 # variabel untuk tracking ayam ke-
bebek_ke = 1 # variabel untuk tracking bebek ke-

# mulai perulangan ayam ke-
while ayam_ke <= ayam:
    if ayam_ke == 50:
        pendapatan = pendapatan + (1-diskon) * harga_ayam
    else:
        pendapatan = pendapatan + harga_ayam
    ayam_ke = ayam_ke + 1 # naikkan nilai ayam_ke

# mulai perulangan bebek ke-
while bebek_ke <= bebek:
    if bebek_ke == 50:
        pendapatan = pendapatan + (1-diskon) * harga_bebek
    else:
        pendapatan = pendapatan + harga_bebek
    bebek_ke = bebek_ke + 1 # naikkan nilai bebek_ke    
        
print "Pendapatan bulan ini Rp.", pendapatan

