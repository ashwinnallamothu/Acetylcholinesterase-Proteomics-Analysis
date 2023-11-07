#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Bio import SeqIO

# Load FASTA file
fasta_file = "/Users/ashwinnallamothu/Desktop/ACHE.fasta"

# Read sequences 
sequences = [record.seq for record in SeqIO.parse(fasta_file, "fasta")]

# Calculate average length
avg_length = sum(len(seq) for seq in sequences) / len(sequences)

# Find the longest sequence
longest_sequence = max(sequences, key=len)

# Print results
print(f"Number of sequences: {len(sequences)}")
print(f"Average sequence length: {avg_length:.2f}")
print(f"Length of the lomgest sequence: {len(longest_sequence)}")

