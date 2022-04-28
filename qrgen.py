#!/usr/bin/python3
# -*- coding: utf-8 *-*
import qrcode
import subprocess
import sys
import os
import argparse
from PIL import Image
qr_version="0.1"
banner='''
  ___   ___  ____  _____   _____  ___  __  ___   ___  
 |__ \ / _ \|  _ \|  __ \ / ____|/ _ \/_ |/ _ \ / _ \ 
    ) | | | | |_) | |  | | (___ | | | || | (_) | | | |
   / /| | | |  _ <| |  | |\___ \| | | || |\__, | | | |
  / /_| |_| | |_) | |__| |____) | |_| || |  / /| |_| |
 |____|\___/|____/|_____/|_____/ \___/ |_| /_/  \___/ 
                                                      
                                                      '''.format("QRGen ~ v"+qr_version+" ~ by h0nus\n")
print(banner)
#print('Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader\n')
parser = argparse.ArgumentParser(description="Tool to generate Malformed QRCodes for fuzzing QRCode parsers/reader",
                                 usage='''qrgen.py -l [number]\nusage: qrgen.py -w [/path/to/custom/wordlist]\n\nPayload lists:
0 : SQL Injections
1 : XSS
2 : Command Injection
3 : Format String
4 : XXE
5 : String Fuzzing
6 : SSI Injection
7 : LFI / Directory Traversal''',
epilog="Pay attention everywhere, even in the dumbest spot")
sgroup = parser.add_argument_group("Options for QRGen")
sgroup.add_argument("--list","-l",type=int,help="Set wordlist to use",choices=[0,1,2,3,4,5,6,7])
sgroup.add_argument("--wordlist","-w",type=str,default=None,help="Use a custom wordlist")

options = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

lists = ['words/sqli.txt','words/xss.txt','words/cmdinj.txt','words/formatstr.txt','words/xxe.txt','words/strfuzz.txt','words/ssi.txt','words/lfi.txt']

try:
    cmd= subprocess.check_output(['mkdir','genqr'],stderr=subprocess.STDOUT)
    print("Payload path generated..")
except:
    print("Payload path exist, continuing...")
    pass
  
try:
    cmd = subprocess.check_output(['rm', 'genqr/*'],stderr=subprocess.STDOUT)
    print("Clearing QR payloads dir..")
except:
    print("Path already cleared or deleted..")
    pass
  
payloads = []

if options.list!=None:
    z = options.list
    payloads = open(lists[z]).readlines()
elif options.wordlist:
    z = options.wordlist
    payloads = open(str(z)).readlines()
    
for i in range(0, len(payloads)): 
    payloads[i] = payloads[i].strip()

if not os.path.exists("genqr"):
    os.mkdir("genqr")

for i in range(0, len(payloads)): 
    img = qrcode.make(payloads[i])
    img.save("genqr/payload-{}.png".format(i))
    
# print("Generated {} payloads!".format(len(payloads)))
# if(len(payloads)>0):	
# 	  Image.open("genqr/payload-{}.png".format(i-1)).show()
# 	  print("Opening last generated payload...")
    
print("Thanks for using QRGen, made by H0nus..")
