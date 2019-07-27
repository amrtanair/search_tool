#! /pkg/qct/software/perl/q3_04/bin/perl
print "Content-Type: text/html\n\n";

my $urlStr = 'Mathi';
my $topic;
my $value;
my $user_name = $ENV{REMOTE_USER};
$user_name =~ s/\@.+$//g;
my $host_address = $ENV{REMOTE_ADDR};
$host_address =~ s/\./\_/g;
if (length ($ENV{'QUERY_STRING'}) > 0){
      $buffer = $ENV{'QUERY_STRING'};
      @pairs = split(/&/, $buffer);
      foreach $pair (@pairs){
           ($name, $value) = split(/=/, $pair);
           $value =~ s/%([a-fA-F0-9]["#"][a-fA-F0-9])/pack("C", hex($1))/eg;
           $in{$name} = $value; 
      }
	$topic = $in{'url'};
	$topic =~ s/:/\_cln_/g;
	$topic =~ s/\//_sls_/g;
	$topic = "/prj/vlsi/pete/ptetools/dev/tss/tdocs/tooldocs/tags/" . $topic . ".tag";
	
	unless (-e $topic) {
	open(DATA1,'>>',$topic) || die "Couldn't open file file.txt, $!";
	close DATA1;
	}
}
else	
{
	$topic = "/prj/vlsi/pete/ptetools/dev/tss/tdocs/tooldocs/tags/" . $user_name . ".tag";
	$value = 'welcome.cgi';
}
	print "<html> <head>\n";
	print "<title>Tool Documentation..</title>";
	print "</head>\n";
	print "<frameset rows = '15%,85%' onLoad='testOnload()'>\n";
	print "<frame id = 'top' name = 'top' src = './dev/tdocs/test2_main.cgi?a=$topic' scrolling='no' noresize='noresize' class='borderless' frameborder='no' border='0' framespacing='0' frameborder='no'/>\n";
	print "<frame id = 'main' name = 'main' src = '$value' frameborder='no' border='0' framespacing='0' marginheight='0' marginwidth='0' scrolling='auto' class='borderless'/>\n";
	print "</frameset>\n";
	print "</html>\n";

