#last modified: 18/11/2020
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory, StopWordRemover, ArrayDictionary
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from bs4 import BeautifulSoup as bs
import string
import re
import sys
import os
import time



site = ""
total_documents = 0

try:
    total_documents = int(sys.argv[2])
    site = sys.argv[1]
except:
    print("\nERROR : Invalid argument(s)")
    print("Valid : py", sys.argv[0],"[site] [total document]")
    print("Example : py ",sys.argv[0]," detik 1000")
    # print("Available site = detik, viva, kompas")
    exit()


start = time.time()
os.system('cls')

# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
# create stopword
stop_factory = StopWordRemoverFactory().get_stop_words()
more_stopword = ['halaman','kompas','com','all', '-']

# Merge stopword
stop_factory += more_stopword

dictionary = ArrayDictionary(stop_factory)
stopword = StopWordRemover(dictionary)

for i in range(total_documents):
    print(i, "/",total_documents ,"documents cleaned")
    print("Cleaning...")
    try:
        with open("download/"+site+"/scrapped/"+site+"-"+str(i+1)+"-bersih.html",'r', encoding="utf8") as f:
            soup = bs(f,'html.parser')

        url = soup.url.text
        title = soup.title.text
        top = soup.top.text
        middle = soup.middle.text
        bottom = soup.bottom.text

        def clean(tag):
            cleaned = stopword.remove(stemmer.stem(tag))
            return cleaned.translate(str.maketrans('', '', string.punctuation))

        title_cleaned   = clean(title)
        top_cleaned   = clean(top)
        middle_cleaned   = clean(middle)
        bottom_cleaned   = clean(bottom)

        with open("download/"+site+"/cleaned/"+site+"-"+str(i+1)+"-cleaned.html", 'w', encoding="utf8") as out:
            
            out.write("<url>")
            out.write(url)
            out.write("</url>\n\n")

            out.write("<title>")
            out.write(title_cleaned)
            out.write("</title>\n\n")

            out.write("<top>")
            out.write(top_cleaned)
            out.write("</top>\n\n")
            
            out.write("<middle>")
            out.write(middle_cleaned)
            out.write("</middle>\n\n")

            out.write("<bottom>")
            out.write(bottom_cleaned)
            out.write("</bottom>")
            

            out.close()
            os.system('cls')
    except:
        sys.exit(1)

print(total_documents, " document(s) saved in: /download/"+site+"/cleaned\n")
end = time.time()
# print(end - start)
