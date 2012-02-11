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

Kita definisikan kelas Manusia dengan atribut nama, umur, tinggi, berat. Atribut perlu kita definisikan nilai sementaranya. Tenang, nanti bisa diubah kok!

Berikutnya Instance (Instans) adalah objek bagian program kita yang merupakan perwakilan dari kelompok objek yang didefinisikan dalam class.
Contohnya Budi. Dalam Python::

    #buat objek 'budi' sebagai instance dari class 'Manusia'
    budi = Manusia()

Kembali ke contoh di atas. Instance adalah objek dalam program kita dan sebetulnya atribut instance lah yang kita 'permainkan'. Nah untuk dapat melakukan 'sesuatu' atas variabel instance, kita perlu melakukan perubahan dalam definisi kelas kita.:: 

    >>> class Manusia(object):
     	nama = ""
        umur = 1
        tinggi = 160
        berat = 60
        
        def set_nama(self, namanya):
            nama = namanya
            
    >>> budi = Manusia()
    >>> budi.set_nama("Budi")
    >>> budi.nama
    ''
    >>>

Kita mencoba untuk mengubah nama objek budi menjadi "Budi" namun gatot. Atribut nama tetap bernilai ' '.

Untuk itulah kita perlu menggunakan sebuah argumen spesial yang biasanya dinamai 'self'. Argumen 'self' merupakan referensi ke instans dari kelas. Dalam bahasa pemrograman lain, 'self' dapat disetarakan dengan 'this'. Nah, contohnya::

    >>> class Manusia(object):
        def set_nama(self, namanya):
            self.nama = namanya 
        
        def set_umur(self, umurnya): 
            self.umur = umurnya 
        
        def set_tinggi(self, tingginya): 
            self.tinggi = tingginya 
            
        def set_berat(self, beratnya):
            self.berat = beratnya

    >>> budi = Manusia()
    >>> budi.set_nama('Budi')
    >>> budi.nama
    'Budi'
    >>>

Nah, kita definisikan class Manusia. Buat instans 'budi' dan kemudian mengubah atribut 'nama' dari 'budi' dengan memanggil method 'set_nama'


Pewarisan (Inheritance)
-----------------------

Sudah disebutkan bahwa setiap objek memiliki atribut. Atribut itu dapat didefinisikan dalam kelas yang kita ciptakan atau dapat di-'warisi' dari kelas induk. Sebagai contoh kembali ke contoh Budi yang adalah pemain bola. Pemain bola adalah juga manusia, sehingga kita dapat mendefinisikan kelas PemainBola sebagai anak dari kelas Manusia::

    class Manusia(object):
        
        def set_nama(self, namanya):
            self.nama = namanya
            
        def set_umur(self, umurnya):
            self.umur = umurnya
            
        def set_tinggi(self, tingginya):
            self.tinggi = tingginya
            
        def set_berat(self, beratnya):
            self.berat = beratnya
            
            
    class PemainBola(Manusia):
       
        def tendang_bola(self):
            print '%s menendang bola" % self.nama

kemudian penggunaannya::

    >>> budi = PemainBola()
    >>> budi.set_nama("Budi")
    >>> budi.tendang_bola()
    Budi menendang bola
    >>>

Kita membuat objek 'budi' sebagai instans dari PemainBola. Nah sebagai seorang pemain bola, Budi memiliki method 'tendang_bola' dan juga mewarisi atribut-atribut dari kelas Manusia seperti nama, umur, tinggi, berat. Kelas Manusia adalah induk dari kelas PemainBola. Dalam Python, untuk mendefinisikan suatu kelas yang mewarisi atribut dari kelas lainnya::
    
    class KelasAnak(KelasInduk):
        ...
        atribut-atribut KelasAnak
        ...

__init__
---------

Class dalam python dapat memiliki atribut berupa 'method' yang merupakan fungsi yang 'melakukan sesuatu'. Method mendapat masukan berupa argumen-argumen dan biasanya 'self' merupakan salah satu argumen. Salah satu method yang 'spesial' dalam python adalah __init__.

__init__ adalah method yang secara otomatis dipanggil saat program kita membuat instans dari kelas tersebut. Dalam bahasa pemrograman lain, __init__ dapat disetarakan walau tidak sama persis dengan 'konstruktor'. __init__ seringkali digunakan untuk memberikan 'initial value' untuk variabel atribut dari kelas tersebut. 

Kembali ke contoh Manusia kita. Kita ingin minimal seorang manusia memiliki nama, maka::

    class Manusia(object):

        def __init__(self, namanya):
            self.nama = namanya

        def set_umur(self, umurnya):
            self.umur = umurnya
            
        def set_tinggi(self, tingginya):
            self.tinggi = tingginya
            
        def set_berat(self, beratnya):
            self.berat = beratnya


    class PemainBola(Manusia):

       def tendang_bola(self):
           print '%s menendang bola" % self.nama
      

kemudian kita buat kelas PemainBola sebagai turunan dari kelas Manusia. Maka penggunaannya dalam program kita::

    >>> budi = PemainBola("Budi")
    >>> budi.tendang_bola()
    Budi menendang bola
    >>>


Polimorfisme
------------

Polimorfisme: banyak bentuk. Dalam pemrograman OOP polimorfisme dilakukan apabila kelas anak menggunakan nama method yang sama dengan na a method kelas induk namun dengan implementasi berbeda. Dalam pemrograman OOP umumnya dikenal 2 bentuk polimorfisme:
Overloading: kelas anak menggunakan nama method yang sama namun tipe dan jumlah argumen berbeda.
Overriding: kelas anak mendifinisikan ulang method dari kelas induk

Dalam python, berbeda dengan bahasa pemrograman lain, hanya mengenal overriding. Overloading dilakukan dengan pendekatan menggunakan 'keyword' sebagai argumen.

Contoh::

    class Manusia(object):
        
        def __init__(self, namanya):
            self.nama = namanya
            
        def set_umur(self, umurnya):
            self.umur = umurnya


    class PemainBola(Manusia):
        
        def __init__(self, posisi):
            self.posisi = posisi

maka jika kita ingin membuat instans budi::

    >>> budi = PemainBola("Budi", "Striker")
    Traceback (most recent call last):
    File "", line 1, in 
    budi = PemainBola("Budi", "Striker")
    TypeError: __init__() takes exactly 2 arguments (3 given)

muncul pesan kesalahan. Yang betul::
    
    >>> budi = PemainBola("Striker")

Nah, kita mendefinisikan ulang method __init__ dalam kelas PemainBola, dan saat kita membuat instans 'budi' dengan memasukkan nama dan posisi, ternyata error. Mengapa? Karena method __init__ dalam kelas PemainBola hanya menerima 2 argumen: self, dan posisi. Method __init__ kelas anak (PemainBola) meng-override method __init__ kelas induk. Lalu bagaimana dong?

Solusinya: dalam definisi method __init__ kelas anak (PemainBola), kita panggil dulu method __init__ dari kelas induk (Manusia)::

    class PemainBola(Manusia):
    
        def __init__(self, nama, posisi):
            Manusia.__init__(self, nama)
            self.posisi = posisi

dan contoh penggunaannya
::

    >>> budi = PemainBola("Budi", "Striker")
    >>> budi.nama
    'Budi'
    >>> budi.posisi
    'Striker'


