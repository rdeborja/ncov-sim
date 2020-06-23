#!/usr/bin/env python
'''
A program to spike in reads from another species.
'''

import sys
import argparse
import ncov.sim.spikein as spikein

parser = argparse.ArgumentParser()
parser.add_argument('--fastq1', help='FASTQ read 1 file')
parser.add_argument('--fastq2', help='FASTQ read 2 file')
parser.add_argument('--spikein1', help='Spike-in FASTQ read 1 file')
parser.add_argument('--spikein2', help='Spike-in FASTQ read 2 file')
parser.add_argument('--output1', help='output filename')
parser.add_argument('--output2', help='output filename')
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

args = parser.parse_args()

fastq1_p = open(args.fastq1, 'r')
fastq2_p = open(args.fastq2, 'r')
spike1_p = open(args.spikein1, 'r')
spike2_p = open(args.spikein2, 'r')

read1 = []
read2 = []
read_count = 0
for line in fastq1_p:
    read1.append(line)
    read1.append(fastq1_p.readline())
    read1.append(fastq1_p.readline())
    read1.append(fastq1_p.readline())
    read2.append(fastq2_p.readline())
    read2.append(fastq2_p.readline())
    read2.append(fastq2_p.readline())
    read2.append(fastq2_p.readline())
    if not spikein.insert_spikein():
        read1.append(spike1_p.readline())
        read1.append(spike1_p.readline())
        read1.append(spike1_p.readline())
        read1.append(spike1_p.readline())
        read2.append(spike2_p.readline())
        read2.append(spike2_p.readline())
        read2.append(spike2_p.readline())
        read2.append(spike2_p.readline())
spikein.write_fastq_file(fastq=read1, output=args.output1)
spikein.write_fastq_file(fastq=read2, output=args.output2)
