#last modified: 08/01/2021
from bs4 import BeautifulSoup as bs
import os
import sys

total_documents = 0
try:
    total_documents = int(sys.argv[1])
except:
    print("\nERROR : Number of documents not found")
    print("Example : py ",sys.argv[0]," 1000")
    exit()
try:
    for i in range(total_documents):
        print(i+1 , "/",total_documents ,"documents scrapped")
        with open("../download/kompas/source/kompas-" +str(i+1)+ ".html",'r', encoding="utf8") as data:
            soup = bs(data,'html.parser')
            data.close()

            #mengambil title
            title = soup.title

            #mengambil url
            url = soup.find('link', rel="canonical").get('href')

            #mengambil article
            article = soup.body.find('div',class_="read__content").find_all('p')
            twitter = soup.find('blockquote',class_="twitter-tweet")
            if twitter: twitter.decompose()
            article_list = []

            #loop ini untuk hapus tag <strong> yang berisi teks yg tidak diperlukan
            for p in article:
                strong = p.find('strong')
                if(strong): strong.decompose()
                            
                article_list.append(p.text)
                # "Baca Juga:" yang tidak didalam <strong> tidak terhapus 

            #convert list > string
            article_string = ''.join(article_list)
            article_string = article_string.replace(' ''-'' ', '')
            
            #pembagi artikel       
            top = []
            middle = []
            bottom = []
            length = len(article_string) #jumlah karakter

            #persentase jumlah karakter per bagian (top, mid, bottom)

            part1 = round(20/100*length) # = 20%
            part2 = round(40/100*length) # = 40%
            # part3 = length - part1 + part2 
            
            extra = 0 #untuk cari titik (.)
            #top
            for x in range(part1):
                top.append( article_string[x] )
                while(top and x >= part1-1):
                    top.append( article_string[x+1] )
                    x += 1
                    extra += 1
                    if( top[-1] == '.' and not article_string[x+1].isdigit()):break

            extra2 = 0
            #middle
            for x in range( (part1 + extra), (part1 + part2) ):
                middle.append( article_string[x] )
                next = article_string[x+1]
                while(middle and x >= (part1 + part2 - 1)):
                    middle.append( article_string[x+1] )
                    x += 1
                    extra2 += 1
                    if( middle[-1] == '.' and not article_string[x+1].isdigit()):break

            #bottom
            for x in range( (part1 + part2  + extra2), length):
                bottom.append( article_string[x] )
                while(bottom and x >= (length-1) and bottom[-1] != '.'):
                    bottom.pop(-1)
                    

        #pembuatan file baru setelah dipilah
        with open("../download/kompas/scrapped/kompas-"+ str(i+1)+ "-bersih.html", 'w', encoding="utf8") as scrapped_html: #kalau encoding dihapus, error di loop ke 434

            scrapped_html.write("<url>" + url + "</url>\n\n")

            scrapped_html.write("<title>" + title.text + "</title>\n\n")

            scrapped_html.write("<top>")
            for text in top:
                scrapped_html.write(text)
            scrapped_html.write("</top>\n\n")

            scrapped_html.write("<middle>")
            for text in middle:
                scrapped_html.write(text)
            scrapped_html.write("</middle>\n\n")

            scrapped_html.write("<bottom>")
            for text in bottom:
                scrapped_html.write(text)
            scrapped_html.write("</bottom>")

        scrapped_html.close()

        os.system('cls')
    print("Complete.")
    print(total_documents, " document(s) saved in: /download/kompas/scrapped\n")
except:
    print("Hanya ditemukan ", i , " dokumen")
    exit()
