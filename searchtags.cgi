#! /pkg/qct/software/perl/q3_04/bin/perl

use CGI;
print "Content-type: text/html\n\n";
my $list = new CGI;
my @resultdata;
my @list;
my $rescount=0;
my $grepStr="";
print "<HTML><HEAD><TITLE>Addresss Book Search Results</TITLE></HEAD>\n";
print "<style>";
print "body {color:#000;
   margin:0;
   overflow-y:scroll
   font-family: courier;
   border: 1px solid #eee;
   padding: 0px;}";

print "p    {font:12px; text-indent: 30px;}";
print "a    {color: green; text-decoration:none}";
print "h2 {
    text-align: left;
    color: #999;
    font-size: 18px;
    padding-left: 8px;
    margin: 10px 0 10px 0;
}";
print "h4 {color: #0052FF; text-decoration: none; text-indent: 30px;}";
print "h3 {
    color: #3083A3;
    text-decoration: none;
    
}";
print "</style>";
print "<BODY>";


local ($buffer, @pairs, $pair, $name, $value, %FORM);
# Read in text
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "GET") {
   $buffer = $ENV{'QUERY_STRING'};
}

# Split information into name/value pairs
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
   ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}

$query = $FORM{query};
my $file = "/prj/vlsi/pete/ptetools/dev/tss/tdocs/tooldocs/tags.csv";
@resultdata=();
$query =~ s/ /,/g; #make space and commas in to just commas
my $result = index($query, ',');
@list=();

if($result != -1) 
{
#@list  =  split /','/, $query;
@list  =  split (',', $query);
}
else
{
	push(@list,$query);
}

my $size = @list;
if($size > 1)
{
	foreach $key (@list)
	{
	
			$grepStr = $grepStr . "grep -i " . $key ." | ";
	}
	$grepStr = substr($grepStr, grepStr.length(), -2);
	@resultdata=();
	@resultdata= qx(more $file | $grepStr );
}
else
{
$grepStr = @list[0];
@resultdata=();
@resultdata= qx(grep -i $grepStr $file);
}
#print "last:  $grepStr\n";
my $user_name = $ENV{HTTP_SM_USER};


$rescount = @resultdata;

#print "<h2>Hi $user_name,<br>  About  $rescount results </h2><br>";
if ($rescount>1) {print "<h2>About $rescount results found</h2><br>";}
else {print "<h2>About  $rescount result found</h2><br>";}
my $timestamp = localtime(time);
file_append("$user_name $timestamp $query");
print "<table width=100%>";
#print "<tr><th>Search Result</th></tr>";
foreach $i (@resultdata) {


	my @words = split /@@/, $i;
	my $link1 = @words[0];
	my $header = @words[1];
	print "<tr><td>";
	print "                            <h2><a href=\"$header\" target=\"main\">$header</a></h2>";
	print "                            <p>Tags: $link1</p>";
	
	print "</td></tr>";
	print "<tr><td>";
	print "</td></tr>";

}
print "</table>";

sub file_append {
	my $data = shift;
	my $file = "/prj/vlsi/pete/ptetools/dev/tss/tdocs/tooldocs/tooldocs.log";
	open(my $fh, '>>', $file) or die "Could not open file '$file' $!";
    print $fh "$data" . "\r\n";
	close $fh;
}

print "</BODY></HTML>\n";
