use strict;
use warnings;
use FindBin qw( $RealBin );

my $currentpath = $RealBin;
my %hash;
my $filename = $ARGV[0] or die "\nArgumen tidak valid.\n> perl [file_sumber_link]\nContoh: perl output.txt\n";

open (my $fh, '<:encoding(UTF-8)', $filename) or die "\nFile gagal dibuat!\n";

my $x=0, my $y=586;
while (my $row = <$fh>){
    chomp($row);

    if ($row =~ "https://news.detik.com/" && $y <= 1000){
        `wget -O ../download/detik/source/detik-$y.html $row`;
	    $y++;

    }elsif($row =~ "https://www.jpnn.com/" && $y <= 1000){
        `wget -O ../download/jpnn/source/jpnn-$y.html $row`;
	    $y++;

    }elsif($row =~ "https://www.kompas.com/" && $y <= 1000) {
        `wget -O ../download/kompas/source/kompas-$y.html $row`;
	    $y++;
    }else{
        print "Nothing happen";
        last;
    }
}