
import sys
import argparse

from Bio import Entrez

parser = argparse.ArgumentParser(description='Searches for a human protein sequence by any provided ID or accession number.')
parser.add_argument('-f', action='store', dest='SearchTerms', required=True, help='The column number containing the search terms in the provided file (starting at 1).')
parser.add_argument('-e', action='store', dest='EmailAddress', required=True, help='Entrez requires your email address.')
parser.add_argument('InputFile', help='Input file')

arguments = parser.parse_args()

Entrez.email = arguments.EmailAddress

iSearchTerm_Col = int(arguments.SearchTerms) - 1

with open(arguments.InputFile, 'r') as InputFile:

	for line in InputFile:
		
		LookupTerm = line.split()[iSearchTerm_Col]

		LookupCommand = 'refseq[FILTER] AND txid9606[Organism] AND {}'.format(LookupTerm)

		handle = Entrez.esearch(db='protein', term=LookupCommand)

		results = Entrez.read(handle)

		handle.close()

		print(results)

		#Lookup the FASTA sequence for each protein by its GeneInfo Identifier (GI) number
		for gi in results['IdList']:
			handle = Entrez.efetch(db='protein', id=gi, rettype='fasta')
			
			print(handle.read())
			
			handle.close()
