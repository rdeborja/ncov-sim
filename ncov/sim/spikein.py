'''
A module for handling insilico spike-in.
'''

import random

def insert_spikein(n=3):
    '''
    Boolean to insert spike-in sequence.
    '''
    return random.randint(0, n)


def write_fastq_file(fastq, output):
    '''
    Write the list of reads to a FASTQ file.
    '''
    out_p = open(output, 'w')
    for line in fastq:
        out_p.write(line)
    out_p.close()
