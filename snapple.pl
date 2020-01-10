use strict;
use warnings;
use English;
use DBI;
use LWP::UserAgent;
use v5.16;

# Setting User Agent and Scraping Snapple's website.
my $ua = LWP::UserAgent->new;
$ua->timeout(30);
$ua->agent('Mozilla/5.0');
my $response = $ua->get('https://www.snapple.com/real-facts');

# Regex to grab the snapple number and fact.
sub scrape {
	my @fact_arr = $response->decoded_content =~ 
				m/<a href="\/real-facts\/(\d+)">([^<>]+)/g;
	return @fact_arr;
}

my @fact_arr = scrape();
my $dbname = "snapple.db";
my $dbh = DBI->connect("dbi:SQLite:dbname=$dbname", "", "");
my ($i, $n) = (1, 0);
while ($n < 1999) {
	# Parsing the raw data from FACT_ARR and placing it into a database
	# with columns:
		# Number -> The Snapple Fact Number.
		# Fact -> The actual Snapple Fact.
		# Redacted -> Boolean, if 0 it's still on the snapple website
			# if 1, the fact has been redacted and no longer appears as
			# a snapple fact on snapple's website.
	if ($i != $fact_arr[$n]) {
		my $stmt = 'INSERT INTO snapple_facts (number, redacted) 
				VALUES (?, ?)';
		my $sth = $dbh->prepare($stmt);
		$sth->execute($i, 1);
	} else {
		my $stmt = 'INSERT INTO snapple_facts 
				(number, fact, redacted) VALUES (?, ?, ?)';
		my $sth = $dbh->prepare($stmt);
		$sth->execute($fact_arr[$n++], $fact_arr[$n++], 0);
	}
	$i += 1;
}
$dbh->disconnect;
