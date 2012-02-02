Pemrograman Berorientasi Objek
==============================

OOP atau Object Oriented Programming atau bahasa Inggrisnya Bahasa Pemrograman Berorientasi Objek adalah paradigma dalam dunia pemrograman yang menekankan modifikasi serta penggunaan dari 'objek'. Objek itu apaan sih kakak? Objek adalah representasi atau perwakilan atau penggambaran dari benda yang ada di keseharian kita. 

Bedanya apa dong dengan pemrograman prosedural? Bedanya dalam pemrograman prosedural, program adalah kumpulan dari prosedur.

Contohnya: program membuat kue prosedural::

    def bikin_kue():
        timbang_gula()
        timbang_tepung()
        campur_gula_tepung()
        bakar_adonan()

    def timbang_gula():
        print "Gula 100g"

    def timbang_tepung():
        print "Tepung 1 kg"

    def campur_gula_tepung():
        print "Mencampur gula dan tepung"

    def bakar_adonan():
        print "Bakar adonan"
        print "Kue siap"


    #panggil prosedur utama bikin kue
    bikin_kue()

Nah, di sini kita membuat kue mengikuti prosedur: timbang_gula, dan seterusnya hingga kue siap.

Bikin Kue dengan paradigma OOP::

    class Kue(object):
        def tambah_gula(self, jumlah):
            self.gula = jumlah
            print "Gula: " + str(self.gula) + " g"
        
        def tambah_tepung(self, jumlah):
            self.tepung = jumlah
            print "Tepung: " + str(self.tepung) + " kg"
        
        def campur_gula_tepung(self):
            print "Campur gula dan tepung"

        def bakar_adonan(self):
            print "Bakar adonan"
            print "Kue siap"

    #buat sebuah objek 'Kue' bernama kueku
    kueku = Kue()

    #lakukan sesuatu atas kueku
    kueku.tambah_gula(100)
    kueku.tambah_tepung(1)
    kueku.campur_gula_tepung()
    kueku.bakar_adonan()

Nah, di sini kita membuat sebuah objek 'Kue' yang kita beri nama 'kueku' dan pembuatan kue dilakukan dengan memodifikasi atau melakukan 'sesuatu' terhadap 'kueku'

OOP Ala Python
--------------

Lanjut lagi ya... dalam Python semua objek memiliki atribut. Dan atribut dapat dipanggil atau diakses dengan::

    objek.atribut

Atribut dapat berupa 'data' ataupun 'method'. 
Data adalah atribut objek yang 'tidak melakukan sesuatu'.
Sedangkan 'method' adalah atribut objek yang 'melakukan sesuatu'.

Kembali ke contoh sebelumnya: objek 'kueku' memiliki 'data': 'tepung' dan 'gula' dan memiliki 'method': 'tambah_gula', 'tambah_tepung', 'campur_gula_tepung', 'bakar_adonan'.

Dua hal lain yang perlu dipahami di awal dalam pemrograman OOP ala Python:

* Class (kelas)
* Instance (instans)

Kelas adalah definisi atau abstraksi dari sebuah kelompok objek. Mengambil contoh Doni dan Budi. Doni dan Budi sama-sama manusia. Doni dan Budi sama-sama di-kelasifikasikan sebagai 'Manusia'. Dalam Python membuat sebuah class sangat gampang::

    class Manusia(object):
        pass

Nah, kita sudah punya sebuah kelas 'Manusia'. Kini, apa atribut dari manusia? Biasanya memiliki nama, umur, tinggi, berat. Dalam Python::

    class Manusia(object):
	nama = ""
	umur = 20
	tinggi = 160
	berat = 60


