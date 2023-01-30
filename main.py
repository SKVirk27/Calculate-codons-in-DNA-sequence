#A computer program that counts the number of occurrences of each of the
# 3-letter words “AAA”, “AAC”, ..., “TTT” in the salmonella genome file
import os
print(os.chdir(os.path.dirname(__file__))) # for common pathname.

with open("sequence.fasta") as myfile: # opening fasta file
  seq_fasta= myfile.readlines()[1:] # ignoring first description line
seq_fasta_join= [] # empty list as seq_fasta_join
for element in seq_fasta:
    seq_fasta_join.append(element.strip())# removing newline in fasta file.
seq_fasta_string=''.join(map(str,seq_fasta_join))# converting list of seq into string
n=3 # Number of occurance
Three_letter_occur = [seq_fasta_string[i:i + n] for i in range(0, len(seq_fasta_string), n)]# iterate to get codons.
#print(Three_letter_occur)
Number_of_codons = len(Three_letter_occur)# Number of codons in seq
print("Number of codons in seq: ", Number_of_codons)
count = {}
for i in Three_letter_occur:
   if not i in count:
         count[i] = 1
   else:
         count[i] +=1
print(count)
# Saving the output in text file.
with open("codons_number.txt", 'w') as f:
    for key, value in count.items():
        f.write('%s:%s\n' % (key, value))