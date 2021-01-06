#last modified: 29/10/2020
from bs4 import BeautifulSoup as bs
import os


total_documents = 30
for i in range(total_documents):
    print(i+1 , "/",total_documents ,"documents scrapped")
    with open("../download/detik/source/detik-" +str(i+1)+ ".html",'r', encoding="utf8") as data:
        soup = bs(data,'html.parser')
        data.close()

        #mengambil title
        title = soup.title

        #mengambil url
        url = soup.find('link', rel="canonical").get('href')

        #mengambil article
        article = soup.find('div',class_="itp_bodycontent").find_all('p')
        article_list = []

        junk_words = ["KOMPAS.com","Baca Juga:","Baca juga: ","Baca Juga: ","Baca Juga:","Baca juga:",
                     'Baca Juga:\xa0', 'Baca juga:\xa0']

        #loop ini untuk hapus tag <strong> yang berisi teks yg tidak diperlukan
        for p in article:
            strong = p.find('strong')
            if(strong): strong.decompose()
                        
            article_list.append(p.text)
            # "Baca Juga:" yang tidak didalam <strong> tidak terhapus 

        #convert list > string
        article_string = ''.join(article_list)
        
        #pembagi artikel       
        top = []
        middle = []
        bottom = []
        length = len(article_string) #jumlah karakter

        #persentase jumlah paragraf per bagian (top, mid, bottom)

        part1 = round(20/100*length) # = 20%
        part2 = round(40/100*length) # = 40%
        # part3 = length - part1 + part2 
        
        extra = 0 #untuk cari titik (.)
        #top
        for x in range(part1):
            top.append( article_string[x] )
            while( x >= part1-1 and top[-1] != '.'):
                top.append( article_string[x+1] )
                x += 1
                extra += 1

        extra2 = 1
        #middle
        for x in range( (part1 + extra), (part1 + part2) ):
            middle.append( article_string[x] )
            while( x >= (part1 + part2 - 1) and middle[-1] != '.'):
                x += 1
                middle.append( article_string[x+1] )
                extra2 += 1

        #bottom
        for x in range( (part1 + part2  + extra2), length):
            bottom.append( article_string[x] )
            while( x >= (length-1) and bottom[-1] != '.'):
                bottom.pop(-1)
                

    #pembuatan file baru setelah dipilah
    with open("../download/detik/cleaned/detik-"+ str(i+1)+ "-bersih.html", 'w', encoding="utf8") as cleaned_html: #kalau encoding dihapus, error di loop ke 434

        cleaned_html.write("<url>" + url + "</url>\n\n")

        cleaned_html.write("<title>" + title.get_text() + "</title>\n\n")

        cleaned_html.write("<top>")
        for text in top:
            cleaned_html.write(text)
        cleaned_html.write("<top>\n\n")

        cleaned_html.write("<middle>")
        for text in middle:
            cleaned_html.write(text)
        cleaned_html.write("</middle>\n\n")

        cleaned_html.write("<bottom>")
        for text in bottom:
            cleaned_html.write(text)
        cleaned_html.write("</bottom>")

    cleaned_html.close()

    os.system('cls')

print(total_documents, "scrapped documents stored in /download/detik/cleaned/\n")
