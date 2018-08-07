# qpython3 (Android)
# it connects CyberLepki with ZXing barcode scanner on Android device

from androidhelper import Android
import time
import socket
import sys
droid = Android()
HOST = '192.168.43.66'  
PORT = 7008
stare = "kondominium"
droid.setClipboard("kondominium")
while True:
    time.sleep(0.2)
    schowek = droid.getClipboard().result
    if stare != schowek:
        stare = schowek
        paczka=stare.encode() 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.sendall(paczka)
        s.close()
        stare = "kondominium"
        droid.setClipboard("kondominium")
        if schowek[0:3] != "590":
            droid.ttsSpeak("powtórz")
        
