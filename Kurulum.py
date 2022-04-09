from main import *
yol = input("Lütfen DataBase lerin Bulunmasını istediğiniz Dosya Yolunu Giriniz\n----> ")
yol = yol.replace("\\", "/")
üyeyol = yol + "/uyeler.csv"
kitapyol = yol + "/kitaplar.csv"


dosya = open("Docs/Vars.py", "a+", encoding="utf-8")
dosya.write("üye = '" + üyeyol + "'\nkitap = '" + kitapyol + "'\n")

kayit_dosyasi_olustur()
kitaplik_olustur()