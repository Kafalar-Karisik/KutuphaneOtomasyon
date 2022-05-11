from os import system as sys

try:
    import PySimpleGUI as pg
except:
    try:
        sys("python3 -m pip install PySimpleGUI")
    except:
        try:
            sys("python -m pip install PySimpleGUI")
        except:
            print(ModuleNotFoundError("PySimpleGUI Kütüphanesini Yükleyin!!!"))
            exit()
from funct import *
from events import *

pg.theme('dark brown 6')
pg.set_options(font=('Courier New', 10))

anaEkran = [
    [pg.Text('Kütüphane Otomasyon Sistemine Hoşgeldiniz', font=12)],
    [pg.Text('\n')],
    [pg.Text('Öğrenci Ekle')],
    [pg.Text('No Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Text('İsim Girin:')],
    [pg.InputText(do_not_clear=False)],
    [pg.Button('Öğrenci Ekle')],
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
    [pg.Button('Kitap Bilgi Al')],
    [pg.Text('\n')],
    [pg.Quit(button_text='Çıkış', button_color='red',)]
]


prog = pg.Window('Kütüphane Otomasyon Sistemi', anaEkran,
                finalize=True, 
                #no_titlebar=True,
                use_custom_titlebar=True,
                icon="icon.ico",
                grab_anywhere=True)
prog.TKroot.wm_overrideredirect(True)

while True:
    try:
        prog.Maximize()
        event, values = prog.read()
        print('prog =', event, '\n' + str(values))


        if event == 'Öğrenci Ekle':
            uye_ekle(values[0], values[1])
        if event == 'Öğrenci Bilgi Al':
            Öğrenci_Bilgi_Al()
        if event == 'Ödünç Kitap Ver':
            Ödünç_Kitap_Ver()
        if event == 'Kitap İade Al':
            Kitap_İade_Al()
        if event == 'Kitap Bilgi Al':
            Kitap_Bilgi_Al()
        if event == 'Ödünç Kitap Ver':
            Ödünç_Kitap_Ver()
        if event == 'Kitap İade Al':
            Kitap_İade_Al()


        if event == pg.WINDOW_CLOSED or event == 'Quit' or event == 'Çıkış':
            break
    except Exception as ex:
        print(ex)
        ex = str(ex)
        with open(DB.log, 'a+') as log:
            log.write(ex + '\n')
        yaz = 'Bir Sorun Var! Lütfen Yazılımcıya Danışın!!!\n' + ex + '\n'
        pg.Popup(yaz)
        pass
