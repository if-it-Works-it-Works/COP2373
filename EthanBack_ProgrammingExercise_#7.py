import re

# Function to split input text into sentences
def split_sentences(s):
    # Regex pattern to find sentences starting with uppercase letters or numbers
    pattern = r'[A-Z0-9].*?[.!?](?=\s|$)'
    # Find all matching sentences (case-insensitive, dot matches newline)
    matches = re.findall(pattern, s, flags=re.DOTALL | re.IGNORECASE)
    # Strip whitespace and filter out empty results, then return list
    return [s.strip() for s in matches if s.strip()]

# Function to display sentences and the total count
def display_results(sentences):
    # Loop through each sentence and print with an arrow prefix
    for i in sentences:
        print('->', i)
    # Print total number of sentences found
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    # Prompt user to paste their paragraph
    s = input("Paste Text Here:\n ")
    # Get list of sentences by splitting input
    sentences = split_sentences(s)
    # Display sentences and total count
    display_results(sentences)

# Run main function when script is executed
if __name__ == '__main__':
    main()