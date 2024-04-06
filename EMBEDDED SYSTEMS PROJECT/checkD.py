from summarizer import Summarizer
import os
import sys

input_file = "speech.txt"



with open(input_file, "r") as file:
    input_text = file.read()

summarizer = Summarizer()
summary = summarizer.get_summary(text=input_text, title="check")

with open("FinalSummary.txt", "w") as output:
    for sentence_info in summary:
        output.write(str(sentence_info['sentence']) + "\n")

sys.exit(0)
