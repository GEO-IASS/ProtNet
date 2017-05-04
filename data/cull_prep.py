########################################
# cull_prep.py
#
#
#
#
#########################################

import Bio.SeqIO
import re

seq_file = open("ss.txt", 'r')
id_file  = open("idFile.txt", 'w')
seq_parsed = Bio.SeqIO.parse(seq_file, "fasta")

seq_filt_list = []
for sequence in list(seq_parsed):
    sequence_test = re.search(r"\S*:sequence", sequence.id)
    if sequence_test != None:
        print(sequence.id)
        id_file.write(sequence.id[0:4]  + "\n")
        seq_filt_list.append(sequence)

seq_only_file = open("sequences.txt", 'w')
Bio.SeqIO.write(seq_filt_list, seq_only_file, "fasta")
seq_only_file.close()
seq_file.close()
id_file.close()