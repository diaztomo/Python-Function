#!/usr/bin/env python
# coding: utf-8

# In[4]:



#KODE SATELIT
#96-03 GMS5
    #04-05 GOE9
    #06-10 MT1R
    #11-15 MTS2
    #16-21 HMW8

    #Antara perubahan satelit ada 2 satelit dalam setahun,
    #perlu melihat secara langsung bulan saat perubahan satelitnya

    #Input

def kochi_downloader(tahun = {"2016":"16"},satelit = "HMW8", jam = "00"):
    #Proses
    import requests
    import time
    import os.path

    har31 = ["01","02","03","04","05","06","07","08","09",
         "10","11","12","13","14","15","16","17","18","19","20",
         "21","22","23","24","25","26","27","28","29","30","31"]

    har30 = ["01","02","03","04","05","06","07","08","09",
         "10","11","12","13","14","15","16","17","18","19","20",
         "21","22","23","24","25","26","27","28","29","30"]

    har29 = ["01","02","03","04","05","06","07","08","09",
         "10","11","12","13","14","15","16","17","18","19","20",
         "21","22","23","24","25","26","27","28","29"]

    har28 = ["01","02","03","04","05","06","07","08","09",
         "10","11","12","13","14","15","16","17","18","19","20",
         "21","22","23","24","25","26","27","28"]

    bulan1 = {
        "01":har31,
        "02":har28,
        "03":har31,
        "04":har30,
        "05":har31,
        "06":har30,
        "07":har31,
        "08":har31,
        "09":har30,
        "10":har31,
        "11":har30,
        "12":har31,
    }

    bulan2 = {
        "01":har31,
        "02":har29,
        "03":har31,
        "04":har30,
        "05":har31,
        "06":har30,
        "07":har31,
        "08":har31,
        "09":har30,
        "10":har31,
        "11":har30,
        "12":har31,
    }

    for i in tahun:
        if int(i)%4==0 : #Jika tahun kabisat
            bulan = bulan2.copy()
        else :
            bulan = bulan1.copy() #jika bukan tahun kabisat
        for j in bulan:
            for k in bulan[j]:
                nama = satelit+tahun[i]+j+k+jam+"IR1.pgm.gz"
                if os.path.isfile(nama):
                    pass #jika file sudah terdownload, maka dilewatkan atau tidak didownload ulang
                else :
                    url = "http://weather.is.kochi-u.ac.jp/sat/ALL/"+i+"/"+j+"/"+k+"/"+nama# URL
                    r = requests.get(url, allow_redirects=True) #Mengakses file pada URL
                    open(nama,"wb").write(r.content) #Menuliskan file ke driektori
                    print(nama+"_berhasil di download") #indikator download selesai
                    time.sleep(20) #melambatkan looping agar terhindar dari block website
    

