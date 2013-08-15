#!/usr/bin/python
# coding: utf-8

"""
File: yahooQuote.py
Retrieve quote from Yahoo with CSV API.

Example URL for Google and Facebook:
	http://download.finance.yahoo.com/d/quotes.csv?s=GOOG+FB&f=spj1

References: 
	https://code.google.com/p/yahoo-finance-managed/wiki/csvQuotesDownload
	http://greenido.wordpress.com/2009/12/22/yahoo-finance-hidden-api/

	http://pymotw.com/2/argparse/




Author: Thibaut Debruille

"""
import urllib2

PROGNAME = u"YahooQuote"


yahoo_url = 'http://download.finance.yahoo.com/d/quotes.csv?s='
csv_format = "&f=spj1"

def GetCsv(symbols):
	for symb in symbols:
		if symb.isdigit():
			print "Error, {0} is not a valid symbol.".format(symb)
			return 1

	final_url = yahoo_url + "+".join(symbols) + csv_format
	# print final_url
	csv = urllib2.urlopen(final_url).read()
	print csv

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description="Retrieve quote of given symbols from Yahoo.")

	parser.add_argument("-s", "--symbols", action="store", dest="symbols", 
						help="Symbol of the company", 
						required=True, nargs='+')
	parser.add_argument("-v", "--version", action='version', version='{0} 1.0'.format(PROGNAME))
	args = parser.parse_args()

	GetCsv(args.symbols)








