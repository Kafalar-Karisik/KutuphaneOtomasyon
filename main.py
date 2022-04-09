import PySimpleGUI as pg
from funct import *
pg.theme('dark grey 12')
anaEkran = [
    [pg.Text('Kütüphane Otomasyon Sistemine Hoşgeldiniz ')],
    [pg.Text('\n\n\n')],
    [pg.Text('Lütfen Yapmak istediğiniz işlemi seçiniz !!')],
    [pg.Button("Üye İşlemleri"), pg.Button("Kitap İşlemleri"), pg.Button("Kitap Teslim İşlemleri")],
    [pg.Quit(button_text="Çıkış",button_color="red")]
]

uyeIslemleri = [
    [pg.Text('Üye İşlemleri...'), pg.Text("\n\n\n")],
    [pg.Cancel("İptal")]
]
kitapIslemleri = [
    [pg.Text('Kitap İşlemleri...'), pg.Text("\n\n\n")],
    [pg.Cancel("İptal")]
]
kitapTeslimIslemleri = [
    [pg.Text('Kitap Teslim İşlemleri...'), pg.Text("\n\n\n")],
    [pg.Cancel("İptal")]
]

prog = pg.Window('Kütüphane Otomasyon Sistemi', anaEkran)

while True:
    event, values = prog.read()

    if event == pg.WINDOW_CLOSED or event == "Çıkış":
        break

    if event == "Üye İşlemleri":
        uye = pg.Window('Üye İşlemleri', uyeIslemleri,)
        event1, values1 = uye.read()
        if event1 == pg.WINDOW_CLOSED:
            uye.Close()
    

    if event == "Kitap İşlemleri":
        uye = pg.Window('Kitap İşlemleri', kitapIslemleri)
        event2, values2 = uye.read()
        if event2 == pg.WINDOW_CLOSED:
            kitapIslemleri.Close()

    if event == "Kitap Teslim İşlemleri":
        uye = pg.Window('Kitap Teslim İşlemleri', kitapTeslimIslemleri)
        event3, values3 = uye.read()
        if event3 == pg.WINDOW_CLOSED:
            kitapTeslimIslemleri.Close()