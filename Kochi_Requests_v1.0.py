def Month_Day():
    har31 = ["01", "02", "03", "04", "05", "06", "07", "08", "09",
             "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

    har30 = ["01", "02", "03", "04", "05", "06", "07", "08", "09",
             "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]

    har29 = ["01", "02", "03", "04", "05", "06", "07", "08", "09",
             "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28", "29"]

    har28 = ["01", "02", "03", "04", "05", "06", "07", "08", "09",
             "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
             "21", "22", "23", "24", "25", "26", "27", "28"]

    bulan1 = {
        "01": har31,
        "02": har28,
        "03": har31,
        "04": har30,
        "05": har31,
        "06": har30,
        "07": har31,
        "08": har31,
        "09": har30,
        "10": har31,
        "11": har30,
        "12": har31,
    }

    bulan2 = {
        "01": har31,
        "02": har29,
        "03": har31,
        "04": har30,
        "05": har31,
        "06": har30,
        "07": har31,
        "08": har31,
        "09": har30,
        "10": har31,
        "11": har30,
        "12": har31,
    }

    return har31, har30, har29, har28, bulan1, bulan2


def kochi_downloader(tahun={"2016": "16"}, satelit="HMW8", jam="00"):
    # Proses
    import requests
    import time
    import os.path

    har31, har30, har29, har28, bulan1, bulan2 = Month_Day()

    for i in tahun:
        if int(i) % 4 == 0:  # Jika tahun kabisat
            bulan = bulan2.copy()
        else:
            bulan = bulan1.copy()  # jika bukan tahun kabisat
        for j in bulan:
            for k in bulan[j]:
                nama = satelit + tahun[i] + j + k + jam + "IR1.pgm.gz"
                if os.path.isfile(nama):
                    pass  # jika file sudah terdownload, maka dilewatkan atau tidak didownload ulang
                else:
                    url = "http://weather.is.kochi-u.ac.jp/sat/ALL/" + i + "/" + j + "/" + k + "/" + nama  # URL
                    r = requests.get(url, allow_redirects=True)  # Mengakses file pada URL
                    open(nama, "wb").write(r.content)  # Menuliskan file ke driektori
                    print(nama + "_berhasil di download")  # indikator download selesai
                    time.sleep(20)  # melambatkan looping agar terhindar dari block website


def extract_gz(tahun, satelit, jam):
    import gzip
    import shutil
    import os.path

    har31, har30, har29, har28, bulan1, bulan2 = Month_Day()

    for i in tahun:

        if int(i) % 4 == 0:  # Jika tahun kabisat
            bulan = bulan2.copy()
        else:
            bulan = bulan1.copy()  # jika bukan tahun kabisat

        for j in bulan:

            for k in bulan[j]:
                fin = satelit + tahun[i] + j + k + jam + "IR1.pgm.gz"
                fout = satelit + tahun[i] + j + k + jam + "IR1.pgm"
                if os.path.isfile(fout):
                    pass
                else:
                    try:
                        with gzip.open(fin, 'rb') as f_in:
                            with open(fout, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)
                    except:
                        pass


def save_hdf(tahun, satelit, jam, nama_file):
    import numpy as np
    import h5py
    import PIL.Image as pil

    har31, har30, har29, har28, bulan1, bulan2 = Month_Day()

    X = []
    ID = []
    for i in tahun:
        if int(i) % 4 == 0:  # Jika tahun kabisat
            bulan = bulan2.copy()
        else:
            bulan = bulan1.copy()  # jika bukan tahun kabisat
        for j in bulan:
            for k in bulan[j]:
                try:
                    name = satelit + tahun[i] + j + k + jam + "IR1.pgm"
                    ID.append(name)
                    try:
                        a = pil.open(name)
                        a = np.array(a)[150:430, 0:280].reshape((280 * 280))
                        X.append(a)
                    except:
                        a = np.zeros((280, 280)).reshape((280 * 280)) + np.nan
                        X.append(a)
                        print(name + "_NA")
                except:
                    print("Something Wrong UweUweUwe~~~")

        a11 = np.array(X)
        a22 = np.array(ID).reshape(len(a11), 1)
        dataset = np.concatenate((a22.T, a11.T)).T

    import pandas as pd
    df = pd.DataFrame(dataset)
    df.to_hdf(nama_file + '.h5', key='df', mode='w')

    return df


def kochi_dataset(tahun, satelit, jam, nama_file):
    kochi_downloader(tahun, satelit, jam)
    extract_gz(tahun, satelit, jam)
    save_hdf(tahun, satelit, jam, nama_file)

