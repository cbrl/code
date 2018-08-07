
#potrzebne uprawnienia administratora 
#W windows 7  dodac pythona do "zezwalaj programowi 
#lub funkcji na dostep przez zapore..." w zapora systemu windows
#w windows 10 uruchamiac za pomoca powershella 


import socket
import struct
import textwrap
import io
import os


s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
s.bind(("192.168.1.147",0))
s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)




def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    try:
        ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    except:
        print("dupa")
        return

    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

def ipv4(addr):
    return '.'.join(map(str, addr))

def tcp_segment(data):
    try:
        src_port, dest_port, sequence, acknowledgement, offset_reserved_flags = struct.unpack('! H H L L H', data[:14])
    except:
        src_port=0
        dest_port=0
        sequence=0
        acknowledgement=0
        offset_reserved_flags=0
  
    offset = (offset_reserved_flags >> 12) * 4
    return src_port, dest_port, sequence, acknowledgement, data[offset:]


def wycinacz(ramka22, ileczlonow):
    wielkielitery=[b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J', b'K', b'L', b'M', b'N', b'O', b'P', b'R', b'S', b'T', b'X', b'Y', b'Z', b'Q', b'W', b'V']
 
    listalekow = []
  
    ileczlonow = ileczlonow - 1
 
    miejscewielkiej2 = 0

    while ileczlonow > 0:
 
        frag=ramka22[ileczlonow]
        ffrag=frag[120:190]
        for x in wielkielitery:
            miejscewielkiej=ffrag.find(x)
            if miejscewielkiej != -1:

                miejscewielkiej2 = miejscewielkiej
        koniecnazwyl=ffrag.find(b'\x00', miejscewielkiej2)        
        listalekow.append(ffrag[miejscewielkiej2:koniecnazwyl])               
        ileczlonow = ileczlonow - 1
    return listalekow



def wycinaczeanu(ramka22, ileczlonow):

    listaeanow = []
  
    ileczlonow = ileczlonow - 1
 
    miejsceeanu = 0

    while ileczlonow > 0:
 
       
        frag=ramka22[ileczlonow]
        miejsceeanu=frag.find(b'\xff\xff\xff\xff\x00\x00\x00\x0d')
       

        if miejsceeanu != -1:

            miejsceeanu=miejsceeanu + 8

            konieceanu=frag.find(b'\x00', miejsceeanu)
            listaeanow.append(frag[miejsceeanu:konieceanu]) 
            
  
        ileczlonow = ileczlonow - 1    

    return listaeanow






def fragmentator(ramka2):



#    ilerazy = ramka2.count(b'\x00\x00\x00B\x00\x00\x00\x00\x00\x00\x00\x01A')
#    ilerazy2 = ramka2.count(b'\xff\xff\xff\xff\x00\x00\x00B')

    ramka22 = ramka2.split(b'\x00\x00\x00B\x00\x00\x00\x00\x00\x00\x00\x01A')
    ileczlonow=(len(ramka22))
    nazwylekow = wycinacz(ramka22, ileczlonow)
    return nazwylekow


def fragmentatorean(ramka2):




    ramka22 = ramka2.split(b'\x00\x00\x00B\x00\x00\x00\x00\x00\x00\x00\x01A')
    ileczlonow=(len(ramka22))
   
    nreanu = wycinaczeanu(ramka22, ileczlonow)
    return nreanu



def wyslijlistesubstancjiiean(substancjeieany):
    
  
    rpihost = '192.168.1.198'
    rpiport = 7008
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ss.connect((rpihost, rpiport))
        ss.sendall(substancjeieany)
        ss.close()
    except:
        print("socket sie poryl")
    return

zapamietajramke = (b'')
licznik = 0

print("# PRZECHWYTYWACZ IS RUNNING :) #")

while True:
    
 
    
    ramka, adres = s.recvfrom(65536)
    
    a, b, c, d, e, f, g = (ipv4_packet(ramka))
    a1, b1, c1, d1, e1 = tcp_segment(g)
    
    if a1 == 3050:
         
#        licznik = licznik + 1
#         if licznik < 8:
#            print(e1)
#            print('##############################')
        
        ilerazy = e1.count(b'\x00\x00\x00B\x00\x00')

        if ilerazy != 0:
            
            ilerazy2 = e1.count(b'\xff\xff\xff\xff\x00\x00\x00B')
            
            if ilerazy2 != 0:
                
                if e1.endswith(b'\x00\x00\x00B\x00\x00\x00d\x00\x00\x00\x00') is False: 
                    zapamietajramke = zapamietajramke + e1
                  
                else:
                    zapamietajramke = zapamietajramke + e1

                    listasubst=(fragmentator(zapamietajramke))
                    listasubst=(b' '.join(listasubst))
                    eany=(fragmentatorean(zapamietajramke))
                    eany=(b' '.join(eany))
                    substancjeieany = listasubst + eany
                    if len(substancjeieany) > 5:
                        wyslijlistesubstancjiiean(substancjeieany)      
                    zapamietajramke = (b'')

                



        
    
    
  
    
       
   

    