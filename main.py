import PySimpleGUI as pg
from funct import *
from time import sleep
pg.theme('dark brown 6')
pg.set_options(font=("Courier New", 12))

anaEkran = [
    [pg.Text('Kütüphane Otomasyon Sistemine Hoşgeldiniz',)],
    [pg.Text('\n\n')],
    [pg.Text('Öğrenci Ekle')],
    [pg.Text('No Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Text('İsim Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Button('Öğrenci Ekle')],
    [pg.Text('\n')],
    [pg.Button('Öğrenci Bilgi Al')],
    [pg.Text('\n')],
    [pg.Text('Ödünç Kitap')],
    [pg.Text('No Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Text('Kitap ID Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Button('Ödünç Kitap Ver')],
    [pg.Text('\n')],
    [pg.Text('Kitap İade')],
    [pg.Text('Üye ID girin')],
    [pg.InputText(do_not_clear=False)],
    [pg.Text('Kitap ID Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Button('Kitap İade Al')],
    [pg.Text('\n\n\n\n\n')],
    [pg.Quit(button_text='Çıkış', button_color='red')]
]



prog = pg.Window('Kütüphane Otomasyon Sistemi', anaEkran,
                size=(1280, 1024), no_titlebar=True)


while True:
    try:
        event, values = prog.read()

        print('prog =', event, '\n' + str(values))


        if event == pg.WINDOW_CLOSED or event == 'Quit' or event == 'Çıkış':
            break
        if event == 'Öğrenci Ekle':
            uye_ekle(values[0], values[1])
        if event == 'Öğrenci Bilgi Al':
            no = False
            no = pg.popup_get_text('Öğrenci No girin', '', no_titlebar=True)

            if no != None:
                # 'Numara =', bilgi_cek(int(values[2]),'NUMARA') , 
                # '\nİsim =' , bilgi_cek(int(values[2]),'ISIM'), 
                # '\nÜyelik Tarihi =' , bilgi_cek(int(values[2]),'UYELIK_TARIHI') , 
                # '\nSon İşlem Tarihi =', bilgi_cek(int(values[2]),'SON_ISLEM_TARIHI') , 
                # '\nSon Alınan Kitap =' , bilgi_cek(int(values[2]),'SON_ALINAN_KITAP') , 
                # '\nSon Yapılan İşlem' , bilgi_cek(int(values[2]),'SON_YAPILAN_ISLEM')
                
                if bilgi_cek(int(no), 'ISIM') == "Aranan ID numarasına ait üye bulunamadı!":
                    pg.Popup("Bu Numaraya sahip öğrenci bulunamadı!", background_color="red", no_titlebar=True, button_color="red")
                    
                else:
                    pg.Popup('Numara =', bilgi_cek(int(values[2]), 'NUMARA'), 
                            '\nİsim =', bilgi_cek(int(values[2]), 'ISIM'), 
                            '\nÜyelik Tarihi =', bilgi_cek(int(values[2]), 'UYELIK_TARIHI'), 
                            '\nSon İşlem Tarihi =', bilgi_cek(int(values[2]), 'SON_ISLEM_TARIHI'), 
                            '\nSon Alınan Kitap =', bilgi_cek(int(values[2]), 'SON_ALINAN_KITAP'), 
                            '\nSon Yapılan İşlem', bilgi_cek(int(values[2]), 'SON_YAPILAN_ISLEM'), 
                            title=str(bilgi_cek(int(values[2]), 'ISIM')))
        if event == 'Ödünç Kitap Ver':
            son = kitap_al(values[3],values[2])
            if son == "Kitap ya da Üye meşgul yahut bulunamadı!":
                pg.Popup("Kitap ya da Üye meşgul yahut bulunamadı!")
        if event == 'Kitap İade Al':
            son = kitap_teslim_et(values[5], values[4])
            if son == "Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!":
                pg.Popup("Kitap ya da Üye bilgilerinin doğruluğunu kontrol ediniz!")
    except Exception as ex:
        print(ex)
        with open(DB.log, "w") as log:
            log.write(ex)
        yaz = "Bir Sorun Var! Lütfen Yazılımcıya Danışın!!!\n" + ex
        pg.Popup(yaz)
        pass