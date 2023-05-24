#!/usr/bin/env python

import argparse
from dark.reads import addFASTACommandLineOptions, parseFASTACommandLineOptions

from gb2seq.alignment import Gb2Alignment, addAlignerOption
from gb2seq.features import Features
from gb2seq.checker import AAChecker, NTChecker

parser = argparse.ArgumentParser(
    description="Check SARS-CoV-2 FASTA for specific substitutions."
)
addAlignerOption(parser)
addFASTACommandLineOptions(parser)
args = parser.parse_args()

features = Features(sars2=True)

checker = AAChecker("spike", "N501Y")

for record in parseFASTACommandLineOptions(args):
    alignment = Gb2Alignment(record, features)
    if checker(alignment):
        print("N501Y substitution found in", record.id)


# Additional (unused) ways to check genome are shown below.

# Various other logical checkers:

checker = (
    AAChecker("spike", "N501Y") & AAChecker("spike", "69-") & AAChecker("spike", "70-")
)
checker = AAChecker("spike", "N501Y") & AAChecker("spike", "A570D")
checker = AAChecker("spike", "N501Y") | AAChecker("spike", "A570D")

# Check for specific nucleotide changes in the nucleocapsid and amino acid
# changes in the spike:

checker = (
    NTChecker("N", "G7C A8T T9A G608A G609A G610C C704T") &
    AAChecker("S", "N501Y H69- V70- Y144-")
)

# Checking many things at once, wanting to know which checks passed or failed
# and what was in the genome at the given locations.

# Note that we use 501Y in the following, not N501Y, since we might just
# want to check that something is in the genome without knowing or caring
# about what's in the reference.

alignment.checkFeature('spike', '501Y 69- 70-', aa=True)
(3,
 0,
 {'501Y': (True, 'N', True, 'Y'),
  '69-': (True, 'H', True, '-'),
  '70-': (True, 'V', True, '-')})
