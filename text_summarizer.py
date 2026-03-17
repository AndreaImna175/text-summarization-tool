# TEXT SUMMARIZATION TOOL USING NLP

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


def summarize_text(input_text, sentences_count=3):
    
    # Convert text into a parser object
    parser = PlaintextParser.from_string(input_text, Tokenizer("english"))
    
    # Initialize TextRank summarizer
    summarizer = TextRankSummarizer()
    
    # Generate summary
    summary = summarizer(parser.document, sentences_count)
    
    # Store summary sentences
    final_summary = ""
    
    for sentence in summary:
        final_summary += str(sentence) + " "
        
    return final_summary


# ----------- SAMPLE INPUT ARTICLE -----------

print("Enter your article (press Enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

input_text = "\n".join(lines)


# ----------- RUN THE TOOL -----------

print("\n===== INPUT ARTICLE =====\n")
print(input_text)

print("\n===== GENERATED SUMMARY =====\n")

summary = summarize_text(input_text, 3)

print(summary)