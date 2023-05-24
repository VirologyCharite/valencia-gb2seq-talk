#!/usr/bin/env python

import argparse
from dark.reads import addFASTACommandLineOptions, parseFASTACommandLineOptions

from gb2seq.alignment import Gb2Alignment, addAlignerOption
from gb2seq.features import Features


parser = argparse.ArgumentParser(
    description=("Read SARS-2 FASTA from standard input. "
                 "Write the spike gene in amino acids as FASTA."))
addAlignerOption(parser)
addFASTACommandLineOptions(parser)
args = parser.parse_args()

features = Features(sars2=True)

for record in parseFASTACommandLineOptions(args):
    alignment = Gb2Alignment(record, features)
    genomeAa, genomeNt = alignment.aaSequences("spike")
    print(genomeAa.toString("fasta"), end="")
