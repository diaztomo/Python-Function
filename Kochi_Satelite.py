#KODE SATELIT
#96-03 GMS5
#04-05 GOE9
#06-10 MT1R
#11-15 MTS2
#16-21 HMW8

#Antara perubahan satelit ada 2 satelit dalam setahun,
#perlu melihat secara langsung bulan saat perubahan satelitnya

#Input
tahun = {"2011":"11",
         "2013":"13","2014":"14",
         "2015":"15",} #dictionary {"YYYY":"YY"}
satelit = "MTS2" #Kode Satelit
jam = "05" #Jam pengambilan gambar, format :"HH"

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
            if os.path.isfile('/home/gazelstronoff/.config/JetBrains/PyCharmCE2021.1/scratches/'+satelit+tahun[i]+j+k+jam+"IR1.pgm.gz"):
                pass #jika file sudah terdownload, maka dilewatkan atau tidak didownload ulang
            else :
                url = "http://weather.is.kochi-u.ac.jp/sat/ALL/"+i+"/"+j+"/"+k+"/"+satelit+tahun[i]+j+k+jam+"IR1.pgm.gz" # URL
                r = requests.get(url, allow_redirects=True) #Mengakses file pada URL
                open(satelit+tahun[i]+j+k+jam+"IR1.pgm.gz","wb").write(r.content) #Menuliskan file ke driektori
                print(satelit+tahun[i]+j+k+jam+"IR1.pgm.gz"+"_berhasil di download") #indikator download selesai
                time.sleep(20) #melambatkan looping agar terhindar dari block website

