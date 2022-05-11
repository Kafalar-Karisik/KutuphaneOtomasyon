def warn(t:str, prnt:bool=True):
    G, B, R, W, P, C, end = '\033[92m', '\033[94m', '\033[91m', '\x1b[37m', '\x1b[35m', '\x1b[36m', '\033[0m'
    #Green,Blue,Red,White,Purple,Ciyan
    bilgi = end + W + "[-]" + W  # [-]
    iyi = end + G + "[+]" + C  # [+]
    uyarı = end + R + "[" + W + "!" + R + "]"  # [!]
    if prnt:
        print(uyarı , R + t + end)



try:
    from Docs import Vars as DB
except ModuleNotFoundError:
    warn("Önce Kurulum.py dosyasını Çalıştırmanız lazım.")
    exit()
from datetime import date

bugn = date.today() 
bugn = str(bugn.day) + "-" + str(bugn.month) + "-" + str(bugn.year)

sira = ('NUMARA','ISIM','UYELIK_TARIHI','SON_ISLEM_TARIHI','SON_ALINAN_KITAP','SON_YAPILAN_ISLEM')

kolon_bul = lambda kolon_adi:sira.index(kolon_adi)

ksira = ('ID','ADI','YAZAR','SAYFA_SAYISI','YAYINEVI','ALAN_UYE')

kkolon_bul = lambda kolon_adi:ksira.index(kolon_adi)


def bilgi_cek(id_no:int, kolon:str):
    dosya = open(DB.üye,encoding='utf-8')
    satirlar = dosya.readlines()
    dosya.close()

    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')

    
    for i in satirlar:
        if int(i[0]) == id_no:
            return i[kolon_bul(kolon)]
    
    return("Aranan ID numarasına ait üye bulunamadı!")
    
def kbilgi_cek(id_no:int, kolon:str):
    """'ID','ADI','YAZAR','SAYFA_SAYISI','YAYINEVI','ALAN_UYE'"""
    dosya = open(DB.kitap,encoding='utf-8')
    satirlar = dosya.readlines()
    dosya.close()

    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')

    
    for i in satirlar:
        if int(i[0]) == id_no:
            return i[kkolon_bul(kolon)]
    
    return("Aranan ID numarasına ait Kitap bulunamadı!")


def uye_ekle(no,isim):
    no,isim = str(no), str(isim)
    dosya = open(DB.üye,encoding='utf-8', mode='r')
    satirlar = dosya.readlines()
    dosya.close()
    
    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')
    uyelik_tarihi = bugn
    son_islem_tarihi = bugn
    son_yapilan_islem = "Kayıt Olundu"
    yeni_uye = [
        no,
        isim,
        uyelik_tarihi,
        son_islem_tarihi,
        '--',
        son_yapilan_islem
    ]

    text = ",".join(yeni_uye) + '\n'
    
    dosya = open(DB.üye,encoding='utf-8', mode='a')
    dosya.write(text)
    dosya.close()

    print('Üye işlemi tamamlandı!')


def kayit_dosyasi_olustur(dizin_yolu:str=DB.üye):
    dosya = open(dizin_yolu, 'x')
    text = "NUMARA,ISIM,UYELIK_TARIHI,SON_ISLEM_TARIHI,SON_ALINAN_KITAP,SON_YAPILAN_ISLEM"
    dosya.write(text+"\n")
    dosya.close()


def uye_sil(id_no:int):
    dosya = open(DB.üye,encoding='utf-8', mode='r')
    satirlar = dosya.readlines()
    dosya.close()
    
    satirlar.remove(satirlar[0])

    for indeks,i in enumerate(satirlar):
        satirlar[indeks] = i.split(',')
    
    yeni_liste = satirlar.copy()

    for i in satirlar:
        if id_no == int(i[0]):
            yeni_liste.remove(i)
            dosya = open(DB.üye, 'w',encoding='utf-8')
            kolonlar = "NUMARA,ISIM,UYELIK_TARIHI,SON_ISLEM_TARIHI,SON_ALINAN_KITAP,SON_YAPILAN_ISLEM"
            dosya.write(kolonlar + '\n')
            
            for i in yeni_liste:
                satir = ",".join(i)
                dosya.write(satir)
            
            dosya.close()
            return None
    
    print("Bu ID numarasına sahip üye bulunamadı!")


def kitaplik_olustur(dizin_yolu:str=DB.kitap):
    dosya = open(dizin_yolu , 'x')
    dosya.write('ID,ADI,YAZAR,SAYFA_SAYISI,YAYINEVI,ALAN_UYE\n')
    dosya.close()


def kitap_ekle(isim,yazar,sayfa_sayisi,yayinevi):
    dosya = open(DB.kitap, 'r', encoding='utf-8')
    satirlar = dosya.readlines()
    dosya.close()

    satirlar.remove(satirlar[0])

    if satirlar:
        for indeks,i in enumerate(satirlar):
            satirlar[indeks] = i.split(',')

        son_id = int(satirlar[-1][0])
    
    else:
        son_id = 0
    
    id_no = str(son_id + 1)
    sayfa_sayisi = str(sayfa_sayisi)

    kitap = [
        id_no,
        isim,
        yazar,
        sayfa_sayisi,
        yayinevi,
        '--' #Değiştirilen kısım burası. Yeni bir öğe ekleniyor.
    ]

    text = ','.join(kitap) + '\n'
    dosya = open(DB.kitap, 'a', encoding='utf-8')
    dosya.write(text)
    dosya.close()



def kitap_al(kitap_id, uye_id):
    # kitaplar ve üyeler veritabanını değişkenlere almalıyız.

    with open(DB.kitap, encoding='utf-8') as kitaplar:
        k_satirlar = kitaplar.readlines()
    
    with open(DB.üye, encoding='utf-8') as uyeler:
        u_satirlar = uyeler.readlines()

    kitap_flag = False
    uye_flag = False

    for indeks, i in enumerate(k_satirlar):
        k_satirlar[indeks] = i.split(',')

        i = i.split(",")
        if i[0] == str(kitap_id) and i[-1] == '--\n':
            kitap_flag = True

    #for indeks, i in enumerate(u_satirlar):
    #    u_satirlar[indeks] = i.split(',')
    #    
    #    if i[0] == str(uye_id) and i[-2] == '--':
    #        uye_flag = True
    for indeks, i in enumerate(u_satirlar):
        u_satirlar[indeks] = i.split(',')
    print(bilgi_cek(uye_id, "NUMARA") , str(uye_id) , bilgi_cek(uye_id, "SON_ALINAN_KITAP") , '--')
    print(str(bilgi_cek(uye_id, "NUMARA") == str(uye_id)) ,",", str(bilgi_cek(uye_id, "SON_ALINAN_KITAP") == '--'))
    
    
    if bilgi_cek(int(uye_id), "NUMARA") == str(uye_id) and bilgi_cek(int(uye_id), "SON_ALINAN_KITAP") == '--':
        uye_flag = True

    print(str(kitap_flag), str(uye_flag))
    
    if uye_flag and kitap_flag:

        for i in k_satirlar:
            if i[0] == str(kitap_id):
                i[-1] = str(uye_id) + '\n'  #!! Değişiklik burada yapıldı. kitaplar verisi değiştirildi
                break

        with open(DB.kitap, mode='w', encoding='utf-8') as kitaplar:
            for i in k_satirlar:  #!! değişiklik yapıldı
                kitaplar.write(",".join(i))  #kitaplar veritabanı değiştirildi
        
        with open(DB.üye, mode='w', encoding='utf-8') as uyeler:
            print(u_satirlar)
            print(type(u_satirlar))
            for i in u_satirlar:
                if i[0] == str(uye_id):
                    i[kolon_bul('SON_ALINAN_KITAP')] = str(kitap_id)
                    i[kolon_bul('SON_YAPILAN_ISLEM')] = "Kitap Alındı\n"
                    i[kolon_bul('SON_ISLEM_TARIHI')] = bugn
                    # Üyeler veritabanı değiştirldi
                uyeler.write(",".join(i))
    
    else:
        print("Kitap ya da Üye meşgul yahut bulunamadı!")
        return "Kitap ya da Üye meşgul yahut bulunamadı!"


def kitap_teslim_et(kitap_id, uye_id):

    with open(DB.kitap, encoding='utf-8') as kitaplar:
        k_satirlar = kitaplar.readlines()
    
    with open(DB.üye, encoding='utf-8') as uyeler:
        u_satirlar = uyeler.readlines()

    kitap_flag = False
    uye_flag = False

    for indeks, i in enumerate(k_satirlar):
        k_satirlar[indeks] = i.split(',')
        
    
    for indeks, i in enumerate(k_satirlar):
        if i[0] == str(kitap_id) and i[-1] == str(uye_id) +'\n': #değişiklik burada
            kitap_flag = True
            
    

    for indeks, i in enumerate(u_satirlar):
        u_satirlar[indeks] = i.split(',')
        
    for indeks, i in enumerate(u_satirlar):
        if i[0] == str(uye_id) and i[-2] == str(kitap_id):
            uye_flag = True
            

    
    if uye_flag and kitap_flag:

        for i in k_satirlar:
            if i[0] == str(kitap_id):
                i[-1] = '--' + '\n'  #değişiklik burada
                break

        with open(DB.kitap, mode='w', encoding='utf-8') as kitaplar:
            for i in k_satirlar:
                kitaplar.write(",".join(i))
        
        with open(DB.üye, mode='w', encoding='utf-8') as uyeler:
            for i in u_satirlar:
                if i[0] == str(uye_id):
                    i[kolon_bul('SON_ALINAN_KITAP')] = '--' #değişiklik burada
                    i[kolon_bul('SON_YAPILAN_ISLEM')] = "Kitap Teslim Edildi\n"  #değişiklik burada
                    i[kolon_bul('SON_ISLEM_TARIHI')] = bugn

                uyeler.write(",".join(i))
    
    else:
        print("Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!") #değişiklik burada
        return "Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!"