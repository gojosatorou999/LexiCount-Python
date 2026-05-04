# LexiCount

A lightweight Python tool for analyzing word frequencies in text strings or files. 

## Features
- **File & String Support**: Analyze direct text input or read from `.txt` files.
- **Top-N Results**: Filter to see only the most frequent words.
- **Text Cleaning**: Automatically removes punctuation and normalizes casing for accurate counts.

## How it Works (Methodology)
The tool follows a simple but effective pipeline:
1. **Normalization**: Converts all text to lowercase to ensure "Word" and "word" are counted together.
2. **Sanitization**: Uses Python's `string.punctuation` map to replace all punctuation marks with spaces, preventing attached punctuation (like `hello!`) from being treated as unique words.
3. **Tokenization**: Splits the sanitized string by whitespace into individual tokens (words).
4. **Frequency Mapping**: Utilizes `collections.Counter` to efficiently tally occurrences.
5. **Sorting**: Returns the most common words using the `most_common()` method.
 
## Usage 
### Analyze a string
```bash
python analyzer.py "The quick brown fox jumps over the lazy dog. The fox was fast."
```

### Analyze a file
```bash
python analyzer.py -f sample.txt --top 20
```

### Arguments
| Argument | Short | Description |
|----------|-------|-------------|
| `input`  | N/A   | The text or file path to analyze. |
| `--file` | `-f`  | Flag to indicate the input is a file path. |
| `--top`  | `-n`  | Number of top words to display (default: 10). |

## Requirements
- Python 3.6+
- No external dependencies (uses standard library).
