# Using gb2seq to work with unannotated viral genomes based on a GenBank reference

## The problem

You have unannotated genomes and need to compare them to an annotated
reference.

We faced this problem regularly in recent years, first with SARS-CoV-2
pandemic and then with mpox.

This might be processing 15M SARS-CoV-2 genomes. It might be processing
consensus sequences from 10 hospital mpox samples (with over 200 genes).
E.g., examine a particular gene or region for NT or AA changes, indels,
genome position, etc.

This is challenging because to work with genome features you need to align
against something that is annotated before you can even begin.

Making a multiple sequence alignment may be risky. Better to examine an
optimal alignment of each unannotated genome with the reference.

You can work with a GUI tool, e.g., Geneious, but that approach is manual,
slow, can be error prone, and definitely does not scale.

## Getting the code

https://github.com/VirologyCharite/gb2seq

```sh
$ pip install gb2seq
```

There is a library of Python code and four general-purpose command-line
scripts that use the library. You can easily write your own scripts.

### Scripts

* describe-site.py
* describe-feature.py
* describe-genome.py
* annotate-genome.py
* roll your own

## What's found at a certain genome location?

* Give a full genome location
* Or, a location relative to a feature
* In nucleotides or amino acids
* Examine a reference sequence and (optionally) also an unannotated genome

## Look at a feature

```sh
$ describe-feature.py --names --sars2
$ describe-feature.py --name spike --sars2 --genome ChVir9290.fasta
```

```sh
$ describe-feature.py --names --ref mpox.gb
```


## Look at the genome
