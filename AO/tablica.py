#!/usr/bin/env python
# -*- coding: utf-8 -*-



def generatoreanskladleki():
    print("# Trwa generowanie słownika EAN-SKŁAD na podstawie pliku ZAL1+2+3.txt.\n")
    eanskladleki = {}
    with open('/home/pi/Desktop/AO/database/ZAL1+2+3.txt', 'r') as plik_0:		                             
        for line in plik_0.readlines():
	    	line = line.replace("\n", "")
	    	dolar = line.find("$")
	    	EAN13 = line[dolar+1:dolar+14]
	    	malpa = line.find("@")
	    	SUBST = line[malpa+1:]
	    	eanskladleki[EAN13]=SUBST
    print("# Generowanie słownika EAN-SKŁAD zakończone.\n")
    return(eanskladleki)
		
def generatorbazysubst():
    print("# Trwa generowanie słownika SUBSTANCJA-WYŚWIETLANA NAZWA, LISTA LEPEK, KINETYKA, NOTKA DO WYŚWIETLENIA na podstawie pliku subst.txt.\n")
    baza = {}
    with open('/home/pi/Desktop/AO/database/subst.txt', 'r') as plik_1:
        for line in plik_1.readlines():
            line = line.replace("\n", "")
            krecha0 = line.find("|")
            krecha1 = line.find("|", krecha0+1)
            krecha2 = line.find("|", krecha1+1)
            krecha3 = line.find("|", krecha2+1)
            krecha4 = line.find("|", krecha3+1)
            baza[line[krecha0+1:krecha1]]= {"n": line[krecha1+1:krecha2], "l": line[krecha2+1:krecha3], "k": line[krecha3+1:krecha4], "c": line[krecha4+1:]}
    print("# Generowanie słownika SUBSTANCJA-WYŚWIETLANA NAZWA, LISTA LEPEK, KINETYKA, NOTKA DO WYŚWIETLENIA zakończone.\n")
    return(baza)


def generatorslownikadetektora():
    print("# Trwa generowanie słownika FRAZA-SUBSTANCJA na podstawie pliku detektor_substancji.txt.\n")
    slownik_detektora={}
    with open('/home/pi/Desktop/AO/database/detektor_substancji.txt', 'r') as plik_2:
        for line in plik_2.readlines():
            prawy_ptaszek=line.find(">")
            znak_rownosci=line.find("=")
            lewy_ptaszek=line.find("<")
            slownik_detektora[line[prawy_ptaszek+1:znak_rownosci]]=line[znak_rownosci+1:lewy_ptaszek]
    print("# Generowanie słownika FRAZA-SUBSTANCJA zakończone.\n")
    return(slownik_detektora)
