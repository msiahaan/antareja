filelist = ['pengantar','memulai','komentar','bilangan_variabel', 'while_if',
            'list_tuple']

print "Buka file tujuan"
dest = open('python-di-windows.rst', 'w')

for name in filelist:
    filename = name + '.rst'
    print "Memproses %r..." % filename
    source = open(filename, 'r')
    for text in source:
        dest.write(text)
    source.close()

dest.close()
print "Selesai!"