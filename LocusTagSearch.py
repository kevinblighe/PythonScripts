
import sys
import argparse
     
from Bio import Entrez, SeqIO
from xml.dom import minidom
     
parser = argparse.ArgumentParser(description='Specify a field of NCBI locus tags, which get looked up in RefSeq for a corresponding gene name, which is appended to the line.')
     
parser.add_argument('-f', action='store', dest='locus_tag_col_str', required=True, help='The locus tag field in the tab-delimited input file.')
parser.add_argument('-e', action='store', dest='email_address', required=True, help='Entrez requires your email address.')
parser.add_argument('infile_name', help='Input file')
     
args = parser.parse_args()
     
Entrez.email = args.email_address

locus_tag_col = int(args.locus_tag_col_str) - 1
     
with open(args.infile_name, 'r') as infile:
	for line in infile:
        	gene_name = '-'

		locus_tag = line.split()[locus_tag_col]

		search_term = 'refseq[FILTER] AND {}'.format(locus_tag)

		handle = Entrez.esearch(db='nuccore', term=search_term)

		results = Entrez.read(handle)

		handle.close()

		for id in results['IdList']:
			print id

			handle = Entrez.efetch(db='nuccore', id=id, retmode='txt')

			print handle.read
