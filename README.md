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

The Python code is [on GitHub](https://github.com/VirologyCharite/gb2seq).

## Overview

There is a library of code and four general-purpose command-line scripts
that use the library.

Examine unannotated genomes, or just the reference.

### Provided scripts

* `describe-feature.py`
* `describe-site.py`
* `describe-genome.py`
* `annotate-genome.py`

## Examine features

Use `describe-feature.py` to list feature names:

```sh
$ describe-feature.py --names --sars2
$ describe-feature.py --names --reference mpox.gb
```

```
Reference:
  Thymidine kinase:
    start: 78486
    stop: 79019
    length (nt): 534
    product: Thymidine kinase
    note: Taxonomic breadth: poxvirinae; Old product: MPXVgp086; thymidine kinase; similar to VACV-WR L2R and VACV-Cop J2R
    feature is translated left-to-right.
    sequence: ATGAACGGCGGACATATTCA...
    length (aa): 178
    translation: MNGGHIQLIIGPMFSGKSTE...
```

Or examine a specific feature:

```sh
$ describe-feature.py --name spike --sars2
$ describe-feature.py --name spike --sars2 --genome CSpecVir9290.fasta
```

## What's at a certain genome location?

Use `describe-site.py` to find out. Specify a site via:

* Use and absolute full-genome location or one that's relative to a feature
* Use nucleotide or amino acid numbering

## describe-genome.py: Examine the genome

## Roll your own

It's easy to write your own scripts. E.g., `get-sar2-spike.py`
