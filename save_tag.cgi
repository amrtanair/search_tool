#! /pkg/qct/bin/perl

#/pkg/qct/software/perl/q3_04/bin/perl

use CGI;
print "Content-type: text/html\n\n";
my $list = new CGI;

print "<HTML><HEAD><TITLE>Addresss Book Search Results</TITLE></HEAD>\n";
print "<style>";
print "body {color:#000;
   margin:0;
   overflow-y:scroll
   font-family: courier;
   border: 1px solid #eee;
   padding: 2px;}";
print "h3   {color: blue;}";
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
$query = $FORM{url};
$replace =$FORM{query};

#Among the search tag replace space and comma in to comma to make it uniform
$querytmp = $FORM{query};
my $file = "/prj/vlsi/pete/ptetools/dev/tss/tdocs/tooldocs/tags.csv";
@resultdata=();
$querytmp =~ s/ /,/; #make space and commas in to just commas
my $result = index($querytmp, ',');
@list=();

if($result != -1) 
{
#@list  =  split /','/, $querytmp;
@list  =  split (',', $querytmp);
}
else
{
	push(@list,$querytmp);
}

my @findPart;
my $file = "/prj/vlsi/pete/ptetools/dev/tss/tdocs/tooldocs/tags.csv";

my @line = qx(grep -i $query $file); # look for the user search tags in the tags file
my $split = "@@";
if(@line[0] ne "")
{
    @findPart  =  split ('@@', @line[0]);
    $find = "@@" . @findPart[1]; #"@@"
	$find =~ s/^\s+|\s+$//g; #trim the space
   	$find    =~ s/\//\\\//g; #prepend \\ to accept the special characters
   	$find    =~ s/\:/\\\:/g;
   	$find    =~ s/\@/\\\@/g;
   	$find    =~ s/\-/\\\-/g;
   	$find    =~ s/\!/\\\!/g;
   	$find    =~ s/\?/\\\?/g;
   	$find    =~ s/\</\\\</g;
   	$find    =~ s/\>/\\\>/g;
   	$find    =~ s/\$/\\\$>/g;
   	$find    =~ s/\&/\\\&/g;
   	$find    =~ s/\+/\\\+/g;
   	$find    =~ s/\,/\\\,/g;
   	$find    =~ s/\;/\\\;/g;
   	$find    =~ s/\=/\\\=/g;
   	$find    =~ s/\%/\\\%/g;
   	$find    =~ s/\{/\\\{/g;
   	$find    =~ s/\}/\\\}/g;
   	$find    =~ s/\^/\\\^/g;
   	$find    =~ s/\~/\\\~/g;
   	$find    =~ s/\[/\\\[/g;
   	$find    =~ s/\]/\\\]/g;
   	$find    =~ s/\`/\\\`/g;
	
	#Include only the newly added tags and skip the old
	foreach $key (@resultdata)
	{
	
			$result = index($replace,$key);
			if($result = -1)
			{
				
			}
			$grepStr = $grepStr . "grep -i " . $key ." | ";
	}

	
	$replace = "," . $replace . $find;
	
	my $cmd = "perl -pi.back -e 's/$find/$replace/g;' $file";

	system($cmd) == 0
	    or die "Couldn't launch [$cmd]: $! / $?";
	print "</p>$FORM{query} Updated Successfully</p>";
 }
else
{
	open(my $fh, '>>', $file) or die "Could not open file '$file' $!";
	print $fh "\n$FORM{query}" . "@@" . "$FORM{url}";
	close $fh;
	print $cmd;
	print "</p>$find Added Successfully</p>";
}
print "</BODY></HTML>";