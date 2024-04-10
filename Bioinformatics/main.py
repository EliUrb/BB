from DNAToolkit import *
from DNAseq import *
import random

#generate random DNA
rndDNAstr=''.join([random.choice(dnaNucleotides)
                   for nuc in range(50)])

#validate that input is DNA
dnaStr = (validateSeq(rndDNAstr))

#use imported DNA
#print(importedDNA)
#print(countNucFreq(importedDNA))
#print(rnaMap(importedDNA))
#print(proMAP(importedDNA))

print(countNucFreq(dnaStr))
print(dnaStr)
print(rnaMap(dnaStr))
print(proMAP(dnaStr))