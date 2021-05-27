Coverage Mapper

To obtain a .tsv file of sequence counts for each reference position and a pdf of a histogram exhibiting these coverage counts, run coverage.py by entering in a linux terminal the following convention:

```
python coverage4.py -1 forward_sequence.fastq -2 reverse_sequence.fastq -x ref_sequence.fasta -q int(quality threshold)
```

See INSTALL.md for instructions for SRA Toolkit to separate forward and reverse sequences from a single file taken from Sequence Read Archive on NCBI.

Please refer to comments in coverage.py for details of pipeline.


Updated 5/7/21
