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

prog = pg.Window('Kütüphane Otomasyon Sistemi', anaEkran, alpha_channel=1)
#uye = pg.Window('Üye İşlemleri', uyeIslemleri)
#ki = pg.Window('Kitap İşlemleri', kitapIslemleri)
#kti = pg.Window('Kitap Teslim İşlemleri', kitapTeslimIslemleri)

uye = pg.Window('Üye İşlemleri', [
    [pg.Text('Üye İşlemleri...'), pg.Text("\n\n\n")],
    [pg.Cancel("İptal")]
])
ki = pg.Window('Kitap İşlemleri', [
    [pg.Text('Kitap İşlemleri...'), pg.Text("\n\n\n")],
    [pg.Cancel("İptal")]
])
kti = pg.Window('Kitap Teslim İşlemleri', [
    [pg.Text('Kitap Teslim İşlemleri...'), pg.Text("\n\n\n")],
    [pg.Cancel("İptal")]
])

while True:
    event, values = prog.read()
    event1, values1 = uye.read()
    event2, values2 = ki.read()
    event3, values3 = kti.read()

    print("prog =" , event , values , "\nuye =" , event1 , values1 ,  "\nki = " , event2 , values2 , "\nddkti = " , event3 , values3)

    if event == pg.WINDOW_CLOSED or event == "Quit":
        break

    if event == "Üye İşlemleri":
        uye.un_hide()
        if event1 == pg.WINDOW_CLOSED:
            uye.hide()
    
    if event == "Kitap İşlemleri":
        ki.un_hide()
        if event2 == pg.WINDOW_CLOSED:
            ki.hide()

    if event == "Kitap Teslim İşlemleri":
        kti.un_hide()
        if event3 == pg.WINDOW_CLOSED:
            kti.hide()