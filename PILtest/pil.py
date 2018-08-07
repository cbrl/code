#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import subprocess
import Tkinter as Tki



global linijkaa
linijkaa = 0

def generujidrukuj():
    info.set("Renderowanie etykiety...")
    inforamka.update_idletasks()
    
    numerleku = e12.get()
    nazwapacjenta = e13.get()

    skladnik_1 = e0.get()
    skladnik_2 = e1.get()
    skladnik_3 = e2.get()
    skladnik_4 = e3.get()
    skladnik_5 = e4.get()
    skladnik_6 = e5.get()
    skladnik_7 = e6.get()
    skladnik_8 = e7.get()

    ilosc_1 = en0.get()
    ilosc_2 = en1.get()
    ilosc_3 = en2.get()
    ilosc_4 = en3.get()
    ilosc_5 = en4.get()
    ilosc_6 = en5.get()
    ilosc_7 = en6.get()
    ilosc_8 = en7.get()

    sposob_1 = e8.get()
    sposob_2 = e9.get()
    sposob_3 = e10.get()
    sposob_4 = e11.get()

    lekarz = e14.get()
    data = e15.get()


    img = Image.open("etyk_zew.png")
    fnt = ImageFont.truetype("/home/pi/Desktop/PILtest/font.ttf", 160)
    fnt2 = ImageFont.truetype("/home/pi/Desktop/PILtest/font.ttf", 50)
    fnt3 = ImageFont.truetype("/home/pi/Desktop/PILtest/font.ttf", 40)
    fnt4 = ImageFont.truetype("/home/pi/Desktop/PILtest/font.ttf", 25)

    d = ImageDraw.Draw(img)

    d.text((180,190), numerleku , font=fnt, fill=(0, 0, 0))
    d.text((10,410), nazwapacjenta , font=fnt2, fill=(255, 255, 255))
    d.text((15,650), skladnik_1 , font=fnt3, fill=(0, 0, 0))
    d.text((15,700), skladnik_2 , font=fnt3, fill=(0, 0, 0))
    d.text((15,750), skladnik_3 , font=fnt3, fill=(0, 0, 0))
    d.text((15,800), skladnik_4 , font=fnt3, fill=(0, 0, 0))
    d.text((15,850), skladnik_5 , font=fnt3, fill=(0, 0, 0))
    d.text((15,900), skladnik_6 , font=fnt3, fill=(0, 0, 0))
    d.text((15,950), skladnik_7 , font=fnt3, fill=(0, 0, 0))
    d.text((15,1000), skladnik_8 , font=fnt3, fill=(0, 0, 0))

    d.text((516,650), ilosc_1 , font=fnt3, fill=(0, 0, 0))
    d.text((516,700), ilosc_2 , font=fnt3, fill=(0, 0, 0))
    d.text((516,750), ilosc_3 , font=fnt3, fill=(0, 0, 0))
    d.text((516,800), ilosc_4 , font=fnt3, fill=(0, 0, 0))
    d.text((516,850), ilosc_5 , font=fnt3, fill=(0, 0, 0))
    d.text((516,900), ilosc_6 , font=fnt3, fill=(0, 0, 0))
    d.text((516,950), ilosc_7 , font=fnt3, fill=(0, 0, 0))
    d.text((516,1000), ilosc_8 , font=fnt3, fill=(0, 0, 0))

    d.text((15,1335), sposob_1 , font=fnt4, fill=(0, 0, 0))
    d.text((15,1361), sposob_2 , font=fnt4, fill=(0, 0, 0))
    d.text((15,1387), sposob_3 , font=fnt4, fill=(0, 0, 0))
    d.text((15,1413), sposob_4 , font=fnt4, fill=(0, 0, 0))

    d.text((80,1460), lekarz , font=fnt3, fill=(0, 0, 0))
    d.text((200,1543), data , font=fnt2, fill=(0, 0, 0))
    img.save("/ramfs/wygenerowana_etykieta.png")
    info.set("Generowanie pliku dla drukarki...")
    inforamka.update_idletasks()
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/wygenerowana_etykieta.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    info.set("Zakończono.")
    return

def linijka(ktora):
    global linijkaa
    linijkaa=ktora
    return
    
def wsadz_tekst(tekst):
    global linijkaa
    if linijkaa==0:
        e0.delete(0, "end")
        e0.insert(0, tekst)
    if linijkaa==1:
        e1.delete(0, "end")
        e1.insert(0, tekst)
    if linijkaa==2:
        e2.delete(0, "end")
        e2.insert(0, tekst)
    if linijkaa==3:
        e3.delete(0, "end")
        e3.insert(0, tekst)
    if linijkaa==4:
        e4.delete(0, "end")
        e4.insert(0, tekst)
    if linijkaa==5:
        e5.delete(0, "end")
        e5.insert(0, tekst)
    if linijkaa==6:
        e6.delete(0, "end")
        e6.insert(0, tekst)
    if linijkaa==7:
        e7.delete(0, "end")
        e7.insert(0, tekst)
    if linijkaa==8:
        e8.delete(0, "end")
        e8.insert(0, tekst)
    if linijkaa==9:
        e9.delete(0, "end")
        e9.insert(0, tekst)
    if linijkaa==10:
        e10.delete(0, "end")
        e10.insert(0, tekst)
    if linijkaa==11:
        e11.delete(0, "end")
        e11.insert(0, tekst)
    if linijkaa==12:
        e12.delete(0, "end")
        e12.insert(0, tekst)
    if linijkaa==13:
        e13.delete(0, "end")
        e13.insert(0, tekst)
    if linijkaa==14:
        e14.delete(0, "end")
        e14.insert(0, tekst)
    if linijkaa==15:
        e15.delete(0, "end")
        e15.insert(0, tekst)
    return

root=Tki.Tk()
root.title("CL")
root.geometry("1280x800")
root.configure(background='black')

cyberl = Tki.PhotoImage(file="/home/pi/Desktop/PILtest/cyberl.png")

ramkalewa = Tki.Frame(bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkalewa.pack(side="left", expand="yes", fill="both")
ramkasrod = Tki.Frame(bg="purple4", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkasrod.pack(side="left", expand="yes", fill="both")
ramkaprawa = Tki.Frame(bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkaprawa.pack(side="left", expand="yes", fill="both")

ramkalewagorna = Tki.Frame(ramkalewa, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkalewasrodk = Tki.Frame(ramkalewa, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkalewadolna = Tki.Frame(ramkalewa, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkalewagorna.pack(side="top", expand="yes", fill="both")
ramkalewasrodk.pack(side="top", expand="yes", fill="both")
ramkalewadolna.pack(side="top", expand="yes", fill="both")

ramkaprawagorna = Tki.Frame(ramkaprawa, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkaprawasrodk = Tki.Frame(ramkaprawa, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkaprawadolna = Tki.Frame(ramkaprawa, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkaprawagorna.pack(side="top", expand="yes", fill="both")
ramkaprawasrodk.pack(side="top", expand="yes", fill="both")
ramkaprawadolna.pack(side="top", expand="yes", fill="both")

infotext0 = Tki.Message(ramkalewagorna, text="PODŁOŻA MAŚCIOWE", width=200, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext1 = Tki.Message(ramkalewasrodk, text="PŁYNY", width=200, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext2 = Tki.Message(ramkalewadolna, text="WITAMINY", width=200, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext3 = Tki.Message(ramkaprawagorna, text="STAŁE II", width=200, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext4 = Tki.Message(ramkaprawasrodk, text="PACJENCI", width=200, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext5 = Tki.Message(ramkaprawadolna, text="M.F.", width=200, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext0.pack(side="top", expand="yes", fill="x")
infotext1.pack(side="top", expand="yes", fill="x")
infotext2.pack(side="top", expand="yes", fill="x")
infotext3.pack(side="top", expand="yes", fill="x")
infotext4.pack(side="top", expand="yes", fill="x")
infotext5.pack(side="top", expand="yes", fill="x")



p0 = Tki.Button(ramkalewagorna, bg="snow", width=10, height= 2, text="Eucerini", command=lambda:wsadz_tekst("Eucerini"))
p0.pack(side="top")
p1 = Tki.Button(ramkalewagorna, bg="snow", width=10, height= 2, text="Hascobaza", command=lambda:wsadz_tekst("Hascobaza"))
p1.pack(side="top")
p2 = Tki.Button(ramkalewagorna, bg="snow", width=10, height= 2, text="Lanolini", command=lambda:wsadz_tekst("Lanolini"))
p2.pack(side="top")
p3 = Tki.Button(ramkalewagorna, bg="snow", width=10, height= 2, text="Vaselini albi", command=lambda:wsadz_tekst("Vaselini albi"))
p3.pack(side="top")
p4 = Tki.Button(ramkalewagorna, bg="snow", width=10, height= 2, text="Vaselini flavi", command=lambda:wsadz_tekst("Vaselini flavi"))
p4.pack(side="top")
p5 = Tki.Button(ramkalewagorna, bg="snow", width=10, height= 2, text="Vaselini hydrof.", command=lambda:wsadz_tekst("Vaselini hydrofilici"))
p5.pack(side="top")

####################plyny:
p6 = Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Agua dest.", command=lambda:wsadz_tekst("Aqua destilata"))
p6.pack(side="top")
p7 = Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Ethanoli 70 st.", command=lambda:wsadz_tekst("Ethanoli 70 st."))
p7.pack(side="top")
p8 = Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Ethanoli 96 st.", command=lambda:wsadz_tekst("Ethanoli 96 st."))
p8.pack(side="top")
p9 = Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Glicerol 85%", command=lambda:wsadz_tekst("Glicerol 85%"))
p9.pack(side="top")
p10= Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Oleum ricini", command=lambda:wsadz_tekst("Oleum ricini"))
p10.pack(side="top")
p11 = Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Paraffini liq.", command=lambda:wsadz_tekst("Paraffini liq."))
p11.pack(side="top")
p12 = Tki.Button(ramkalewasrodk, bg="sky blue", width=10, height= 2, text="Perhydrol 30%", command=lambda:wsadz_tekst("Perhydrol 30%"))
p12.pack(side="top")
####################subst stałe1:
p13 = Tki.Button(ramkalewadolna, bg="yellow", width=10, height= 2, text="Vitaminum A", command=lambda:wsadz_tekst("Vitaminum A"))
p13.pack(side="top")
p14 = Tki.Button(ramkalewadolna, bg="yellow", width=10, height= 2, text="Vitaminum E", command=lambda:wsadz_tekst("Vitaminum E"))
p14.pack(side="top")
p15 = Tki.Button(ramkalewadolna, bg="yellow", width=10, height= 2, text="Vit. A+D liq.", command=lambda:wsadz_tekst("Vitaminum A+D liq."))
p15.pack(side="top")
p16 = Tki.Button(ramkalewadolna, bg="yellow", width=10, height= 2, text="Vitaminum D", command=lambda:wsadz_tekst("Vitaminum D"))
p16.pack(side="top")
####################subst stałe2:
p17 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Benzocaini", command=lambda:wsadz_tekst("Benzocaini"))
p17.pack(side="top")
p18 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Cygnolini", command=lambda:wsadz_tekst("Cygnolini"))
p18.pack(side="top")
p19 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Detreomycini", command=lambda:wsadz_tekst("Detreomycini"))
p19.pack(side="top")
p20 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Hydrocortisoni", command=lambda:wsadz_tekst("Hydrocortisoni"))
p20.pack(side="top")
p21 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Kalii iod.", command=lambda:wsadz_tekst("Kalii iodati"))
p21.pack(side="top")
p22 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Mentholi", command=lambda:wsadz_tekst("Mentholi"))
p22.pack(side="top")
p23 = Tki.Button(ramkaprawagorna, bg="LightPink1", width=10, height= 2, text="Procaini", command=lambda:wsadz_tekst("Procaini"))
p23.pack(side="top")
################# misce fiat:
p24 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.glob.vag.", command=lambda:wsadz_tekst("M. f. glob. vag."))
p24.pack(side="top")
p25 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.gtt.", command=lambda:wsadz_tekst("M. f. gtt."))
p25.pack(side="top")
p26 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.mixt.", command=lambda:wsadz_tekst("M. f. mixt."))
p26.pack(side="top")
p27 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.pulv.", command=lambda:wsadz_tekst("M. f. pulv."))
p27.pack(side="top")
p28 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.sol.", command=lambda:wsadz_tekst("M. f. sol."))
p28.pack(side="top")
p29 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.susp.", command=lambda:wsadz_tekst("M. f. susp."))
p29.pack(side="top")
p30 = Tki.Button(ramkaprawadolna, bg="green yellow", width=10, height= 2, text="M.f.ung.", command=lambda:wsadz_tekst("M. f. ung."))
p30.pack(side="top")
################# pacjenci:
p31 = Tki.Button(ramkaprawasrodk, bg="thistle4", width=10, height= 2, text="K.Kowalski", command=lambda:wsadz_tekst("Krzysztof Kowalski"))
p31.pack(side="top")
p32 = Tki.Button(ramkaprawasrodk, bg="thistle4", width=10, height= 2, text="R.Barańczak", command=lambda:wsadz_tekst("Robert Barańczak"))
p32.pack(side="top")
p33 = Tki.Button(ramkaprawasrodk, bg="thistle4", width=10, height= 2, text="W.Putin", command=lambda:wsadz_tekst("Włodzimierz Putin"))
p33.pack(side="top")

##############################predef:
def czyscpola():
    e0.delete(0, "end")
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")
    e7.delete(0, "end")
    e8.delete(0, "end")
    e9.delete(0, "end")
    e10.delete(0, "end")
    e11.delete(0, "end")
    e12.delete(0, "end")
    e13.delete(0, "end")
    e14.delete(0, "end")
    e15.delete(0, "end")
    en0.delete(0, "end")
    en1.delete(0, "end")
    en2.delete(0, "end")
    en3.delete(0, "end")
    en4.delete(0, "end")
    en5.delete(0, "end")
    en6.delete(0, "end")
    en7.delete(0, "end")
    return

def zaladujrp1():
    czyscpola()
    e0.insert(0, "Lanolini")
    e1.insert(0, "Vaselini albi")
    e2.insert(0, "Paraffini liq.")
    e3.insert(0, "Aqua aa ad.")
    e4.insert(0, "M. f. ung.")
    e5.insert(0, "")
    e6.insert(0, "")
    e7.insert(0, "")
    
    en0.insert(0, "")
    en1.insert(0, "")
    en2.insert(0, "")
    en3.insert(0, "  100.0")
    en4.insert(0, "")
    en5.insert(0, "")
    en6.insert(0, "")
    en7.insert(0, "")
    
    e8.insert(0, "Smarować pupę.")
    e9.insert(0, "")
    e10.insert(0, "")
    e11.insert(0, "")
    e12.insert(0, "")
    e13.insert(0, "")
    e14.insert(0, "")
    e15.insert(0, "")
    return
    
def zaladujrp2():
    czyscpola()
    e0.insert(0, "Eucerini")
    e1.insert(0, "Vaselini albi")
    e2.insert(0, "Aquae aa ad.")
    e3.insert(0, "M. f. ung.")
    e4.insert(0, "")
    e5.insert(0, "")
    e6.insert(0, "")
    e7.insert(0, "")
    
    en0.insert(0, "")
    en1.insert(0, "")
    en2.insert(0, "  200.0")
    en3.insert(0, "")
    en4.insert(0, "")
    en5.insert(0, "")
    en6.insert(0, "")
    en7.insert(0, "")
    
    e8.insert(0, "Smarować się z rana i z wieczora.")
    e9.insert(0, "Codziennie.")
    e10.insert(0, "")
    e11.insert(0, "")
    e12.insert(0, "")
    e13.insert(0, "")
    e14.insert(0, "")
    e15.insert(0, "")
    return
    
def zaladujrp3():
    czyscpola()
    e0.insert(0, "Detreomycini")
    e1.insert(0, "Hydrocortisoni")
    e2.insert(0, "Benzocaini")
    e3.insert(0, "Acidi borici")
    e4.insert(0, "Vit.A liq.")
    e5.insert(0, "Nystatyni")
    e6.insert(0, "Eucerini ad.")
    e7.insert(0, "M. f. ung.")
    
    en0.insert(0, "    4.0")
    en1.insert(0, "    2.0")
    en2.insert(0, "    3.0")
    en3.insert(0, "    5.0")
    en4.insert(0, "20000j.")
    en5.insert(0, "18000j.")
    en6.insert(0, "  100.0")
    en7.insert(0, "")
    
    e8.insert(0, "Nie wiem, zapomniałem.")
    e9.insert(0, "")
    e10.insert(0, "")
    e11.insert(0, "")
    e12.insert(0, "")
    e13.insert(0, "")
    e14.insert(0, "Elżbieta Groch")
    e15.insert(0, "")
    return
    
def zaladujrp4():
    czyscpola()
    e0.insert(0, "")
    e1.insert(0, "")
    e2.insert(0, "")
    e3.insert(0, "")
    e4.insert(0, "")
    e5.insert(0, "")
    e6.insert(0, "")
    e7.insert(0, "")
    
    en0.insert(0, "")
    en1.insert(0, "")
    en2.insert(0, "")
    en3.insert(0, "")
    en4.insert(0, "")
    en5.insert(0, "")
    en6.insert(0, "")
    en7.insert(0, "")
    
    e8.insert(0, "")
    e9.insert(0, "")
    e10.insert(0, "")
    e11.insert(0, "")
    e12.insert(0, "")
    e13.insert(0, "")
    e14.insert(0, "")
    e15.insert(0, "")
    return
    
def zaladujrp5():
    czyscpola()
    e0.insert(0, "")
    e1.insert(0, "")
    e2.insert(0, "")
    e3.insert(0, "")
    e4.insert(0, "")
    e5.insert(0, "")
    e6.insert(0, "")
    e7.insert(0, "")
    
    en0.insert(0, "")
    en1.insert(0, "")
    en2.insert(0, "")
    en3.insert(0, "")
    en4.insert(0, "")
    en5.insert(0, "")
    en6.insert(0, "")
    en7.insert(0, "")
    
    e8.insert(0, "")
    e9.insert(0, "")
    e10.insert(0, "")
    e11.insert(0, "")
    e12.insert(0, "")
    e13.insert(0, "")
    e14.insert(0, "")
    e15.insert(0, "")
    return
    
def zaladujrp6():
    czyscpola()
    e0.insert(0, "")
    e1.insert(0, "")
    e2.insert(0, "")
    e3.insert(0, "")
    e4.insert(0, "")
    e5.insert(0, "")
    e6.insert(0, "")
    e7.insert(0, "")
    
    en0.insert(0, "")
    en1.insert(0, "")
    en2.insert(0, "")
    en3.insert(0, "")
    en4.insert(0, "")
    en5.insert(0, "")
    en6.insert(0, "")
    en7.insert(0, "")
    
    e8.insert(0, "")
    e9.insert(0, "")
    e10.insert(0, "")
    e11.insert(0, "")
    e12.insert(0, "")
    e13.insert(0, "")
    e14.insert(0, "")
    e15.insert(0, "")
    return
    

ramkazprzepisami = Tki.Frame(ramkasrod, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkazprzepisami.pack(side="bottom", expand="yes", fill="both")
p34 = Tki.Button(ramkazprzepisami, text="MAŚĆ POŚLADKOWA\n\nRp.\nLanolini\nVaselini albi\nParaffini liq.\nAquae aa ad.---100\nM.f.ung.\n\n\n\n\n\n\n", fg="white", bg="navy", justify="left", width=16, height= 15, command=lambda:zaladujrp1())
p34.pack(side="left")
p35 = Tki.Button(ramkazprzepisami, text="EUC./WAZ./WODA 200g\n\nRp.\nEucerini\nVaselini albi\nAquae aa ad.---200\nM.f.ung.\n\n\n\n\n\n\n\n", fg="white", bg="navy", justify="left", width=16, height= 15, command=lambda:zaladujrp2())
p35.pack(side="left")
p36 = Tki.Button(ramkazprzepisami, text="MAŚĆ GROCHOWEJ\n\nRp.\nDetreomycini---4.0\nHydrocortisoni---2.0\nBenzocaini---3.0\nAcidi borici---5.0\nVit.A liq.---20000j.m.\nNystatyni---18000j.m.\nEucerini ad.---100.0\nM.F.ung.\n\n\n\n", fg="white", bg="navy", justify="left", width=16, height= 15, command=lambda:zaladujrp3())
p36.pack(side="left")
p37 = Tki.Button(ramkazprzepisami, text="POWTARZAJĄCA SIĘ RP.4\n\n\n\n\n\n\n\n\n\n\n\n\n\n",fg="white", bg="navy", justify="left", width=16, height= 15, command=lambda:zaladujrp4())
p37.pack(side="left")
p38 = Tki.Button(ramkazprzepisami, text="POWTARZAJĄCA SIĘ RP.5\n\n\n\n\n\n\n\n\n\n\n\n\n\n",fg="white", bg="navy", justify="left", width=16, height= 15, command=lambda:zaladujrp5())
p38.pack(side="left")
p39 = Tki.Button(ramkazprzepisami, text="POWTARZAJĄCA SIĘ RP.6\n\n\n\n\n\n\n\n\n\n\n\n\n\n",fg="white", bg="navy", justify="left", width=16, height= 15, command=lambda:zaladujrp6())
p39.pack(side="left")



ramkasrodL = Tki.Frame(ramkasrod, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkasrodS = Tki.Frame(ramkasrod, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkasrodR = Tki.Frame(ramkasrod, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkasrodL.pack(side="left", expand="yes", fill="both")
ramkasrodS.pack(side="left", expand="yes", fill="both")
ramkasrodR.pack(side="left", expand="yes", fill="both")

ramkasrodS1 = Tki.Frame(ramkasrodS, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=0)
ramkasrodS1.pack(side="top", expand="yes", fill="both")
ramkasrodS2 = Tki.Frame(ramkasrodS, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=0)
ramkasrodS2.pack(side="bottom", expand="yes", fill="both")
ramkasrodS1A = Tki.Frame(ramkasrodS1, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=0)
ramkasrodS1A.pack(side="left", expand="yes", fill="both")
ramkasrodS1B = Tki.Frame(ramkasrodS1, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=0)
ramkasrodS1B.pack(side="left", expand="yes", fill="both")
ramkasrodS1C = Tki.Frame(ramkasrodS1, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=0)
ramkasrodS1C.pack(side="left", expand="yes", fill="both")

info = Tki.StringVar()
inforamka = Tki.Label(ramkasrodS1C, height=1, width=38, font="Courier 10 bold", textvariable = info)
inforamka.pack(side="top")
info.set("Cyberlepkowy generator etykiet wita.")

odpalaj = Tki.Button(ramkasrodS1C, bd=0, image=cyberl, bg="dark green", highlightthickness=0, command=lambda:generujidrukuj())
odpalaj.pack(side="top")

odpalaj = Tki.Button(ramkasrodS1C, bd=1, text="Wyczyść pola.", bg="dark green", highlightthickness=1, command=lambda:czyscpola())
odpalaj.pack(side="bottom", pady=50)

e0 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e0.pack(side="top", anchor="e")
e1 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e1.pack(side="top", anchor="e")
e2 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e2.pack(side="top", anchor="e")
e3 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e3.pack(side="top", anchor="e")
e4 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e4.pack(side="top", anchor="e")
e5 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e5.pack(side="top", anchor="e")
e6 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e6.pack(side="top", anchor="e")
e7 = Tki.Entry(ramkasrodS1A, width=21, font="Courier 20 bold")
e7.pack(side="top", anchor="e")

e8 = Tki.Entry(ramkasrodS2, width=45, font="Courier 20 bold")
e8.pack(side="top", anchor="w")
e9 = Tki.Entry(ramkasrodS2, width=45, font="Courier 20 bold")
e9.pack(side="top", anchor="w")
e10 = Tki.Entry(ramkasrodS2, width=45, font="Courier 20 bold")
e10.pack(side="top", anchor="w")
e11 = Tki.Entry(ramkasrodS2, width=45, font="Courier 20 bold")
e11.pack(side="top", anchor="w")
e12 = Tki.Entry(ramkasrodS2, width=5, font="Courier 20 bold")
e12.pack(side="top", anchor="w")
e13 = Tki.Entry(ramkasrodS2, width=23, font="Courier 20 bold")
e13.pack(side="top", anchor="w")
e14 = Tki.Entry(ramkasrodS2, width=25, font="Courier 20 bold")
e14.pack(side="top", anchor="w")
e15 = Tki.Entry(ramkasrodS2, width=10, font="Courier 20 bold")
e15.pack(side="top", anchor="w")







en0 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en0.pack(side="top", anchor="w")
en1 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en1.pack(side="top", anchor="w")
en2 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en2.pack(side="top", anchor="w")
en3 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en3.pack(side="top", anchor="w")
en4 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en4.pack(side="top", anchor="w")
en5 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en5.pack(side="top", anchor="w")
en6 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en6.pack(side="top", anchor="w")
en7 = Tki.Entry(ramkasrodS1B, width=7, font="Courier 20 bold")
en7.pack(side="top", anchor="w")
###########:pacjenci:
ramkasrodR1 = Tki.Frame(ramkasrodR, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkasrodR1.pack(side="top", expand="yes", fill="both")
ramkasrodR2 = Tki.Frame(ramkasrodR, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=1)
ramkasrodR2.pack(side="bottom", expand="yes", fill="both")

infotext6 = Tki.Message(ramkasrodR1, text="STAŁE I", width=100, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext6.pack(side="top", expand="yes", fill="x")
p34a = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Ac. salic.", command=lambda:wsadz_tekst("Acidi salicylici"))
p34a.pack(side="top")
p34b = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Glukoza", command=lambda:wsadz_tekst("Glukoza"))
p34b.pack(side="top")
p35 = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Ichtioli", command=lambda:wsadz_tekst("Ichtioli"))
p35.pack(side="top")
p36 = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Laktoza", command=lambda:wsadz_tekst("Laktoza"))
p36.pack(side="top")
p37 = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Natrium tio.", command=lambda:wsadz_tekst("Natrii tiosulf."))
p37.pack(side="top")
p38 = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Talci", command=lambda:wsadz_tekst("Talci venati"))
p38.pack(side="top")
p39 = Tki.Button(ramkasrodR1, bg="LightPink1", width=10, height= 2, text="Zinci oxydi", command=lambda:wsadz_tekst("Zinci oxydi"))
p39.pack(side="top")

infotext6 = Tki.Message(ramkasrodR2, text="LEKARZE", width=100, bg='midnight blue', foreground='yellow', font="Sans 10 bold")
infotext6.pack(side="top", expand="yes", fill="x")
p40 = Tki.Button(ramkasrodR2, bg="orange red", width=10, height= 2, text="Kozak W.", command=lambda:wsadz_tekst("Waldemar Kozak"))
p40.pack(side="top")
p41 = Tki.Button(ramkasrodR2, bg="orange red", width=10, height= 2, text="Ściana G.", command=lambda:wsadz_tekst("Grażyna Ściana"))
p41.pack(side="top")
p42 = Tki.Button(ramkasrodR2, bg="orange red", width=10, height= 2, text="Mokulski Z.", command=lambda:wsadz_tekst("Zbigniew Mokulski"))
p42.pack(side="top")
p43 = Tki.Button(ramkasrodR2, bg="orange red", width=10, height= 2, text="Biebrza J.", command=lambda:wsadz_tekst("Jan Biebrza"))
p43.pack(side="top")
p44 = Tki.Button(ramkasrodR2, bg="orange red", width=10, height= 2, text="Wiśniewski T.", command=lambda:wsadz_tekst("Tobiasz Wiśniewski"))
p44.pack(side="top")



p4_0 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ1", font="Helvetica 15 bold", command=lambda:linijka(0), bg="black")
p4_0.pack(side="top"),
p4_1 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ2", font="Helvetica 15 bold", command=lambda:linijka(1), bg="black")
p4_1.pack(side="top")
p4_2 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ3", font="Helvetica 15 bold", command=lambda:linijka(2), bg="black")
p4_2.pack(side="top")
p4_3 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ4", font="Helvetica 15 bold", command=lambda:linijka(3), bg="black")
p4_3.pack(side="top")
p4_4 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ5", font="Helvetica 15 bold", command=lambda:linijka(4), bg="black")
p4_4.pack(side="top")
p4_5 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ6", font="Helvetica 15 bold", command=lambda:linijka(5), bg="black")
p4_5.pack(side="top")
p4_6 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ7", font="Helvetica 15 bold", command=lambda:linijka(6), bg="black")
p4_6.pack(side="top")
p4_7 = Tki.Button(ramkasrodL, fg="white", width=5, text="SKŁ8", font="Helvetica 15 bold", command=lambda:linijka(7), bg="black")
p4_7.pack(side="top")
p4_8 = Tki.Button(ramkasrodL, width=5, text="SPO1", font="Helvetica 15 bold", command=lambda:linijka(8),bg="white")
p4_8.pack(side="top")
p4_9 = Tki.Button(ramkasrodL, width=5, text="SPO2", font="Helvetica 15 bold", command=lambda:linijka(9), bg="white")
p4_9.pack(side="top")
p4_10 = Tki.Button(ramkasrodL, width=5, text="SPO3", font="Helvetica 15 bold", command=lambda:linijka(10), bg="white")
p4_10.pack(side="top")
p4_11 = Tki.Button(ramkasrodL, width=5, text="SPO4", font="Helvetica 15 bold", command=lambda:linijka(11), bg="white")
p4_11.pack(side="top")
p4_12 = Tki.Button(ramkasrodL, fg="white", width=5, text="NUM", font="Helvetica 15 bold", command=lambda:linijka(12), bg="black")
p4_12.pack(side="top")
p4_13 = Tki.Button(ramkasrodL, fg="white", width=5, text=" PAC ", font="Helvetica 15 bold", command=lambda:linijka(13), bg="black")
p4_13.pack(side="top")
p4_14 = Tki.Button(ramkasrodL, fg="white", width=5, text="  LEK  ", font="Helvetica 15 bold", command=lambda:linijka(14), bg="black")
p4_14.pack(side="top")
p4_15 = Tki.Button(ramkasrodL, fg="white", width=5, text="    DAT    ", font="Helvetica 15 bold", command=lambda:linijka(15), bg="black")
p4_15.pack(side="top")


root.mainloop()




