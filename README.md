# Genomic Sequence Analysis Pipeline

A complete Python pipeline for DNA sequence analysis.
Reads a FASTA file, validates every sequence, 
analyzes each one and writes a full report.

## Features
- FASTA file parsing
- Sequence validation — length, characters, empty check  
- GC% calculation and classification
- Complement strand generation
- Nucleotide frequency analysis
- Full report written to file
- Error handling throughout — never crashes
- Pipeline summary with average GC% and highest GC gene

## How to run
python genome_pipeline.py

## Input
FASTA format file — sequences.fasta.txt

## Output
**- Summary printed to screen**
invalid character
seq length too short
Total sequences: 6
Valid sequences: 4
Average GC%: 58.44
Highest GC gene: EGFR_human
Highest GC%: 70.0

**- Full report saved to report.txt**

## Concepts used
Variables, operators, conditionals, loops, 
strings, data structures, functions, 
file handling, list comprehensions, error handling
