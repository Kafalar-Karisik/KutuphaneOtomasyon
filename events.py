from funct import *
from main import *

def Öğrenci_Ekle():
    uye_ekle(values[0], values[1])
#----------------------------------------------------------------------------------------------#
################################################################################################
#______________________________________________________________________________________________#
def Öğrenci_Bilgi_Al():
    no = False
    no = pg.popup_get_text('Öğrenci No girin', '', no_titlebar=True)

    if no != None:
        try:
            no = int(no)
        except:
            pg.Popup('Lütfen Geçerli Bir Numara Giriniz',
                        background_color="red", no_titlebar=True)
            pass
        if bilgi_cek(int(no), 'ISIM') == 'Aranan ID numarasına ait üye bulunamadı!':
            pg.Popup('Bu Numaraya sahip öğrenci bulunamadı!',
                        background_color='red', no_titlebar=True, button_color='red')

        else:

            pg.Popup('Numara =', bilgi_cek(no, 'NUMARA'),
                        '\nİsim =', bilgi_cek(no, 'ISIM'),
                        '\nÜyelik Tarihi =', bilgi_cek(
                            no, 'UYELIK_TARIHI'),
                        '\nSon İşlem Tarihi =', bilgi_cek(
                            no, 'SON_ISLEM_TARIHI'),
                        '\nSon Alınan Kitap =', bilgi_cek(
                            no, 'SON_ALINAN_KITAP'),
                        '\nSon Yapılan İşlem', bilgi_cek(
                            no, 'SON_YAPILAN_ISLEM'),
                        title=str(bilgi_cek(no, 'ISIM')))
#----------------------------------------------------------------------------------------------#
################################################################################################
#______________________________________________________________________________________________#
def Ödünç_Kitap_Ver():
    son = kitap_al(values[3], values[2])
    if son == 'Kitap ya da Üye meşgul yahut bulunamadı!':
        pg.Popup('Kitap ya da Üye meşgul yahut bulunamadı!')
#----------------------------------------------------------------------------------------------#
################################################################################################
#______________________________________________________________________________________________#
def Kitap_İade_Al():
    son = kitap_teslim_et(values[5], values[4])
    if son == 'Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!':
        pg.Popup(
            'Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!')
#----------------------------------------------------------------------------------------------#
################################################################################################
#______________________________________________________________________________________________#
def Kitap_Bilgi_Al():
    no = False
    no = pg.popup_get_text('Kitap No girin', '', no_titlebar=True, background_color="grey")

    if no != None:

        try:
            no = int(no)
        except:
            pg.Popup('Lütfen Geçerli Bir Numara Giriniz',
                        background_color="red", no_titlebar=True)
            pass
        if kbilgi_cek(no, 'ADI') == 'Aranan ID numarasına ait Kitap bulunamadı!':
            pg.Popup('Bu Numaraya sahip Kitap bulunamadı!',
                        background_color='red', no_titlebar=True, button_color='red')

        else:

            pg.Popup('Numara =', kbilgi_cek(no, 'ID'),
                        '\nYAZAR =', kbilgi_cek(no, 'YAZAR'),
                        '\nSAYFA SAYISI =', kbilgi_cek(no, 'SAYFA_SAYISI'),
                        '\nYAYINEVİ =', kbilgi_cek(no, 'YAYINEVI'),
                        '\nALAN ÜYE', kbilgi_cek(no, 'ALAN_UYE'),
                        title=str(kbilgi_cek(no, 'ADI')), background_color="grey", no_titlebar=True)
#----------------------------------------------------------------------------------------------#
################################################################################################
#______________________________________________________________________________________________#
def Ödünç_Kitap_Ver():
    son = kitap_al(values[3], values[2])
    if son == 'Kitap ya da Üye meşgul yahut bulunamadı!':
        pg.Popup('Kitap ya da Üye meşgul yahut bulunamadı!')
#----------------------------------------------------------------------------------------------#
################################################################################################
#______________________________________________________________________________________________#
def Kitap_İade_Al():
    son = kitap_teslim_et(values[5], values[4])
    if son == 'Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!':
        pg.Popup(
            'Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!')
