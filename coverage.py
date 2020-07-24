import subprocess
#subprocess.check_call(['python','-m','pip','install','pybedtools'])
import argparse
import collections
from collections import Counter
import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import os
import pandas as pd
import pybedtools
import pyranges as pr
from statistics import mean,median,mode,stdev
import statsmodels.api as sm
from statsmodels.formula.api import ols
import sys
from sys import argv

class calcov():
    def __init__(self, ff, rr, ee, qq):
        self.ref = ee
        self.fwd = ff
        self.rev = rr
        self.quali = qq

    def mapd(self, fas=None, fwq=None, rvq=None):
        fas = self.ref
        fwq = self.fwd
        rvq = self.rev
        # index reference genome
        # HIV genome reference K03455.1
        os.system('bwa index -p hiv_ref -a bwtsw ' + fas)
        os.system('bwa index ' + fas)
        # align/map MiSeq forward and reverse sequences to reference
        # fastq > sam
        os.system('bwa mem ' + fas + ' ' + fwq + ' ' + rvq + ' > aln_pairs.sam')
        # sam > bam > sort > index > depth/coverage > txt
        os.system('samtools view -b -S aln_pairs.sam > aln_pairs.bam')
        os.system('samtools sort -o sorted_aln' + self.quali + '.bam aln_pairs.bam')
        os.system('samtools index sorted_aln' + self.quali + '.bam')
        os.system('samtools view -q ' + self.quali + ' -o view' + self.quali + '.bam sorted_aln' + self.quali + '.bam')
        os.system('samtools depth sorted_aln' + self.quali + '.bam > depth' + self.quali + '.txt')
        # read txt
        with open('depth' + self.quali + '.txt') as f:
            cnt = [row[2] for row in csv.reader(f,delimiter='\t')]
        with open('depth' + self.quali + '.txt') as f:
            ref = [row[1] for row in csv.reader(f,delimiter='\t')]
        # write .tsv
        qsc = np.int64(self.quali)
        df = pd.DataFrame(list(zip(ref,cnt)),columns = ['Position', 'Count'])
        tsvname = (str(qsc)+ "_coverage.tsv")
        df.to_csv(tsvname, sep='\t', index=False)
        return (ref, cnt)

    # plot counts and reference ranges
    def pltt(self):
        rff,cnn = self.mapd()
        rf=[]
        for i in rff:
            j=int(i)
            rf.append(j)
        cn=[]
        for i in cnn:
            j=int(i)
            cn.append(j)
        plt.clf()
        plt.close()
        plt.figure()
        plt.bar(rf,cn,align='edge')
        plt.tight_layout(h_pad=2.08,w_pad=2.08,rect=[1, 1, 1, 1])
        plt.xticks(np.arange(0,len(rf)+100,step=1000))
        plt.yticks(np.arange(0,len(cn)+100,step=1000))
        plt.xlabel('Reference Range', fontsize=10)
        plt.ylabel('Counts', fontsize=10)
        plt.title('Counts / Reference Range_'+ self.quali)
        plt.savefig(self.quali +'_coverage.pdf')
        return 0

parser = argparse.ArgumentParser()

parser.add_argument("-1", "--fwdfq", dest = "fwdfq")
parser.add_argument("-2", "--revfq", dest = "revfq")
parser.add_argument("-x", "--reffa", dest = "reffa")
parser.add_argument("-q", "--qual", dest = "qual")

args = parser.parse_args()

print( "forward_fastq {} reverse_fastq {} reference_fasta {} quality_threshold {} ".format(
    args.fwdfq,
    args.revfq,
    args.reffa,
    args.qual
))

a = args.fwdfq
b = args.revfq
c = args.reffa
d = args.qual

action = calcov(a,b,c,d)
action.pltt()

# python coverage.py -1 SRR961514.1_1.fastq -2 SRR961514.1_2.fastq -x ref_sequence.fasta -q 10