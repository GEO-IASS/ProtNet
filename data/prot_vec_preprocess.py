#######################################
# prot_vec_preprocess.py
#
#
#
#
#######################################

import sys
import re
import random
import Bio.SeqIO

PERCENT_SPLIT = 0.10

def main():
    print("Begin Preprocessing\n")
    source_train_out = open("source_train.txt", 'w')
    target_train_out = open("target_train.txt", 'w')
    source_test_out  = open("source_test.txt", 'w')
    target_test_out  = open("target_test.txt", 'w')

    # Read in FASTA formated Proten File and split on sequence delimiter
    seq_file  = open("ss.txt", 'r')
    cull_file = open("cull_seq.txt", 'r')
    cull_seqs = Bio.SeqIO.parse(cull_file, "fasta")
    cull_list = list(cull_seqs)

    
    # Go through each sequence and remove all metadata
    seq_dict = {}
    sequences = seq_file.read().split(">")
    for sequence in sequences:
        if sequence == '':
            continue
        
        # Filter out metadata and find sequence label
        data_seq = sequence.split("\n")
        string_type = data_seq[0].split(":")[-1]
        total_string = "".join(data_seq[1:])
        
        # Replace spaces -- which represent coils -- with C
        if string_type == "secstr":
            total_string = total_string.replace(' ', 'C')
        seq_dict[data_seq[0]] = total_string
        
    
    
    for sequence in cull_list:
        print(sequence.id)
        if (sequence.id[0:4] + ":" + sequence.id[4] + ":sequence") in seq_dict:
            # Get the protein sequence and secondary structure
            secstr = seq_dict[sequence.id[0:4] + ":" + sequence.id[4] + ":secstr"]
            seqstr = seq_dict[sequence.id[0:4] + ":" + sequence.id[4] + ":sequence"]
            
            # Break protein sequences into thremers or smaller.
            threemer_list_sec = re.findall("..?.?", secstr)
            sec_string = " ".join(threemer_list_sec)
            threemer_list_seq = re.findall("..?.?", seqstr)
            seq_string = " ".join(threemer_list_seq)
            
            if random.random() > PERCENT_SPLIT:
                source_train_out.write(seq_string + "\n")
                target_train_out.write(sec_string + "\n")
        
            # Place in test dataset
            else:
                source_test_out.write(seq_string + "\n")
                target_test_out.write(sec_string + "\n")


#     sequences = seq_file.read().split(">")


#     target_list = []
#     source_list = []

#     # Go through each sequence and remove all metadata
#     for sequence in sequences:
#         if sequence == '':
#             continue
        
#         # Filter out metadata and find sequence label
#         data_seq = sequence.split("\n")
#         string_type = data_seq[0].split(":")[-1]
#         total_string = "".join(data_seq[1:])
        
#         # Replace spaces -- which represent coils -- with C
#         if string_type == "secstr":
#             total_string = total_string.replace(' ', 'C')
        
#         # Break protein sequences into thremers or smaller.
#         threemer_list = re.findall("..?.?", total_string)
#         seq_string = " ".join(threemer_list)

#         # If it is a protein sequence
#         if string_type == "sequence":
#             source_list.append(seq_string)
        
#         # If a secondary sequence string
#         elif string_type == "secstr":
#             target_list.append(seq_string)
                
    
#     # If the target_list and soure_list are not equal in size, we can not translate.
#     assert len(target_list) == len(source_list)

#     for i in range(0, len(source_list)):
#         # Place in training dataset
#         if random.random() > PERCENT_SPLIT:
#             source_train_out.write(source_list[i] + "\n")
#             target_train_out.write(target_list[i] +"\n")
        
#         # Place in test dataset
#         else:
#             source_test_out.write(source_list[i] + "\n")
#             target_test_out.write(target_list[i] + "\n")

    source_test_out.close()
    source_train_out.close()
    target_test_out.close()
    target_train_out.close()
    seq_file.close()

if __name__ == "__main__":
    main()
