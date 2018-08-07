#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CyberLepki - a tool facilitating the labeling of drug packages.
# Copyright (C) 2018  Piotr Głuchowski
# License: GPLv3
# Contact: cyberlepki@gmail.com


# imports ##############################################################################################################################################

from Tkinter import *
import subprocess
import time
import threading
import socket
import sys
import Queue
import tablica
from PIL import Image as ImageL
from PIL import ImageDraw as ImageDrawL
from PIL import ImageFont as ImageFontL
import PIL.ImageOps  
import string
import random
from datetime import datetime as czas

GFX_PATH = "/home/pi/Desktop/AO/gfx/"
BIN_PATH = "/home/pi/Desktop/AO/lepki/"

# start tkinter #############################################################################################################################################
print("STARTUJEMY :-)")
root=Tk()
root.title("CyberLepki")
root.geometry("1280x800")
root.configure(background='black')

# pictures of stickers (displayed) ##########################################################################################################################

PIC000 = PhotoImage(file = GFX_PATH + "canvas_pory.png")
PIC001 = PhotoImage(file = GFX_PATH + "m1x1.png"); PIC002 = PhotoImage(file = GFX_PATH + "m1x2.png"); PIC003 = PhotoImage(file = GFX_PATH + "m1x3.png")
PIC004 = PhotoImage(file = GFX_PATH + "m2x1.png"); PIC005 = PhotoImage(file = GFX_PATH + "m2x2.png"); PIC006 = PhotoImage(file = GFX_PATH + "m2x3.png")
PIC007 = PhotoImage(file = GFX_PATH + "m3x1.png"); PIC008 = PhotoImage(file = GFX_PATH + "m3x2.png"); PIC009 = PhotoImage(file = GFX_PATH + "m3x3.png")
PIC010 = PhotoImage(file = GFX_PATH + "m4x1.png"); PIC011 = PhotoImage(file = GFX_PATH + "m4x2.png"); PIC012 = PhotoImage(file = GFX_PATH + "m4x3.png")
PIC013 = PhotoImage(file = GFX_PATH + "PIC013_B_30_minut_przed_posilkiem.png"); PIC014 = PhotoImage(file = GFX_PATH + "PIC014_B_ten_lek_bierze_sie_przed_snem.png"); PIC015 = PhotoImage(file = GFX_PATH + "PIC015_B_z_bialkiem_lepiej_wchodzi.png")
PIC016 = PhotoImage(file = GFX_PATH + "PIC016_B_paracetamol.png"); PIC017 = PhotoImage(file = GFX_PATH + "PIC017_B_nie_z_nabialem.png")

# pictures of buttons: #######################################################################################################################################

obrBUTTON0 = PhotoImage(file = GFX_PATH + "info.png"); obrBUTTON1 = PhotoImage(file= GFX_PATH + "next.png"); obrBUTTON2 = PhotoImage(file = GFX_PATH + "xxx.png"); obrBUTTON3 = PhotoImage(file = GFX_PATH + "xxxx.png")
obrBUTTON4 = PhotoImage(file = GFX_PATH + "ratuj.png"); obrBUTTON00 = PhotoImage(file = GFX_PATH + "infol.png"); obrBUTTON00s = PhotoImage(file = GFX_PATH + "start.png"); obrBUTTON01 = PhotoImage(file = GFX_PATH + "infop.png")
obrBUTTON_NE = PhotoImage(file = GFX_PATH + "NE.png"); obrBUTTON_NW0 = PhotoImage(file = GFX_PATH + "NW0.png"); obrBUTTON_NW1 = PhotoImage(file = GFX_PATH + "NW1.png"); obrBUTTON_NW2= PhotoImage(file = GFX_PATH + "NW2.png")
obrBUTTON_SE= PhotoImage(file = GFX_PATH + "SE.png"); obrBUTTON_SW= PhotoImage(file = GFX_PATH + "SW.png"); zieldruk = PhotoImage(file = GFX_PATH + "zieldruk.png"); piskor = PhotoImage(file = GFX_PATH + "piskor.png")
fioldruk = PhotoImage(file = GFX_PATH + "fioldruk.png"); kleps = PhotoImage(file = GFX_PATH + "kleps.png"); xxxxd = PhotoImage(file = GFX_PATH + "xxxxd.png"); xxxxg = PhotoImage(file = GFX_PATH + "xxxxg.png")

#  sticker numbers - files for printer ####################################################################################################

def print_a_sticker(sticker_number):
    file_for_the_printer = BIN_PATH + "pustalepka.bin"
    if sticker_number == 0: file_for_the_printer = BIN_PATH + "pustalepka.bin"
    elif sticker_number == 1: file_for_the_printer = BIN_PATH + "dosage/1x1.bin"
    elif sticker_number == 2: file_for_the_printer = BIN_PATH + "dosage/1x2.bin"
    elif sticker_number == 3: file_for_the_printer = BIN_PATH + "dosage/1x3.bin"
    elif sticker_number == 4: file_for_the_printer = BIN_PATH + "dosage/2x1.bin"
    elif sticker_number == 5: file_for_the_printer = BIN_PATH + "dosage/2x2.bin"
    elif sticker_number == 6: file_for_the_printer = BIN_PATH + "dosage/2x3.bin"
    elif sticker_number == 7: file_for_the_printer = BIN_PATH + "dosage/3x1.bin"
    elif sticker_number == 8: file_for_the_printer = BIN_PATH + "dosage/3x2.bin"
    elif sticker_number == 9: file_for_the_printer = BIN_PATH + "dosage/3x3.bin"
    elif sticker_number == 10: file_for_the_printer = BIN_PATH + "dosage/4x1.bin"
    elif sticker_number == 11: file_for_the_printer = BIN_PATH + "dosage/4x2.bin"
    elif sticker_number == 12: file_for_the_printer = BIN_PATH + "dosage/4x3.bin"
    elif sticker_number == 13: file_for_the_printer = BIN_PATH + "cbrl/PIC013_B_30_minut_przed_posilkiem.bin"
    elif sticker_number == 14: file_for_the_printer = BIN_PATH + "cbrl/PIC014_B_ten_lek_bierze_sie_przed_snem.bin"
    elif sticker_number == 15: file_for_the_printer = BIN_PATH + "cbrl/PIC015_B_z_bialkiem_lepiej_wchodzi.bin"
    elif sticker_number == 16: file_for_the_printer = BIN_PATH + "cbrl/PIC016_B_paracetamol.bin"
    elif sticker_number == 17: file_for_the_printer = BIN_PATH + "cbrl/PIC017_B_nie_z_nabialem.bin"
    subprocess.call(["lpr", file_for_the_printer])
    
    
# displayed picture numbers ###################################################################################################

def choose_picture(which_pict):
    
    global PIC001, PIC002, PIC003, PIC004, PIC005, PIC006, PIC007, PIC008, PIC009, PIC010, PIC011, PIC012;
    global PIC013, PIC014, PIC015, PIC016, PIC017
    
    if which_pict  == 1:
        return(PIC001)
    elif which_pict == 2: 
        return(PIC002)	
    elif which_pict == 3: 
        return(PIC003)
    elif which_pict == 4: 
        return(PIC004)
    elif which_pict == 5: 
        return(PIC005)
    elif which_pict == 6: 
        return(PIC006)	
    elif which_pict == 7: 
        return(PIC007) 
    elif which_pict == 8: 
        return(PIC008)
    elif which_pict == 9:
        return(PIC009)
    elif which_pict == 10: 
        return(PIC010)	
    elif which_pict == 11: 
        return(PIC011)
    elif which_pict == 12: 
        return(PIC012)
    elif which_pict == 13:
        return(PIC013) 
    elif which_pict == 14:
        return(PIC014)
    elif which_pict == 15: 
        return(PIC015)
    elif which_pict == 16:
        return(PIC016)
    elif which_pict == 17: 
        return(PIC017)

# classes: ################################################################################################################

class InfoBelt:
    
    """ Contains sticker image and text comment about drug."""
    
    def __init__(self, title, sticker, kom, nr_obr, purple_green_switch): 
        
        if purple_green_switch == "1":
            kolorek = "DeepPink4"
        else:
            kolorek = "dark green"
    
        self.range_of_choice = nr_obr + ";0;0"
        self.frame = Frame(protoframe, bg = kolorek, highlightbackground = kolorek, highlightcolor = kolorek, highlightthickness=2)
        self.frame.pack(side=TOP, fill=X)
        self.frameL = Frame(self.frame, bg='black', highlightbackground = kolorek, highlightcolor = kolorek, highlightthickness=0)
        self.frameL.pack(side=LEFT)
        self.lab=Label(self.frameL, text = title, font = 'Sans 20 bold', bg = kolorek, fg = 'green yellow')
        self.lab.pack(side=TOP, expand=YES, fill=X, anchor = N)
        self.BUTTON0 = Button(self.frameL, fg = 'red', bd=0, image=sticker, command= lambda: what_has_been_pressed(0, self.range_of_choice), highlightcolor='black', bg="black", highlightbackground='black')
        self.BUTTON0.pack(side=LEFT)
        self.BUTTON1 = Button(self.frameL, fg = 'red', bd=0, image=fioldruk, command= lambda: print_inscription_2("kom", kom), highlightcolor='black', bg="black", highlightbackground='black')
        self.BUTTON1.pack(side=LEFT)
        self.comment = Message(self.frame, width=660, text=kom, bg='black', foreground='green yellow', font="Courier 16", highlightbackground = kolorek, highlightcolor = kolorek, highlightthickness=2)
        self.comment.pack(side=LEFT, expand = YES, fill = BOTH)


class XInfoBelt:
    
    """ Contains three stickers images only."""
    
    def __init__(self, title, sticker0, sticker1, sticker2, range_of_choice, black_switch):
        
        if black_switch == "1":
            kolorek = "black"
        else:
            kolorek = "DeepPink4"
            
        self.frame = Frame(protoframe, bg='DeepPink4', highlightbackground='black', highlightcolor='black', highlightthickness=2)
        self.frame.pack(side=TOP)
        self.lab=Label(self.frame, text=title, font='Sans 20 bold', bg=kolorek, fg='lawn green')
        self.lab.pack(side=TOP, expand=YES, fill=X)
        self.BUTTON0 = Button(self.frame, fg = 'red', bd=0, image=sticker0, command= lambda: what_has_been_pressed(0, range_of_choice), highlightcolor='black', bg="black", highlightbackground='black')
        self.BUTTON0.pack(side=LEFT)
        self.BUTTON1 = Button(self.frame, fg = 'red', bd=0, image=sticker1, command= lambda: what_has_been_pressed(1, range_of_choice), highlightcolor='black', bg="black", highlightbackground='black')
        self.BUTTON1.pack(side=LEFT)
        self.BUTTON2 = Button(self.frame, fg = 'red', bd=0, image=sticker2, command= lambda: what_has_been_pressed(2, range_of_choice), highlightcolor='black', bg="black", highlightbackground='black')
        self.BUTTON2.pack(side=LEFT)
        
# functions: #####################################################################################################################


def menu_on_the_right():
    global BUTTON112menu; global BUTTON2menuxxx
    framemenu = Frame(praprotoframe, bg="black", highlightbackground='black', highlightcolor='black', highlightthickness=5)
    framemenu.pack(side=RIGHT, fill=Y, anchor=E)
    framepom0 = Frame(framemenu, bg="black", highlightbackground='black', highlightcolor='black', highlightthickness=0)
    framepom0.pack(side=TOP)
    BUTTON00menu = Button(framepom0, fg = 'black', bd=0, image=obrBUTTON00, command= lambda: page_minus_one_and_display_belts(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON00menu.pack(side=LEFT)
    BUTTON00smenu = Button(framepom0, fg = 'black', bd=0, image=obrBUTTON00s, command= lambda: page_to_display_eq_one_and_display_belts(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON00smenu.pack(side=RIGHT)
    BUTTON01menu = Button(framemenu, fg = 'black', bd=0, image=obrBUTTON01, command= lambda: page_plus_one_and_display_belts(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON01menu.pack(side=TOP)
    ramka10i11 = Frame(framemenu, bg="black", highlightbackground='black', highlightcolor='black', highlightthickness=0)
    ramka10i11.pack(side=TOP)
    ramkaik=Frame(ramka10i11, bg="black", highlightbackground='black', highlightcolor='black', highlightthickness=0)
    ramkaik.pack(side=RIGHT)
    ramka10i11_2=Frame(ramka10i11, bg="black", highlightbackground='black', highlightcolor='black', highlightthickness=0)
    ramka10i11_2.pack(side=LEFT)
    BUTTON112menu = Button(ramka10i11_2, fg = 'black', bd=0, image=obrBUTTON_NW2, command= lambda: mode_of_operation(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON112menu.pack(side=TOP)
    BUTTON122menu = Button(ramka10i11_2, fg = 'black', bd=0, image=obrBUTTON_SW, command= lambda: green_text_on_black_ean_list(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON122menu.pack(side=TOP)
    BUTTON11menu = Button(ramkaik, fg = 'black', bd=0, image=obrBUTTON_NE, command= lambda: reset_green_text(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON11menu.pack(side=TOP)
    BUTTON12menu = Button(ramkaik, fg = 'black', bd=0, image=obrBUTTON_SE, command= lambda: drug_inter_analyzer(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON12menu.pack(side=TOP)
    BUTTON3gmenu = Button(framemenu, fg = 'black', bd=0, image=xxxxg,  command= lambda: custom_sticker(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON3gmenu.pack(side=TOP)
    BUTTON3dmenu = Button(framemenu, fg = 'black', bd=0, image=xxxxd,  command= lambda: long_note_page(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON3dmenu.pack(side=TOP)
    BUTTON2menuxxx = Button(framemenu, fg = 'black', bd=0, image=obrBUTTON2, command= lambda: drug_dosage_page(), highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON2menuxxx.pack(side=TOP)
    BUTTON4menu = Button(framemenu, fg = 'black', bd=0, image=obrBUTTON4, command=s_o_s, highlightbackground='black', highlightthickness=0, bg="black")
    BUTTON4menu.pack(side=TOP)
    
def ramka_z_tekstem(text_ramka, font_ramka):
	
    """ Start page."""

    frametext = Frame(protoframe, bg="dark green", highlightbackground='midnight blue', highlightcolor='dark green', highlightthickness=0, height=800, width=1110)
    infotext = Message(frametext, text=text_ramka, width=1110, bg='black', foreground='green yellow', font = font_ramka)
    frametext.pack_propagate(0)
    frametext.pack(side=BOTTOM, fill=X, anchor = S)
    infotext.pack(side=LEFT)

def what_has_been_pressed(button_number, range_of_choice):
	range_of_choice_list = range_of_choice.split(";")
	sticker_number = int(range_of_choice_list[button_number])
	print_a_sticker(sticker_number)

def proto_frame_widget_destroyer():
    for widget in protoframe.winfo_children():
        widget.destroy()

def page_plus_one_and_display_belts():
    global global_list_of_recognized_substances, page_to_display
    page_to_display = page_to_display + 1
    belts(global_list_of_recognized_substances, page_to_display)
    
def page_minus_one_and_display_belts():
    global global_list_of_recognized_substances, page_to_display
    page_to_display = page_to_display - 1
    belts(global_list_of_recognized_substances, page_to_display)
    
def green_text_on_black_ean_list():
    global widget_text_field_content, text_field_content, text_field_header, now_is_running
    proto_frame_widget_destroyer()
    pobieracz_label = Label(protoframe, width=1110, textvariable = widget_text_field_content, anchor=NW, justify=LEFT, font = "Courier 20", fg="green yellow", bg="black")
    pobieracz_label.pack_propagate(0)
    pobieracz_label.pack(side=TOP, fill=BOTH)
    widget_text_field_content.set(text_field_header + text_field_content)
    now_is_running = "listaEAN"
   
    
def reset_green_text():
    global eanes_and_substances, text_field_content, was_erased, global_list_of_recognized_substances
    eanes_and_substances = []
    global_list_of_recognized_substances = []
    text_field_content = ""
    page_to_display = 1 
    widget_text_field_content.set(text_field_header + text_field_content)
    was_erased = 1
    
def drug_inter_analyzer(): 
    global widget_text_field_content
    linia="----------------------------------------------------------------------\n"
    widget_text_field_content.set(linia + "              JESZCZE NIE MA ANALIZATORA INTERAKCJI :(\n" + linia)
    return
    
def mode_of_operation():

    """	
    0 - more than 1 belt,
    1 - new belt after each scan,
    2 - automatic printing after code scan.
    
    """
	
    global button_state, BUTTON112menu
    if button_state == 0:
       BUTTON112menu.configure(image=obrBUTTON_NW0) 
       button_state = 1
    elif button_state == 1:
       BUTTON112menu.configure(image=obrBUTTON_NW1)
       button_state = 2
    elif button_state == 2:
       BUTTON112menu.configure(image=obrBUTTON_NW2) 
       button_state = 0

def page_to_display_eq_one_and_display_belts():
    global global_list_of_recognized_substances, page_to_display
    page_to_display = 1
    belts(global_list_of_recognized_substances, page_to_display)

def print_a_sticker_for_me(lista):
    iii = lista[0]
    substance_data = SUBSTANCE_BASE[iii]
    range_of_choice = substance_data["l"] + ";0;0"
    what_has_been_pressed(0, range_of_choice)

def belts(substances, part):
    global page_to_display, SUBSTANCE_BASE, now_is_running
    if part == 0: 
        part = 1
        page_to_display = 1
    proto_frame_widget_destroyer()
    commentt = ""
    licznik00 = 0
    part=part*5
    substances = substances[part-5:part]
    for i in substances:
        licznik00 = licznik00 + 1
        substance_data = (SUBSTANCE_BASE[i])
        # tytuł, wyswietlany obrazek, komentarz, nr obrazka        
        commentt = substance_data["c"] + "\n"
        if licznik00 == 1:
            belt0 = InfoBelt(substance_data["n"], choose_picture(int(substance_data["l"])), commentt, substance_data["l"], "1")
        if licznik00 == 2:
            belt1 = InfoBelt(substance_data["n"], choose_picture(int(substance_data["l"])), commentt, substance_data["l"], "0")
        if licznik00 == 3:
            belt2 = InfoBelt(substance_data["n"], choose_picture(int(substance_data["l"])), commentt, substance_data["l"], "1") 
        if licznik00 == 4:
            belt3 = InfoBelt(substance_data["n"], choose_picture(int(substance_data["l"])), commentt, substance_data["l"], "0")
        if licznik00 == 5:
            belt4 = InfoBelt(substance_data["n"], choose_picture(int(substance_data["l"])), commentt, substance_data["l"], "1")
            break	
    now_is_running = "infobelts"  
    					      
def refreshener():
    global page_to_display, global_list_of_recognized_substances, eanes_and_substances, text_field_content, text_field_header, now_is_running
    global was_erased, koala_counter, BUTTON2menuxxx
    if not received_string_queue.empty():
        page_to_display = 1
        string=received_string_queue.get()
        stringczypowtorzony = string.decode("utf-8")
        if button_state == 2:
            stringczypowtorzony = "njk548u58vhunv8hjvundluvnsdunhv7854jij"
        if stringczypowtorzony in text_field_content:
            koala_counter = 1
            BUTTON2menuxxx.configure(image=piskor)
        elif string[0:2] == "59" and button_state == 0:
                try:
                    pokapoka = EAN_COMPOSITION_PRODUCTS[string]
                except:
                    pokapoka = "W słowniku brak takiego EAN-u."
                string = string.decode("utf-8")
                pokapoka = pokapoka.decode("utf-8")
                eanes_and_substances.append(string + " " + pokapoka)
                text_field_content = ""
                for ean_plus_subst in eanes_and_substances:
                    nowa_pozycja = "".join(ean_plus_subst + "\n")
                    text_field_content = text_field_content + nowa_pozycja
                widget_text_field_content.set(text_field_header + text_field_content)
                global_list_of_recognized_substances = substance_detector(text_field_content)
                if now_is_running == "infobelts":
                    belts(global_list_of_recognized_substances, page_to_display)
                    
        elif string[0:2] == "59" and button_state == 1:
            try:
                skladleku = EAN_COMPOSITION_PRODUCTS[string]
            except:
                skladleku = "W słowniku brak takiego EAN-u." 
            lista_subs_z_jednego_shota = substance_detector(skladleku)
            belts(lista_subs_z_jednego_shota, page_to_display)
            
        elif string[0:2] == "59" and button_state == 2:
            try:
                skladleku = EAN_COMPOSITION_PRODUCTS[string]
            except:
                skladleku = "W słowniku brak takiego EAN-u." 
            lista_subs_z_jednego_shota = substance_detector(skladleku)
            print_a_sticker_for_me(lista_subs_z_jednego_shota)
            
               
    if was_erased == 1 and now_is_running == "infobelts":
        page_to_display = 1   
        was_erased = 0
        global_list_of_recognized_substances = []
        belts(global_list_of_recognized_substances, page_to_display)
    else:
        was_erased = 0
    if koala_counter > 0:
        koala_counter = koala_counter + 1
    if koala_counter == 100:
        BUTTON2menuxxx.configure(image=obrBUTTON2)
        koala_counter = 0
    root.after(100, refreshener)

def substance_detector(text_field_content):
    listaist = []
    for det, pol in DETECTOR_DICTIONARY.items():
        if det in text_field_content:
            listaist.append(pol)
    listaist.remove('')
    return(listaist)
    
  
def s_o_s():
	haslo=(b'RATUJ')
	piotrIP='192.168.1.169'
	piotrport=7009
	ratuj=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ratuj.connect((piotrIP, piotrport))
	ratuj.sendall(haslo)
	ratuj.close()


def clear_how_much_at_what_time_sticker():
    global enter_rano, enter_poludnie, enter_wieczor, enter_noc
    enter_rano.delete(0, "end")
    enter_poludnie.delete(0, "end")
    enter_wieczor.delete(0, "end")
    enter_noc.delete(0, "end")
    return
    
def print_how_much_at_what_time_sticker():
    global enter_rano, enter_poludnie, enter_wieczor, enter_noc, BUTTON2menuxxx
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    HMAWTS_morning = enter_rano.get()
    HMAWTS_noon = enter_poludnie.get()
    HMAWTS_evening = enter_wieczor.get()
    HMAWTS_night = enter_noc.get()
    if HMAWTS_morning =="":
        HMAWTS_morning = "-"
    if HMAWTS_noon =="":
        HMAWTS_noon = "-"
    if HMAWTS_evening =="":
        HMAWTS_evening = "-"
    if HMAWTS_night =="":
        HMAWTS_night = "-"
    img = ImageL.open("/home/pi/Desktop/PILtest/rpwn.png")
    fntrpwn = ImageFontL.truetype("/home/pi/Desktop/PILtest/font.ttf", 110)
    rwpnplus = ImageDrawL.Draw(img)
    rwpnplus.text((58,90), HMAWTS_morning , font=fntrpwn, fill=(0, 0, 0))
    rwpnplus.text((227,90), HMAWTS_noon , font=fntrpwn, fill=(0, 0, 0))
    rwpnplus.text((398,90), HMAWTS_evening , font=fntrpwn, fill=(0, 0, 0))
    rwpnplus.text((572,90), HMAWTS_night , font=fntrpwn, fill=(0, 0, 0))
    img.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)
    
def drug_dosage_page():
    global enter_rano, enter_poludnie, enter_wieczor, enter_noc, V, now_is_running
    V.set(11)
    proto_frame_widget_destroyer()
    radio_frame = Frame(protoframe, height=140, width=1110)
    radio_frame.pack_propagate(0)
    radio_frame.pack(side = TOP)
    radio_frame0 = Frame(radio_frame, bg="black")
    radio_frame0.pack(side = LEFT, fill=Y)
    Radiobutton(radio_frame0, bg='snow', text="TABLETKI", variable = V, value=0, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame0, bg='snow', text="KAPSUŁKI", variable = V, value=1, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame0, bg='snow', text="SASZETKI", variable = V, value=2, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    radio_frame1 = Frame(radio_frame, bg="black")
    radio_frame1.pack(side = LEFT, fill=Y)
    Radiobutton(radio_frame1, bg='sky blue', text="AMPUŁKI", variable = V, value=3, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame1, bg='sky blue', text="ZASTRZYKI", variable = V, value=4, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame1, bg='sky blue', text="KROPLÓWKI", variable = V, value=5, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    radio_frame2 = Frame(radio_frame, bg="black")
    radio_frame2.pack(side = LEFT, fill=Y)
    Radiobutton(radio_frame2, bg='khaki', text="WDECHY", variable = V, value=6, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame2, bg='khaki', text="INHALACJE", variable = V, value=7, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame2, bg='khaki', text="AER.DO NOSA", variable = V, value=8, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    radio_frame3 = Frame(radio_frame, bg="black")
    radio_frame3.pack(side = LEFT, fill=Y)
    Radiobutton(radio_frame3, bg='LightPink1', text="CZOPKI", variable = V, value=9, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame3, bg='LightPink1', text="GLOBULKI", variable = V, value=10, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    Radiobutton(radio_frame3, bg='LightPink1', text="?", variable = V, value=11, height = 2, width = 12, highlightbackground='black', highlightthickness=6).pack(side = TOP, anchor = W)
    porydnia = Canvas(master = radio_frame)
    porydnia.config(bg="black", highlightthickness=0)
    porydnia.pack(side=LEFT, anchor=N)
    porydnia.create_image((190,70), image = PIC000)
    enter_rano = Entry(porydnia, width=1, font="Courier 35 bold", bg="yellow", bd=1)
    porydnia.create_window((53,92), window=enter_rano)
    enter_poludnie = Entry(porydnia, width=1, font="Courier 35 bold", bg="yellow", bd=1)
    porydnia.create_window((143,92), window=enter_poludnie)
    enter_wieczor = Entry(porydnia, width=1, font="Courier 35 bold", bg="yellow", bd=1)
    porydnia.create_window((233,92), window=enter_wieczor)
    enter_noc = Entry(porydnia, width=1, font="Courier 35 bold", bg="yellow", bd=1)
    porydnia.create_window((323,92), window=enter_noc)
    radio_frame3 = Frame(radio_frame, bg="black", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=200, width=200)
    radio_frame3.pack_propagate(0)
    radio_frame3.pack(side=LEFT)
    czyszczylszczyk = Button(radio_frame3, fg = 'white', bd=0, height=3, width=5, text="CZYŚĆ\nRPWN", bg='black', highlightbackground='yellow', highlightthickness=2, command=lambda: clear_how_much_at_what_time_sticker())
    czyszczylszczyk.pack(side=LEFT, padx=10)
    BUTTONprint__pory = Button(radio_frame3, fg = 'black', bd=0, height=5, width=8, text="DRUKUJ\n RPWN", bg="red", highlightthickness=0, command=lambda: print_how_much_at_what_time_sticker())
    BUTTONprint__pory.pack(side=RIGHT, padx=10)
    xbelt0 = XInfoBelt("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''", PIC001, PIC002, PIC003, "1;2;3", "1")
    xbelt1 = XInfoBelt("", PIC004, PIC005, PIC006, "4;5;6", "1")
    xbelt2 = XInfoBelt("", PIC007, PIC008, PIC009, "7;8;9", "1")
    xbelt3 = XInfoBelt("", PIC010, PIC011, PIC012, "10;11;12", "1")
    now_is_running = "dawkowania"
    
def random_number():
    global drawn_number
    drawn_number.set(''.join(random.choice("ABCDEF" + string.digits) for i in range(5)))

    
def clear_fields():
    global inscr_0, inscr_10, inscr_11, inscr_20, inscr_21, inscr_22, inscr_23, inscr_24, inscr_25, inscr_26, inscr_27, inscr_28
    inscr_0.delete(0, "end"); inscr_10.delete(0, "end"); inscr_11.delete(0, "end"); inscr_20.delete(0, "end"); inscr_21.delete(0, "end")
    inscr_23.delete(0, "end"); inscr_24.delete(0, "end"); inscr_25.delete(0, "end"); inscr_26.delete(0, "end"); inscr_27.delete(0, "end")
    inscr_28.delete(0, "end")


def print_inscription_0():
    global BUTTON2menuxxx
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    fnt = ImageFontL.truetype("/home/pi/Desktop/PILtest/font.ttf", 160)
    L0 = ImageL.new("RGB", (696, 185), "white")
    lepa=ImageDrawL.Draw(L0)
    n0 = inscr_0.get()
    lepa.text((0,0), n0, font=fnt, fill=(0, 0, 0))
    L0.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)

    
def print_inscription_1():
    global BUTTON2menuxxx
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    fnt = ImageFontL.truetype("/home/pi/Desktop/PILtest/font.ttf", 80)
    n0=inscr_10.get()
    n1=inscr_11.get()
    n1=n1.rstrip()
    if n1 == "":
        L0 = ImageL.new("RGB", (696, 90), "white")
    else:
        L0 = ImageL.new("RGB", (696, 185), "white")
    lepa=ImageDrawL.Draw(L0)
    lepa.text((0,0), n0, font=fnt, fill=(0, 0, 0))
    lepa.text((0,90), n1, font=fnt, fill=(0, 0, 0))
    L0.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)

    
def print_inscription_2(lep_czy_kom, belt_comment):
    global BUTTON2menuxxx
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    fnt = ImageFontL.truetype("/home/pi/Desktop/PILtest/font.ttf", 40)
    if lep_czy_kom == "lep":
        n0=inscr_20.get(); n1=inscr_21.get(); n2=inscr_23.get(); n3=inscr_24.get(); n4=inscr_25.get(); n5=inscr_26.get(); n6=inscr_27.get(); n7=inscr_28.get()
    elif lep_czy_kom == "kom":
        belt_comment = unicode(belt_comment, 'utf-8')
        n0=belt_comment[0:28]
        n1=belt_comment[28:56]
        n2=belt_comment[56:84]
        n3=belt_comment[84:112]
        n4=belt_comment[112:140]
        n5=belt_comment[140:168]
        n6=belt_comment[168:196]
        n7=belt_comment[196:224]
    n0=n0.rstrip(); n1=n1.rstrip(); n2=n2.rstrip(); n3=n3.rstrip(); n4=n4.rstrip(); n5=n5.rstrip(); n6=n6.rstrip(); n7=n7.rstrip()
    y=48
    if n0 != "":
        y=48
    if n1 != "":
        y=88
    if n2 != "":
        y=128
    if n3 != "":
        y=168
    if n4 != "":
        y=208
    if n5 != "":
        y=248
    if n6 != "":
        y=288
    if n7 != "":
        y=328
    L0 = ImageL.new("RGB", (696, y), "white")
    lepa=ImageDrawL.Draw(L0)
    lepa.text((0,0), n0, font=fnt, fill=(0, 0, 0))
    lepa.text((0,40), n1, font=fnt, fill=(0, 0, 0))
    lepa.text((0,80), n2, font=fnt, fill=(0, 0, 0))
    lepa.text((0,120), n3, font=fnt, fill=(0, 0, 0))
    lepa.text((0,160), n4, font=fnt, fill=(0, 0, 0))
    lepa.text((0,200), n5, font=fnt, fill=(0, 0, 0))
    lepa.text((0,240), n6, font=fnt, fill=(0, 0, 0))
    lepa.text((0,280), n7, font=fnt, fill=(0, 0, 0))
    L0.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)

    
def print_random_number():
    global BUTTON2menuxxx
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    n0 = drawn_number.get()
    fnt = ImageFontL.truetype("/home/pi/Desktop/PILtest/font.ttf", 160)
    L0 = ImageL.new("RGB", (696, 185), "white")
    lepa=ImageDrawL.Draw(L0)
    lepa.text((0,0), n0, font=fnt, fill=(0, 0, 0))
    L0.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)

    
def print_random_number_no_cut():
    global BUTTON2menuxxx
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    n0 = drawn_number.get()
    fnt = ImageFontL.truetype("/home/pi/Desktop/PILtest/font.ttf", 160)
    L0 = ImageL.new("RGB", (696, 185), "white")
    lepa=ImageDrawL.Draw(L0)
    lepa.text((0,0), n0, font=fnt, fill=(0, 0, 0))
    L0.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
        subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "--no-cut", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)

    
def p_for_given_only():
    nagl = czas.now().strftime("%Y%m%d-%H%M%S-WYDAĆ-POBRAĆ")
    inscr_20.delete(0, "end")
    inscr_20.insert(0, nagl)
    inscr_28.delete(0, "end")
    inscr_28.insert(0, "ZAPŁACONO ZA WZIĘTE")

    
def p_for_all():
    nagl = czas.now().strftime("%Y%m%d-%H%M%S--TYLKO-WYDAĆ")
    inscr_20.delete(0, "end")
    inscr_20.insert(0, nagl)
    inscr_28.delete(0, "end")
    inscr_28.insert(0, "ZAPŁACONO ZA CAŁOŚĆ")
    
def ordered_by(): 
    podl = czas.now().strftime(">>> %Y.%m.%d--%H:%M:%S <<<")
    inscr_20.delete(0, "end")
    inscr_20.insert(0, ">>> ZAMÓWIONE PANI/PANU: <<<")
    inscr_23.delete(0, "end")
    inscr_23.insert(0, ">>>>>>>>>>> TOWAR: <<<<<<<<<")
    inscr_28.delete(0, "end")
    inscr_28.insert(0, podl)
    
def custom_sticker():
    global inscr_0, inscr_10, inscr_11, inscr_20, inscr_21, inscr_23, inscr_24, inscr_25, inscr_26, inscr_27, inscr_28, drawn_number, now_is_running
    proto_frame_widget_destroyer()
    custom_sticker_typ2 = Frame(protoframe, bg="black", highlightbackground='midnight blue', highlightcolor='red', highlightthickness=1, height=400, width=1110)
    custom_sticker_typ2.pack_propagate(0)
    custom_sticker_typ2.pack(side=TOP, fill=X)
    custom_sticker_typ2L = Frame(custom_sticker_typ2, bg="orange", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=400)
    custom_sticker_typ2L.pack(side=LEFT)
    custom_sticker_typ2R = Frame(custom_sticker_typ2, bg="dark green", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=400, width=280)
    custom_sticker_typ2R.pack_propagate(0)
    custom_sticker_typ2R.pack(side=RIGHT)
    BUTTONprint__3 = Button(custom_sticker_typ2R, fg = 'black', bd=0, height=4, width=13, text="LOSUJ", bg='green yellow', highlightthickness=0, command=lambda: random_number())
    BUTTONprint__3.pack(side=BOTTOM, pady=20)
    BUTTONprint__4 = Button(custom_sticker_typ2R, fg = 'black', bd=0, height=4, width=13, text="DRUKUJ", bg="red", highlightthickness=0, command=lambda: print_random_number())
    BUTTONprint__4.pack(side=BOTTOM, pady=20)
    BUTTONprint__5 = Button(custom_sticker_typ2R, fg = 'black', bd=0, height=4, width=13, text="DRUKUJ BEZ CIĘCIA", bg="red", highlightthickness=0, command=lambda: print_random_number_no_cut())
    BUTTONprint__5.pack(side=BOTTOM, pady=20)
    inforamka = Label(custom_sticker_typ2R, height=1, width=17, font="Courier 20 bold", text ="WYLOSOWANY NR:", bg='green yellow')
    inforamka.pack(side="top")
    ramkaznumerkiem = Label(custom_sticker_typ2R, height=1, width=17, font="Courier 20 bold", textvariable = drawn_number, bg='green yellow', fg='red')
    ramkaznumerkiem.pack(side="top")
    custom_sticker_typ2RD = Frame(custom_sticker_typ2, bg="black", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=400, width=200)
    custom_sticker_typ2RD.pack_propagate(0)
    custom_sticker_typ2RD.pack(side=RIGHT)
    BUTTONprint__2 = Button(custom_sticker_typ2RD, fg = 'black', bd=0, height=7, width=10, text="DRUKUJ", bg="red", highlightthickness=0, command=lambda: print_inscription_2("lep", ""))
    BUTTONprint__2.pack(side=TOP)
    BUTTONczysciciel = Button(custom_sticker_typ2RD, fg = 'white', bd=0, height=3, width=10, text="CZYŚĆ POLA", bg='black', highlightbackground='yellow', highlightthickness=4, command=lambda: clear_fields())
    BUTTONczysciciel.pack(side=BOTTOM)
    BUTTONzzw = Button(custom_sticker_typ2RD, fg = 'white', bd=0, height=3, width=10, text="ZZW", bg='yellow4', highlightbackground='yellow', highlightthickness=4, command=lambda: p_for_given_only())
    BUTTONzzw.pack(side=BOTTOM)
    BUTTONzzc = Button(custom_sticker_typ2RD, fg = 'white', bd=0, height=3, width=10, text="ZZC", bg='purple4', highlightbackground='yellow', highlightthickness=4, command=lambda: p_for_all())
    BUTTONzzc.pack(side=BOTTOM)
    BUTTONzzp = Button(custom_sticker_typ2RD, fg = 'black', bd=0, height=3, width=10, text="ZAM. POD PACJ.", bg='deep pink', highlightbackground='yellow', highlightthickness=4, command=lambda: ordered_by())
    BUTTONzzp.pack(side=BOTTOM) 
    inscr_20=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_20.pack(side=TOP)
    inscr_21=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_21.pack(side=TOP)
    inscr_23=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_23.pack(side=TOP)
    inscr_24=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_24.pack(side=TOP)
    inscr_25=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_25.pack(side=TOP)
    inscr_26=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_26.pack(side=TOP)
    inscr_27=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_27.pack(side=TOP)
    inscr_28=Entry(custom_sticker_typ2L, width=28, font="Courier 28 bold", bg="yellow", bd=1)
    inscr_28.pack(side=TOP)
    custom_sticker_typ1 = Frame(protoframe, bg="black", highlightbackground='midnight blue', highlightcolor='red', highlightthickness=1, height=200, width=1110)
    custom_sticker_typ1.pack_propagate(0)
    custom_sticker_typ1.pack(side=TOP, fill=X)
    custom_sticker_typ1L = Frame(custom_sticker_typ1, bg="orange", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=200)
    custom_sticker_typ1L.pack(side=LEFT)
    custom_sticker_typ1R = Frame(custom_sticker_typ1, bg="black", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=200, width=200)
    custom_sticker_typ1R.pack_propagate(0)
    custom_sticker_typ1R.pack(side=RIGHT, anchor=S)
    BUTTONprint__1 = Button(custom_sticker_typ1R, fg = 'black', bd=0, height=7, width=10, text="DRUKUJ", bg="red", highlightthickness=0, command=lambda: print_inscription_1())
    BUTTONprint__1.pack(pady=50)
    inscr_10=Entry(custom_sticker_typ1L, width=14, font="Courier 65 bold", bg="yellow", bd=1)
    inscr_10.pack(side=TOP)
    inscr_11=Entry(custom_sticker_typ1L, width=14, font="Courier 65 bold", bg="yellow", bd=1)
    inscr_11.pack(side=TOP)
    custom_sticker_typ0 = Frame(protoframe, bg="black", highlightbackground='midnight blue', highlightcolor='red', highlightthickness=1, height=200, width=1110)
    custom_sticker_typ0.pack_propagate(0)
    custom_sticker_typ0.pack(side=TOP, fill=X)
    custom_sticker_typ0L = Frame(custom_sticker_typ0, bg="orange", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=200)
    custom_sticker_typ0L.pack(side=LEFT)
    custom_sticker_typ0R = Frame(custom_sticker_typ0, bg="black", highlightbackground='red', highlightcolor='red', highlightthickness=0, height=200, width=200)
    custom_sticker_typ0R.pack_propagate(0)
    custom_sticker_typ0R.pack(side=RIGHT, anchor=S)
    BUTTONprint__0 = Button(custom_sticker_typ0R, fg = 'black', bd=0, height=7, width=10, text="DRUKUJ", bg="red", highlightthickness=0, command=lambda: print_inscription_0())
    BUTTONprint__0.pack(pady=50)
    inscr_0=Entry(custom_sticker_typ0L, width=7, font="Courier 150 bold", bg="yellow", bd=1)
    inscr_0.pack(side=LEFT)
    now_is_running = "customlepka"
    
def long_note_page():
    global now_is_running, note_s
    proto_frame_widget_destroyer()
    ramkanotka=Frame(protoframe, bd=0, bg="DarkOrchid4")
    ramkanotka.pack(side=TOP, expand=YES, fill=X)
    print_0 = Button(ramkanotka, bd=0, height = 4, command=lambda:  print_long_note(), fg="black", width=24, bg='red', text="DRUKUJ TEKST", highlightthickness=0)
    print_0.pack(side=LEFT, anchor=N, padx = 24)
    print_1 = Button(ramkanotka, bd=0, height = 4, command=lambda: clear_notepad(), fg="white", width=24, bg='black', text="CZYŚĆ POLE TEKSTOWE", highlightthickness=0)
    print_1.pack(side=LEFT, anchor=N, padx = 24)
    print_2 = Button(ramkanotka, bd=0, height = 4, command=lambda: insert_time(), fg="black", width=24, bg='green yellow', text="WKLEJ DATĘ I CZAS", highlightthickness=0)
    print_2.pack(side=RIGHT, anchor=N, padx = 24)
    print_3 = Button(ramkanotka, bd=0, height = 4, command=lambda: insert_eans(), fg="black", width=24, bg='green yellow', text="WKLEJ LISTĘ EAN", highlightthickness=0)
    print_3.pack(side=RIGHT, anchor=N, padx = 24)
    note_s = Text(protoframe, width=46, height=16, bd=0, bg="black", insertbackground="green yellow", insertwidth="4", fg="green yellow", font="Courier 30", highlightcolor='red', highlightbackground='red', highlightthickness=0)
    note_s.pack(side=TOP, expand=YES, fill=BOTH)
    now_is_running = "LongNote"

def insert_time():
    podl = czas.now().strftime(">>> %Y.%m.%d--%H:%M:%S <<<")
    note_s.insert(INSERT, podl)

def insert_eans():
    global note_s, text_field_content
    note_s.insert(INSERT, text_field_content) 
    
def clear_notepad():
    global note_s
    note_s.delete("1.0", "end")

def print_long_note():
    global BUTTON2menuxxx, note_s
    BUTTON2menuxxx.configure(image=kleps)
    BUTTON2menuxxx.update_idletasks()
    fnt = ImageFontL.truetype("/home/pi/Desktop/PILtest/dluganotka.ttf", 40)
    xn = ""
    xn0=note_s.get("1.0", "1.end")
    xn = xn + xn0 + "\n"
    xn1=note_s.get("2.0", "2.end")
    xn = xn + xn1 + "\n"
    xn2=note_s.get("3.0", "3.end")
    xn = xn + xn2 + "\n"
    xn3=note_s.get("4.0", "4.end")
    xn = xn + xn3 + "\n"
    xn4=note_s.get("5.0", "5.end")
    xn = xn + xn4 + "\n"
    xn5=note_s.get("6.0", "6.end")
    xn = xn + xn5 + "\n"
    xn6=note_s.get("7.0", "7.end")
    xn = xn + xn6 + "\n"
    xn7=note_s.get("8.0", "8.end")
    xn = xn + xn7 + "\n"
    xn8=note_s.get("9.0", "9.end")
    xn = xn + xn8 + "\n"
    xn9=note_s.get("10.0", "10.end")
    xn = xn + xn9 + "\n"
    xn10=note_s.get("11.0", "11.end")
    xn = xn + xn10 + "\n"
    xn11=note_s.get("12.0", "12.end")
    xn = xn + xn11 + "\n"
    xn12=note_s.get("13.0", "13.end")
    xn = xn + xn12 + "\n"
    xn13=note_s.get("14.0", "14.end")
    xn = xn + xn13 + "\n"
    xn14=note_s.get("15.0", "15.end")
    xn = xn + xn14 + "\n"
    xn15=note_s.get("16.0", "16.end")
    xn = xn + xn15 + "\n"
    xn = xn.replace("\n\n", "\n")
    kom = xn
    enterek = 0
    listaenek = []
    while True:
        if enterek == 0:
            hop = 0
        else:
            hop = 1
        enterek = kom.find("\n", enterek + hop)
        if enterek != -1:
            listaenek.append(enterek)
        else:
            break
    shift = 0
    krechaspacjowa = 46
    for nextline_symbol_place in listaenek:
        how_many_spaces = 0
        nextline_symbol_place = nextline_symbol_place + shift
        if nextline_symbol_place > 0 and nextline_symbol_place < 46:
             how_many_spaces = 46 - nextline_symbol_place
        elif nextline_symbol_place > 46 and nextline_symbol_place < 92:
             how_many_spaces = 92 - nextline_symbol_place
        elif nextline_symbol_place > 92 and nextline_symbol_place < 138:
             how_many_spaces = 138 - nextline_symbol_place
        elif nextline_symbol_place > 138 and nextline_symbol_place < 184:
             how_many_spaces = 184 - nextline_symbol_place
        elif nextline_symbol_place > 184 and nextline_symbol_place < 230:
             how_many_spaces = 230 - nextline_symbol_place
        elif nextline_symbol_place > 230 and nextline_symbol_place < 276:
             how_many_spaces = 276 - nextline_symbol_place
        elif nextline_symbol_place > 276 and nextline_symbol_place < 322:
             how_many_spaces = 322 - nextline_symbol_place
        elif nextline_symbol_place > 322 and nextline_symbol_place < 368:
             how_many_spaces = 368 - nextline_symbol_place
        elif nextline_symbol_place > 368 and nextline_symbol_place < 414:
             how_many_spaces = 414 - nextline_symbol_place
        elif nextline_symbol_place > 414 and nextline_symbol_place < 460:
             how_many_spaces = 460 - nextline_symbol_place
        elif nextline_symbol_place > 460 and nextline_symbol_place < 506:
             how_many_spaces = 506 - nextline_symbol_place
        elif nextline_symbol_place > 506 and nextline_symbol_place < 552:
             how_many_spaces = 552 - nextline_symbol_place
        elif nextline_symbol_place > 552 and nextline_symbol_place < 598:
             how_many_spaces = 598 - nextline_symbol_place
        elif nextline_symbol_place > 598 and nextline_symbol_place < 644:
             how_many_spaces = 644 - nextline_symbol_place
        elif nextline_symbol_place > 644 and nextline_symbol_place < 690:
             how_many_spaces = 690 - nextline_symbol_place
        elif nextline_symbol_place > 690 and nextline_symbol_place < 736:
             how_many_spaces = 736 - nextline_symbol_place
        kom_part0 = kom[:nextline_symbol_place]
        kom_part1 = kom[nextline_symbol_place + 1:]
        kom = kom_part0 + " "*how_many_spaces + kom_part1
        shift = shift + how_many_spaces - 1 
    n0=kom[0:46]
    n1=kom[46:92]
    n2=kom[92:138]
    n3=kom[138:184]
    n4=kom[184:230]
    n5=kom[230:276]
    n6=kom[276:322]
    n7=kom[322:368]
    n8=kom[368:414]
    n9=kom[414:460]
    n10=kom[460:506]
    n11=kom[506:552]
    n12=kom[552:598]
    n13=kom[598:644]
    n14=kom[644:690]
    n15=kom[690:736]
    n0=n0.upper(); n1=n1.upper(); n2=n2.upper(); n3=n3.upper(); n4=n4.upper(); n5=n5.upper(); n6=n6.upper(); n7=n7.upper()
    n8=n8.upper(); n9=n9.upper(); n10=n10.upper(); n11=n11.upper(); n12=n12.upper(); n13=n13.upper(); n14=n14.upper(); n15=n15.upper()
    n0=n0.rstrip(); n1=n1.rstrip(); n2=n2.rstrip(); n3=n3.rstrip(); n4=n4.rstrip(); n5=n5.rstrip(); n6=n6.rstrip(); n7=n7.rstrip()
    n8=n8.rstrip(); n9=n9.rstrip(); n10=n10.rstrip(); n11=n11.rstrip(); n12=n12.rstrip(); n13=n13.rstrip(); n14=n14.rstrip(); n15=n15.rstrip()
    y=48
    if n0 != "":
        y=48
    if n1 != "":
        y=88
    if n2 != "":
        y=128
    if n3 != "":
        y=168
    if n4 != "":
        y=208
    if n5 != "":
        y=248
    if n6 != "":
        y=288
    if n7 != "":
        y=328
    if n8 != "":
        y=368
    if n9 != "":
        y=408
    if n10 != "":
        y=448
    if n11 != "":
        y=488
    if n12 != "":
        y=528
    if n13 != "":
        y=568
    if n14 != "":
        y=608
    if n15 != "":
        y=648
    L0 = ImageL.new("RGB", (696, y), "white")
    lepa=ImageDrawL.Draw(L0)
    lepa.text((0,0), n0, font=fnt, fill=(0, 0, 0))
    lepa.text((0,40), n1, font=fnt, fill=(0, 0, 0))
    lepa.text((0,80), n2, font=fnt, fill=(0, 0, 0))
    lepa.text((0,120), n3, font=fnt, fill=(0, 0, 0))
    lepa.text((0,160), n4, font=fnt, fill=(0, 0, 0))
    lepa.text((0,200), n5, font=fnt, fill=(0, 0, 0))
    lepa.text((0,240), n6, font=fnt, fill=(0, 0, 0))
    lepa.text((0,280), n7, font=fnt, fill=(0, 0, 0))
    lepa.text((0,320), n8, font=fnt, fill=(0, 0, 0))
    lepa.text((0,360), n9, font=fnt, fill=(0, 0, 0))
    lepa.text((0,400), n10, font=fnt, fill=(0, 0, 0))
    lepa.text((0,440), n11, font=fnt, fill=(0, 0, 0))
    lepa.text((0,480), n12, font=fnt, fill=(0, 0, 0))
    lepa.text((0,520), n13, font=fnt, fill=(0, 0, 0))
    lepa.text((0,560), n14, font=fnt, fill=(0, 0, 0))
    lepa.text((0,600), n15, font=fnt, fill=(0, 0, 0))
    L0.save("/ramfs/customlepa.png")
    with open("/ramfs/bindowyslania.bin", "w") as binarkadlaql:
       subprocess.call(["brother_ql_create", "--model", "QL-800", "--label-size", "62", "/ramfs/customlepa.png"], stdout=binarkadlaql)
    subprocess.call(["lpr", "/ramfs/bindowyslania.bin"])
    BUTTON2menuxxx.configure(image=obrBUTTON2)
     
## threads: ######################################################################################

def thread_zero():
	
    """Parallel execution. Threading + Queue."""	

    HOST = subprocess.Popen(["hostname", "-I"], stdout=subprocess.PIPE ).communicate()[0]
    HOST = HOST.replace('\n', '')
    PORT = 7008
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('# Utworzono Socket.\n')
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('# Nie udało się przywiązać Socketa do ' + HOST + " " + str(PORT) + ".\n")
        sys.exit()
    print('# Socket przywiązany do ' + HOST + " " + str(PORT) + ".\n")
    content = (b'')
    while True:  
        s.listen(10)
        conn, addr = s.accept()
        content = (b'skip')
        while True:   
            data = conn.recv(1024)   
            if len(data) != 0:
                content = data
            if len(data) == 0:
                conn.close()
                break
        if content != (b'skip'):
            received_string_queue.put(content.decode("cp437"))
            
# prep ######################################################################################################################################################

SUBSTANCE_BASE = {}
SUBSTANCE_BASE = tablica.generatorbazysubst()    
EAN_COMPOSITION_PRODUCTS = {}
EAN_COMPOSITION_PRODUCTS = tablica.generatoreanskladleki()   
DETECTOR_DICTIONARY = {}
DETECTOR_DICTIONARY  = tablica.generatorslownikadetektora()
now_is_running = ""
button_state = 0               
global_list_of_recognized_substances=[]
eanes_and_substances = []
page_to_display = 1
was_erased = 0
text_field_content = ""
koala_counter = 0
text_field_header = "----------------------------------------------------------------------\n" + "                          ODCZYTANE EANY:\n" + "----------------------------------------------------------------------\n"
V = IntVar()
widget_text_field_content = StringVar()
drawn_number = StringVar()
praprotoframe = Frame(bg='black', height=800, width=1280)
praprotoframe.pack_propagate(0)
praprotoframe.pack(fill=BOTH)
menu_on_the_right() 
protoframe=Frame(praprotoframe,  bg='black', width=1110, height=800)
protoframe.pack_propagate(0)
protoframe.pack(fill=BOTH)
received_string_queue=Queue.Queue()
datareception=threading.Thread(target=thread_zero)
datareception.start()
ramka_z_tekstem("CyberLepki - narzędzie ułatwiające etykietowanie opakowań leków.\n\nCopyright (C) 2018  Piotr Głuchowski.\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by \
the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, \
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. \
You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.", "Sans 24") 
refreshener()
root.mainloop()






	


