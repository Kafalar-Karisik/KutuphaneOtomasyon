import os
yol = input("Lütfen DataBase lerin Bulunmasını istediğiniz Dosya Yolunu Giriniz\n----> ")
yol = yol.replace("\\", "/")
üyeyol = yol + "/uyeler.csv"
kitapyol = yol + "/kitaplar.csv"
logyol = yol + "/hata.log"
try:
    os.mkdir("Docs")
except:
    pass
try:
    dosya = open("Docs/Vars.py", "a+", encoding="utf-8")
    dosya.write("üye = '" + üyeyol + "'\nkitap = '" +
                kitapyol + "'\nlog = '" + logyol + "'\n")
except:
    pass
try:
    with open(üyeyol, 'x') as dosya:
        text = "NUMARA,ISIM,UYELIK_TARIHI,SON_ISLEM_TARIHI,SON_ALINAN_KITAP,SON_YAPILAN_ISLEM"
        dosya.write(text+"\n")
except:
    pass
try:
    with open(kitapyol, 'x') as dosya:
        dosya.write('ID,ADI,YAZAR,SAYFA_SAYISI,YAYINEVI,ALAN_UYE\n')
except:
    pass
try:
    with open(logyol, 'x') as dosya:
        pass
except:
    pass
