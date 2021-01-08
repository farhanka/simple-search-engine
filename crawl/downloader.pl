use strict;
use warnings;
use FindBin qw( $RealBin );

my $currentpath = $RealBin;
my %hash;
my $filename = $ARGV[0] or die "\nArgumen tidak valid.\n> perl downloader.pl [file_sumber_link]\nContoh: perl downloader.pl output.txt\n";

open (my $fh, '<:encoding(UTF-8)', $filename) or die "\nFile gagal dibuat!\n";

my $x=0, my $y=1;
while (my $row = <$fh>){
    chomp($row);

    if ($row =~ "https://news.detik.com/" && $y <= 1000){
        `wget -O ../download/detik/source/detik-$y.html $row`;
	    $y++;

    }elsif($row =~ "https://www.viva.co.id/" && $y <= 1000){
        `wget -O ../download/viva/source/viva-$y.html $row`;
	    $y++;

    }elsif($row =~ "https://www.kompas.com/" && $y <= 1000) {
        `wget -O ../download/kompas/source/kompas-$y.html $row`;
	    $y++;
    }else{
        print "Nothing happen";
        last;
    }
}
