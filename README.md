# simple-search-engine

Bahasa yang digunakan adalah perl dan Python

## Cara Penggunaan
1. Crawling (/crawl)
    * mengambil link dari situs
    
          - perl [nama script] [n hari kebelakang yang ingin di crawl] [file output]
          - contoh : perl crawler_detik.pl 30 output_detik.txt
          - script yang tersedia : 
               crawler_detik.pl
               crawler_viva.pl
               crawler_kompas.pl
           
          
    * mendownload html dari link output
    
          - perl downloader.pl [file link yang sudah terbuat dari crawling]
          - contoh : perl output_detik.txt
          
2. Scrapping (/scrap) 
   
      * Mengambil data-data yang diperlukan dari dokumen html yang sudah di crawl
      
       - py [nama script] [jumlah dokumen]
       - contoh: py scrap_detik.py 1000
       - script yang tersedia : 
               scrap_detik.py
               scrap_viva.py
               scrap_kompas.py
           
   
3. Cleaning (/):
         
         * Stemming & Stopwords removing
         
         - py cleaner.py [viva/detik/kompas] [jumlah dokumen]
         - contoh py cleaner.py detik 1000
  
4. Indexing (/) :

         - py indexer.py
    
5.  Menjalankan Flask (/)

         - py app.py
    
6. Buka 127.0.0.1/5000
     
              
  
