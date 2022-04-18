import PySimpleGUI as pg
from funct import *
from time import sleep
pg.theme('dark grey 12')
anaEkran = [
    [pg.Text('Kütüphane Otomasyon Sistemine Hoşgeldiniz ')],
    [pg.Text('\n\n')],
    [pg.Text('Üye Ekle')],
    [pg.Text('No Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Text('İsim Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Button('Üye Ekle')],
    [pg.Text('\n')],
    [pg.Text('Üye Bilgi')],
    [pg.Text('No Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Button('Bilgi Çek')],
    [pg.Quit(button_text='Çıkış', button_color='red')]
]


prog = pg.Window('Kütüphane Otomasyon Sistemi', anaEkran,
                 size=(1280, 1024), no_titlebar=True)


while True:
    event, values = prog.read()

    print('prog =', event, '\n' + str(values))

    if event == pg.WINDOW_CLOSED or event == 'Quit' or event == 'Çıkış':
        break
    if event == 'Üye Ekle':
        uye_ekle(values[0], values[1])
    if event == 'Bilgi Çek':
        #'Numara =', bilgi_cek(int(values[2]),'NUMARA') , '\nİsim =' , bilgi_cek(int(values[2]),'ISIM'), '\nÜyelik Tarihi =' , bilgi_cek(int(values[2]),'UYELIK_TARIHI') , '\nSon İşlem Tarihi =', bilgi_cek(int(values[2]),'SON_ISLEM_TARIHI') , '\nSon Alınan Kitap =' , bilgi_cek(int(values[2]),'SON_ALINAN_KITAP') , '\nSon Yapılan İşlem' , bilgi_cek(int(values[2]),'SON_YAPILAN_ISLEM')
        pg.Popup('Numara =', bilgi_cek(int(values[2]), 'NUMARA'), '\nİsim =', bilgi_cek(int(values[2]), 'ISIM'), '\nÜyelik Tarihi =', bilgi_cek(int(values[2]), 'UYELIK_TARIHI'), '\nSon İşlem Tarihi =', bilgi_cek(int(
            values[2]), 'SON_ISLEM_TARIHI'), '\nSon Alınan Kitap =', bilgi_cek(int(values[2]), 'SON_ALINAN_KITAP'), '\nSon Yapılan İşlem', bilgi_cek(int(values[2]), 'SON_YAPILAN_ISLEM'), no_titlebar=True, background_color="grey")
