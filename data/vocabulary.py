#########################################
# vocabulary.py
#
#
#
#########################################

import collections
import Bio.SeqIO

# Open source Files
source_train_file = open("source_train.txt", 'r')
target_train_file = open("target_train.txt", 'r')
source_test_file = open("source_test.txt", 'r')
target_test_file = open("target_test.txt", 'r')


# Create counter objects
source_count = collections.Counter()
target_count = collections.Counter()

# source train count loop.
for source_line in source_train_file.readlines():
    for word in source_line.split():
        source_count[word] += 1
source_train_file.close()

# source test count loop.
for source_line in source_test_file.readlines():
    for word in source_line.split():
        source_count[word] += 1
source_test_file.close()



# target train count loop.
for target_line in target_train_file.readlines():
    for word in target_line.split():
        target_count[word] += 1
target_train_file.close()

for target_line in target_test_file.readlines():
    for word in target_line.split():
        target_count[word] += 1
target_train_file.close()




# Make vocabulary files.
source_vocab = open("source_vocab.txt", 'w')
target_vocab = open("target_vocab.txt", 'w')


# source train
for word in source_count.most_common():
    source_vocab.write(word[0] + "\t" + str(word[1]) + "\n")


# target train
for word in target_count.most_common():
    target_vocab.write(word[0] + "\t" + str(word[1]) + "\n")

