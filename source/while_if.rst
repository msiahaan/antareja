Diskon....Diskon...
====================

Kembali ke kisah fiksi di bagian sebalumnya, Anda menghadap Boss dengan hasil: "Pendapatan kita bulan ini: Rp. 9.290.000, Boss!". Boss bertanya: "Ok, apakah itu sudah memperhitungkan diskon 25% untuk pembeli ayam ke-50 dan bebek ke-50? Bulan ini kita promo, lho!". Yah, bagaimana ini si Boss? Kok baru bilang?

Tapi tenang. Sebagai seaorang *Python Programmer* saatnya menggunakan senjata baru: *while* dan *if*. Anda pun mengetikkan program berikut::

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

dan jalankan::

    Jumlah ayam terjual 74 ekor
    Jumlah bebek terjual 68 ekor
    Pendapatan bulan ini Rp. 9257500.0

maka Anda pun kembali ke Boss dengan jawaban: "Ok, boss, pendapatan kita bulan ini: Rp. 9.257.500".

Masih mengikuti? Ada 3 konsep yang ingin ditunjukkan dalam contoh program di atas:

while
------

*while* adalah *statement* yang mengindikasikan bahwa kita ingin mengulang sebuah bagian program selama kondisi perulangan masih terpenuhi. Contoh yang lebih sederhana dari contoh program kita::

    a = 10
    b = 1
    while b <= a:
	    print b
	    b = b + 1

yang apabila dijalankan::

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

kita mencetak nilai variabel *b* selama nilai *b* lebih kecil atau sama dengan nilai variabel *a*. 

Indentasi
---------

Bagian-bagian program dari sebuah program python ditunjukkan dengan indentasi/perataan. Jadi jangan lupa untuk menambahkan spasi pada bagian program yang diulang. Misalnya Anda lupa menambahkan spasi seperti berikut::

    a = 10
    b = 1

    while b <= a:
    print b
    b = b + 1
	
apabila dijalankan akan membangkitkan pesan kesalahan::

    File "<pyshell#14>", line 2
        print b
            ^
    IndentationError: expected an indented block

*IndentationError* kata python.


if...else...
------------

*if...else...* adalah statement yang mengindikasikan bahwa sebuah bagian program akan dijalankan apabila sebuah kondisi terpenuhi. Contoh program yang lebih sederhana::

    a = 4
    b = 5

    if a > b:
        print a, 'lebih besar dari', b
    elif a == b:
        print a, 'sama dengan', b
    else:
        print a, 'lebih kecil dari', b

Apabila dijalankan::

    4 lebih kecil dari 5
	
*elif* memungkinkan ada lebih dari sebuah kondisi.

Operator perbandingan
---------------------

Dalam menyatakan kondisi perbandingan, kita menggunakan *operator perbandingan*. Operator perbandingan yang dikenal:

========  ====
Operator  Arti           
========  ====
<         Lebih kecil dari    
<=        Lebih kecil atau sama dengan    
>         Lebih besar dari      
>=        Lebih besar atau sama dengan
==        Sama dengan
!=        Tidak sama dengan      
========  ====

Rangkuman
---------
Pada bagian ini kita telah belajar mengenai:

* *while* statement
* indentasi
* *if...else...* statement

