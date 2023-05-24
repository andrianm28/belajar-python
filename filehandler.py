print("Melihat file konfigurasi 1: ")
f1 = open("files/config1.txt", "r")
print(f1.read())
f1.close()

print("menuliskan konfigurasi baru")
f2 = open("files/config2.txt", "w")
f2.write("ini adalah konfigurasi kedua")
f2.close()