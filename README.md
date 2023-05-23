# Using gb2seq to work with unannotated viral genomes based on a GenBank reference

## The problem

You have unannotated genomes and need to compare them to an annotated
reference.

We faced this problem regularly in recent years, first with SARS-CoV-2
pandemic and then with mpox.

This might be processing 15 million SARS-CoV-2 genomes. It might be
processing consensus sequences from 10 hospital mpox samples (with over 200
genes).  E.g., examine a particular gene or region for NT or AA changes,
indels, genome position, etc.

This is challenging because to work with genome features you need to align
against something that is annotated before you can even begin.

Making a multiple sequence alignment may be risky. Better to examine an
optimal alignment of each unannotated genome with the reference.

You can work with a GUI tool, e.g., Geneious, but that approach is manual,
slow, can be error prone, and definitely does not scale.

## Code and installation

```sh
$ pip install gb2seq
```

The Python code: [https://github.com/VirologyCharite/gb2seq](https://github.com/VirologyCharite/gb2seq)

This talk [https://github.com/VirologyCharite/valencia-gb2seq-talk](https://github.com/VirologyCharite/valencia-gb2seq-talk)

## Overview

There is a library of code and four general-purpose command-line scripts
that use the library.

Examine unannotated genomes, or just the reference.

### Provided scripts

* `describe-feature.py`
* `describe-site.py`
* `describe-genome.py`
* `annotate-genome.py`

Hint: use `--aligner edlib` for much faster results.

## Examine features

Use `describe-feature.py` to list feature names:

```sh
$ describe-feature.py --names --sars2
$ describe-feature.py --names --reference mpox.gb
```

Or examine a specific feature:

```sh
$ describe-feature.py --name spike --sars2
```

Also examine an unannotated genome:

```sh
$ describe-feature.py --name spike --sars2 --genome sars-2-genome.fasta
```

An mpox example:

```sh
$ describe-feature.py --reference mpox.gb --name 'Thymidine kinase' --genome mpox-genome.fasta --aligner edlib
Reference:
  Thymidine kinase:
    start: 78486
    stop: 79019
    length (nt): 534
    product: Thymidine kinase
    note: Taxonomic breadth: poxvirinae; Old product: MPXVgp086; thymidine kinase; similar to VACV-WR L2R and VACV-Cop J2R
    feature is translated left-to-right.
    sequence: ATGAACGGCGGACATATTCAGTTGATAATCGGCCCCATGTTTTCAGGTAAAAGTACAGAATTAATTAGACGAGTTAGACG...
    length (aa): 178
    translation: MNGGHIQLIIGPMFSGKSTELIRRVRRYQIAQYKCVTIKYSNDNRYGTGLWTHDKNNFAALEVTKLCDVLEAITDFSVIG...
  Genome ChVir28389:
    start: 78547
    stop: 79080
    length (nt): 534
    sequence: ATGAACGGCGGACATATTCAGTTGATAATCGGCCCCATGTTTTCAGGTAAAAGTACAGAATTAATTAGACGAGTTAGACG...
    translation: MNGGHIQLIIGPMFSGKSTELIRRVRRYQIAQYKCVTIKYSNDNRYGTGLWTHDKNNFAALEVTKLCDVLEAITDFSVIG...
```

## What's at a certain genome location?

Use `describe-site.py` to find out. Specify a site via:

* Locations can be in the full-genome or relative to a feature
* Use nucleotide or amino acid numbering

```sh
$ describe-site.py --sars2 --site 23063
{
    "alignmentOffset": 23063,
    "featureName": "surface glycoprotein",
    "featureNames": [
        "surface glycoprotein"
    ],
    "reference": {
        "aa": "N",
        "aaOffset": 500,
        "codon": "AAT",
        "frame": 0,
        "id": "NC_045512.2",
        "ntOffset": 23063
    }
}
```

Site relative to a feature (`--feature spike --relative`):

```sh
$ describe-site.py --sars2 --site 1501 --feature spike --relative
{
    "alignmentOffset": 23063,
    "featureName": "surface glycoprotein",
    "featureNames": [
        "surface glycoprotein"
    ],
    "reference": {
        "aa": "N",
        "aaOffset": 500,
        "codon": "AAT",
        "frame": 0,
        "id": "NC_045512.2",
        "ntOffset": 23063
    }
}
```

With amino acid numbering (via `--aa`):

```sh
$ describe-site.py --sars2 --site 501 --feature spike --relative --aa
{
    "alignmentOffset": 23063,
    "featureName": "surface glycoprotein",
    "featureNames": [
        "surface glycoprotein"
    ],
    "reference": {
        "aa": "N",
        "aaOffset": 500,
        "codon": "AAT",
        "frame": 0,
        "id": "NC_045512.2",
        "ntOffset": 23063
    }
}
```

With an unannotated genome (via `--genome alpha-genome.fasta`):

```sh
$ describe-site.py --sars2 --site 501 --relative --feature spike --aa --genome alpha-genome.fasta
{
    "alignmentOffset": 23063,
    "featureName": "surface glycoprotein",
    "featureNames": [
        "surface glycoprotein"
    ],
    "genome": {
        "aa": "Y",
        "aaOffset": 497,
        "codon": "TAT",
        "frame": 0,
        "id": "EPI_ISL_601443 hCoV-19/England/MILK-9E05B3/2020",
        "ntOffset": 22991
    },
    "reference": {
        "aa": "N",
        "aaOffset": 500,
        "codon": "AAT",
        "frame": 0,
        "id": "NC_045512.2",
        "ntOffset": 23063
    }
}
```

The above is the `N501Y` change in the Alpha variant.

## Examine the genome

Use `describe-genome.py`.

Extract the SARS-CoV-2 spike from an unannotated genome, as amino acids:

```sh
$ describe-genome.py --sars2 --genome alpha-genome.fasta --feature spike --printAaSequence --quiet
```

Extract feature sequences as nucleotides and amino acids into separate file
and save comparisons to the reference:

```sh
$ describe-genome.py --sars2 --genome alpha-genome.fasta --outDir /tmp/out \
    --feature spike --feature n --printNtSequence --printAaSequence \
    --printAaMatch --printNtMatch
```

## Annotate a genome

```sh
$ annotate-genome.py --aligner edlib --reference mpox.gb --genome mpox-genome.fasta
```

## Roll your own

It's easy to write your own scripts. E.g., `get-sar2-spike.py`
