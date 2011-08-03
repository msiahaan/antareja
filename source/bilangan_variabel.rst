Bilangan dan Variabel
======================

Ayam dan Bebek
---------------

Anda bekerja di pedagang ayam dan bebek, dan suatu saat Boss meminta: "Tolong hitung pendapatan kita bulan ini! SEKARANG!". Karena Anda seorang *Python Programmer* maka,

* buka laptop Anda
* jalankan IDLE
* buka jendela baru dalam IDLE untuk membuat program Python baru
* ketikkan baris-baris berikut::

    # contoh2.py
    # program untuk menghitung pendapatan per bulan
    # dari suatu pedagang ayam + bebek fiktif

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

    #pendapatan bulan ini
    pendapatan = (ayam*harga_ayam) + (bebek*harga_bebek)
    print "Pendapatan bulan ini Rp.", pendapatan
	
Kemudian jalankan program kita::

    Jumlah ayam terjual 74 ekor
    Jumlah bebek terjual 68 ekor
    Pendapatan bulan ini Rp. 9290000

Dan Anda pun menghadap Boss dengan hasil: "Pendapatan kita bulan ini: Rp. 9.290.000, Boss!"

Contoh di atas kisah rekaan namun saya ingin menyajikan beberapa konsep yang penting::

    ayam = 10 + 15 + 36 / 6 + 45 - 2
	
*ayam* adalah sebuah variabel. Apakah variabel itu? *Variabel* adalah sebuah identitas dari sebuah tempat dalam memori yang menyimpan data. Variabel *ayam* di atas menyimpan data dalam memori yang berupa data bilangan bulangan bulat. Sebelum data disimpan dalam variabel *ayam* kita melakukan beberapa operasi bilangan. Operasi bilangan ditandai dengan penggunaan *operator* bilangan / matematika. Jenis-jenis *operator matematika* yang dikenal

========  ====
Operator  Arti           
========  ====
\+        Penambahan     
\-        Pengurangan     
/         Pembagian       
%         Sisa pembagian 
\*        Perkalian      
========  ====

Sebagai catatan tambahan, Python juga mengenal jenis data bilangan selain bilangan bulat, yaitu data *real/float* (bilangan pecahan) dan bilangan *imajiner*. Sebagai referensi: `Python Language Reference, Data Model`_

.. _Python Language Reference, Data Model: http://docs.python.org/reference/datamodel.html

*Operator* yang bekerja atas bilangan *real/flot* dan *imajiner* sama dengan operator bilangan bulat. Silakan dicoba sendiri ya!

Rangkuman
----------

Melalui contoh singkat di atas kita telah belajat tentang

* variabel
* operasi matematika/bilangan

