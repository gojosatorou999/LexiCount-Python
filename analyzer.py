import argparse
import re
import string
from collections import Counter
from typing import List, Dict

def clean_text(text: str) -> List[str]:
    """
    Cleans the input text by removing punctuation and converting to lowercase.
    """
    # Remove punctuation using regex for better handling of contractions
    # This keeps words like "it's" as "it's" or removes the apostrophe depending on preference.
    # Here we'll strip most punctuation but keep alphanumeric characters.
    text = text.lower()
    # Replace punctuation with spaces
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(translator)
    # Split by whitespace
    words = text.split()
    return words

def get_word_frequency(words: List[str]) -> List[tuple]:
    """
    Counts the frequency of each word and returns a list of tuples sorted by frequency.
    """
    counts = Counter(words)
    return counts.most_common()

def main():
    parser = argparse.ArgumentParser(description="LexiCount: A simple word frequency analyzer tool.")
    parser.add_argument("input", help="Text string or path to a .txt file to analyze.")
    parser.add_argument("-n", "--top", type=int, default=10, help="Number of top words to display (default: 10).")
    parser.add_argument("-f", "--file", action="store_true", help="Treat input as a file path.")
    
    args = parser.parse_args()
    
    text = ""
    if args.file:
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.input}' not found.")
            return
    else:
        text = args.input
    
    if not text.strip():
        print("Error: No text provided for analysis.")
        return

    words = clean_text(text)
    frequencies = get_word_frequency(words)
    
    print(f"\n{'Word':<20} | {'Frequency':<10}")
    print("-" * 35)
    
    for word, count in frequencies[:args.top]:
        print(f"{word:<20} | {count:<10}")
    
    print(f"\nTotal unique words: {len(frequencies)}")
    print(f"Total word count: {len(words)}")

if __name__ == "__main__":
    main()
