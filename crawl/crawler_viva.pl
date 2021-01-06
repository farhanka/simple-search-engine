use strict;
use warnings;
use POSIX qw(strftime);
use feature 'state';
use WWW::Mechanize;
use feature qw(say);

sub genDate{
    return my $date = strftime "$_[0]", localtime time()-($_[1]*24*60*60);
}

my $mech = WWW::Mechanize->new();
my @all_urls;
my %news_links;
my $total_artikel = 0;
my $url = "";

my $fileName = $ARGV[1] or 
die "\nArgumen tidak valid. \nperl [nama_file] [hari] [file_output] \nContoh : perl $0 5 output.txt\n";
open OUT, ">$fileName" or die "Tidak Bisa Membuat File!";

my $total_days = int($ARGV[0]) or 
die "\nArgumen tidak valid. \nperl [nama_file] [hari] [file_output] \nContoh : perl $0 5 output.txt\n";

print "\nMemulai pendataan tautan...\n";

HERE: for (my $i=0; $i<=$total_days; $i++){ #variabel $input harus dicasting ke int agar looping berjalan

    my $date = genDate("%Y-%m-%d", $i); 

    #memisahkan tanggal - bulan - tahun pada variabel masing-masing.
    (my $year, my $month, my $day) = split /-/, $date;
    print "Crawling data pada : $date\n";

    my $page;

    # for ($page=1; $page<=1; $page++){
        #url ini adalah pola index url dari viva.co.id
        $url = "https://www.viva.co.id/indeks/berita/all/$year/$month/$day?type=art";
        $mech->get($url);
        @all_urls = $mech->links();
        
        foreach my $link (@all_urls){
            my $url = $link->url;
                # saring url berita

                    if (($url =~ "https://www.viva.co.id/berita/bisnis/" || 
                         $url =~ "https://www.viva.co.id/berita/nasional/" ||
                         $url =~ "https://www.viva.co.id/berita/metro/")  && 
                         !exists $news_links{$link->url}){
                        $total_artikel++;
                        $news_links{$url} = 1;
                        if($total_artikel == 1000){
                                    last HERE;
                        }
                    }
        } #akhir looping untuk array all_urls
    # } #akhir looping halaman
} #akhir looping tanggal

print "Menyimpan $total_artikel tautan...\n";
sleep(5);

foreach (keys %news_links) {
    say OUT $_;
}
print "$total_artikel tautan tersimpan di \"$fileName\"\n";;
close OUT;