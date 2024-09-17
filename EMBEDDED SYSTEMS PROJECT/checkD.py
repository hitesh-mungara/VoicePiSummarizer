from lexrank import LexRank
from lexrank.mappings.stopwords import STOPWORDS
from lexrank.utils.text import split_sentences, tokenize
import os
import sys

# Input file with the text to be summarized
input_file = "speech.txt"

# Read the input file
with open(input_file, "r") as file:
    input_text = file.read()

# Split the input text into sentences
sentences = split_sentences(input_text)

# Tokenize the sentences
tokenized_sentences = [tokenize(sentence) for sentence in sentences]

# Initialize LexRank with the tokenized sentences and stopwords
lexrank = LexRank([tokenized_sentences], stopwords=STOPWORDS['en'])

# Get the summary (choose the number of sentences you want in the summary)
summary = lexrank.get_summary(sentences, summary_size=5)

# Write the summary to an output file
with open("FinalSummary.txt", "w") as output:
    for sentence in summary:
        output.write(sentence + "\n")

# Exit the script
sys.exit(0)
