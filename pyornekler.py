#!/usr/bin/python

import author
author
print("\n")
print("\n")
print("\n")
import os,time,sys
isname=os.name
if isname=="posix":
    print("\nİşletim sisteminiz linux tabanlıdır\n")
    
elif isname=="nt":
    print("\nİşletim sisteminiz windows'un sürümlerindendir\n")

aciklama="Bu program basit python örneklerinin fonksiyonlara tanımlandığı bir scripttir\n"

print("Python basit örnekler\n")

print(aciklama)
print("\n")

while True:
    try:
        

        def sonsuzklasor():
            from os import mkdir
            print("\nSonsuz klasör oluşturucu\n")
            x=int(input("\nKlasör sayısının kaçtan başlamasını istediğinizi giriniz:"))
            y=str(input("\nKlasör ismi giriniz:"))
            while True:
                mkdir(y+str(x))
                x+=1

        def kronometre():
            from time import sleep
    
            print("\nKronometre\n")

            x=float(input("\nKaç dakika ayarlamak istiyorsunuz:"))
            x*=60
            sleep(x)
            print("\n")
            print(x,"dakika/saniye doldu!!!\a")
            print("\n")

        def cevrimici():
            import requests
        
            try:    
                calis=input("\nÇevrimiçi olup olmadığını öğrenmek istediğiniz sitenin adresi:")
    
                siteson="http://www."+str(calis)
                requ = requests.get(siteson)
                if requ.status_code==200:
                    print("[ + ] Site çevrimiçidir\n")    
            except:
                print("""[ - ] Aşağıdaki nedenlerin herhangi birinden dolayı siteye erişim yok:
            
                1-Site çevrimiçi değil
            
                2-Site ülkenizde engellenmiş durumdadır
            
                3-Site TOR ağına dahildir\n""")

        def cikis():
            print("\ncreated by 'S3SS!Z H4CK3R'\n")
            print("\nÇıkılıyor...\n")
            time.sleep(2)
            sys.exit() 
    
    
        def notlar():
            osname1=os.name
            if osname1=="posix":
                os.system("clear")
            if osname1=="nt":
                os.system("cls")
            
            not1="Bu program tamamen istediğiniz gibi çalışmayabilir"
            print(not1)
            print("\n")
            not2="""Kronometre seçeneği verdiğiniz değeri 60 ile çarpıp o süreye göre bekleyecektir.Yani siz 1.46 diye bir değer girdiğinizde 106 saniye değil 87.6 saniye bekleyecektir. (Ben denediğim zaman öyle olmuştu:)__)\n"""
            print(not2)
            print("\n")    
            not3="""İlk seçenekteki sonsuz dosya oluşturucu programı kendi cihazlarınızda denemeniz önerilmez.Deneyecekseniz bile yeni boş bir klasör oluşturun ve programı klasörün içine atıp çalıştırın."""   
            print(not3)
            print("\n")
            not4="""Bu programdaki herhangi bir seçenekten dolayı herhangi bir cihaz zarar görürse sorumluluk kullanıcıya aittir."""
            print(not4)
            print("\n")
            print("Çıkılıyor...")
            time.sleep(2)
            sys.exit()

        sec1="""\n[ 1 ] Sonsuz dosya oluşturucu (Uyarı:Bu işlem işlemcinizi çok yorabilir kendi       bilgisayarlarınızda denemeniz önerilmez!!!)"""

        sec2="\n[ 2 ] Kronometre"

        sec3="\n[ 3 ] Site çevrimiçi kontrolü"

        sec4="\n[ 4 ] Program üzerine notlar"

        cik="\n[ 0 ] Çıkış"

        print("\n")
        print(sec1)
        print("\n")
        print(sec2)
        print("\n")
        print(sec3)
        print("\n")
        print(sec4)
        print("\n")
        print(cik)
        print("\n")
        soru=input("\nNe yapmak istediğinizi seçin:")

        if soru=="1":
            sonsuzklasor()
    
        if soru=="2":
            kronometre()
        if soru=="3":
            cevrimici()
        if soru=="4":
            notlar()
        if soru=="0":
            cikis()    

    except KeyboardInterrupt:
        cikis()
