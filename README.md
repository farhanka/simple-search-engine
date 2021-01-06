# simple-search-engine

Bahasa yang digunakan adalah perl dan Python

## Cara Penggunaan
1. Crawling (/crawl)
    * mengambil link dari situs
    
          - perl [nama_script] [n hari kebelakang yang ingin di crawl] [file output]
          - contoh : perl crawler_detik.pl 30 output_detik.txt
          
    * mendownload html dari link output
    
          - perl downloader.pl [file link yang sudah terbuat dari crawling]
          - contoh : perl output_detik.txt
          
2. Scrapping (/scrap) 
   
       - py [nama_script] [jumlah_dokumen]
       - contoh: py scrap_detik.py 1000
   
3. Cleaning (/):
    
         - py cleaner.py [situs] [jumlah dokumen]
         - contoh py cleaner.py detik 1000
  
4. Indexing (/) :

         - py indexing.py
    
5.  Menjalankan Flask (/)

         - py app.py
    
6. Buka 127.0.0.1/5000
     
              
  
