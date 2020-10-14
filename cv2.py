#TOLLS REKAYASA SOSIAL 
#BY DARUL FEBRI
#recode boleh.. saya juga belajar dari ngerecode
#enjoyy
#menghapus jendela nya belum bisa.... makanya berantakan
#sebenernya sih ini toll dikususkan tk termux aja

import os
import time
import sys
import tqdm
os.system("clear")
print("LOADING.......")
time.sleep(3)
def menu():
    os.system("clear")
    print("|========================================|")
    time.sleep(.100)
    print("|              SETUP UTILITY             |")
    time.sleep(.100)
    print("|                                        |")
    time.sleep(.100)
    print("|POWERED BY  DAULFER COMPANY             |")
    time.sleep(.100)
    print("|========================================|")
    time.sleep(.300)
    print("|                                        |")
    time.sleep(.100)
    print("|1. FACEBOOK                             |")
    time.sleep(.100)
    print("|2. TWITTER                              |")
    time.sleep(.100)
    print("|3. FITUR                                |")
    time.sleep(.100)
    print("|                                        |")
    time.sleep(.100)
    print("|========================================|")
    time.sleep(3)
    masuk = input("pilihan > ")
    if (masuk == "1"):
        os.system("clear")
        menu2()
    if (masuk == "2"):
        os.system("clear")
        print("|===============|")
        print("|COMING SOON... |")
        print("|===============|")
        time.sleep(5)
        os.system("clear")
        menu()
    if (masuk == "3"):
        os.system("clear")
        fitur()
    if (masuk != "1","2","3"):
        os.system("clear")
        print("mohon pilih salah satu pilihan")
        menu()
def fitur():
    print("credits..")
    print("|------------------------------------------")
    print("|  Di desain oleh daulfer                 |")
    print("|  Di program oleh daulfer                |")
    print("|  Dibuat di perawang                     |")
    print("|  versi program => 0.1                   |")
    print("|------------------------------------------")
    input("Tekan apa saja untuk melanjutkan...")
    menu()
          
        
              
def menu2():
    os.system("clear")
    print("|==========================================|")
    print("|            FACEBOOK HUNTER               |")
    print("|                                          |")
    print("| POWERED BY DAULFER COMPANY               |")
    print("|==========================================|?")
    print("")
    pilih1()
def pilih1():
    masuk2y = input("Masukkan Id/No hp/ Email : ")
    print("METODE MASUK >",masuk2y)
    time.sleep(3)
    lanjut()
    
def lanjut():
    
    yupi = input("Masukkan nama akun facebooknya ; ")
    print("namanya :",yupi)
    time.sleep(5)
    proses()
  
        
def proses():
    
     
    print ("[*] pengecekan...")
    time.sleep(5)
    print ("[+] pengecekan selesai")
    time.sleep(2)
    print ("")
    print("[*] Memulai operasi")
    time.sleep(1)
    print("[*] mencari user")
    from tqdm import tqdm
    for i in tqdm(range(10)):
        time.sleep(1)
    print("[+] user didapat")
    print("[+] Mencoba mendapatkan sandi")
    time.sleep(2)
    print("[X] Gagal")
    print("[*] Mencoba lagi..")
    time.sleep(2)
    print("[X] Gagal")
    print("[*] Mencoba lagi..")
    time.sleep(2)
    print("[x] Gagal")
    print("[*] Mencoba lagi..")
    from tqdm import tqdm
    for i in tqdm(range(10)):
         time.sleep(1)
    print("[+] Password didapat. Format = md5 ")
    time.sleep(2)
    print("[+] Nge hash password..")
    time.sleep(2)
    print("[+] password didapat.. ;)")
    time.sleep(4)
    os.system("clear")
    data()
def data():
    os.system("clear")
    print("[]=silahkan masukkan data diri target lagi=[]")
    kk = input("[*] nama > ")
    hh = input("[*] no hp/id/email > ")
    time.sleep(2)
    print("MENGKONFIRMASI, MOHON TUNGGU...")
    time.sleep(5)
    print("+-----------------------------------+")
    print("|            DATA KORBAN            |")
    print("+-----------------------------------+")
    time.sleep(.100)
    print("| NAMA         =",kk,              "|")
    time.sleep(.100)
    print("| METODE LOGIN =",hh,              "|")
    time.sleep(.100)
    print("| PASSWORD     = Uzurxbian22        |")
    time.sleep(.100)
    print("+-----------------------------------+")
    print("")
    time.sleep(3)
    print("terimakasih telah menggunakan tolls ini")
    time.sleep(3)
    endl()
def endl():
    exit()
menu()
