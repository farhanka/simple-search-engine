import time
import os
from pathlib import Path, PureWindowsPath
from glob import glob
from bs4 import BeautifulSoup as bs
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string
import re
import json

class Kata:
    def __init__(self):
        self.dokumen = {}

class Dokumen:
    def __init__(self, tautan, judul, desc):
        self.url = tautan
        self.judul = judul
        self.isi = desc


kamus = {}
dokumen ={}
display_dokumen = {} 
f=open("words_score.txt", "r", encoding='utf-8')    #uncomment ini untuk baca dari dokumen yang sudah dibersihkan
# f=open("words_score2.txt", "r", encoding='utf-8')   #uncomment ini untuk baca dari dokumen original
baris = f.readlines()

for i in baris:
    kata= i.split(" ")
    key = kata[0]
    kamus[key] = Kata()

    for j in range(1, len(kata)-1):
        temp = kata[j].split(":")
        kamus[key].dokumen[temp[0]] = float(temp[1])
f.close()

BASE_DIR = Path(__file__).resolve().parent
IN_DIR = BASE_DIR / 'download/'

for path in IN_DIR.glob('**/cleaned/*.html'):       #uncomment ini untuk baca dari dokumen yang sudah dibersihkan
# for path in IN_DIR.glob('**/scrapped/*.html'):    #uncomment ini untuk baca dari dokumen original 
    with open(path.resolve(), 'r', encoding='utf-8') as file:
        soup = bs(file,'html.parser')
        p = PureWindowsPath(path.resolve())
        name = p.parts[-1]
        link = soup.url.text
        title = soup.title.text
        top = soup.top.text
        middle = soup.middle.text
        bottom = soup.bottom.text
        content = top +" "+ middle +" "+ bottom
    dokumen[name] = Dokumen(link, title, content)
    file.close() 

factory = StemmerFactory()
stemmer = factory.create_stemmer()
stop_factory = StopWordRemoverFactory().get_stop_words()
dictionary = ArrayDictionary(stop_factory)
stopword = StopWordRemover(dictionary)

def clean(query):
            cleaned = stopword.remove(stemmer.stem(query))
            return cleaned

def search(query, banyak=3):
    query = query.lower()
    query = clean(query)
    start = time.time()
    querylist = query.split(" ")
    result={}

    for i in querylist: #simpan semua query ke dalam dictionary sebagai vektor query
        if i in kamus.keys():
            dokumenList = kamus[i].dokumen

            for j in dokumenList.keys():
                if j not in result.keys():
                    result[j] = float(dokumenList[j])
                
                else:
                    result[j]+= float(dokumenList[j])
    finish = time.time()

    data = []
    nomor=1
    for k, v in sorted(result.items(), key=lambda x:x[1], reverse=True):
        data.append({
            'id' : nomor,
            'title' : str(dokumen[k].judul), 
            'url'   : str(dokumen[k].url),
            'desc'  : str(dokumen[k].isi[:250]) + '...'
        })
        if nomor==banyak:
            break
        nomor+=1

    return json.dumps(data)
