import string
import re

# looked this up, this function will remove double-spacing from within the string
def normalize_spaces(text):
    return re.sub(r'\s+', ' ', text.strip())

# Looked this up, removes punctuation from the text like hyphens, asterisks, etc
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

# cleans the text by lowercasing, normalizing spaces, and removing punctuation
def clean(text):
    rinse_1 = normalize_spaces(text.lower())
    rinse_2 = remove_punctuation(rinse_1)
    return rinse_2

# Scans the message for our key of spam words/phrases
# Then returning the spam score, and a list of the detected spam words/phrases
def spam_tracker(message, keywords):
    cleaned_message = clean(message)

    # Creates a list of individual words to scan through
    words = cleaned_message.split()
    word_set = set(words)

    score = 0
    matched_words = []

    for keyword in keywords:
        cleaned_keyword = clean(keyword)
        # Checks if the keyword contains a space: making it a phrase
        if " " in cleaned_keyword:
            # It's a phrase - check if phrase exists in the cleaned message string
            if cleaned_keyword in cleaned_message:
                score += 1
                # Keep original keyword for display
                matched_words.append(keyword)

        # If there is no space, then it's a keyword
        else:
            # Single word - check in word set
            if cleaned_keyword in word_set:
                score += 1
                # Keep original keyword for display
                matched_words.append(keyword)

    return score, matched_words

# Just assigning different ratings, to arbitrary scores I came up with
def spam_rating(score):
    if score == 0:
        return "Very Low"
    if score <= 3:
        return "Low"
    if score <= 6:
        return "Moderate"
    if score <= 10:
        return "Likely"
    else:
        return "Very Likely"

def main():

    # establishing a list of our "scam words" to reference
    keywords = ["free", "winner", "won", "prize", "cash", "urgent", "money", "credit",
        "deal", "offer", "click here", "subscribe", "buy now", "easy",
        "guarantee", "limited time", "act now", "discount", "cheap", "earn",
        "income", "save big", "investment", "work from home", "congratulations",
        "trial", "no cost", "promise", "password", "risk free"]

    print("Please enter your email below to check likelihood of spam.")
    print("Enter an empty line to finish.\n")

    message_lines = []
    empty_line_count = 0

    # This function allows users to just copy and paste their email in by running it through a loop to make it processable
    while True:
        #Reads a line of the users input
        line = input()

        # this checks weather that line is empty or not if it is 1 is added to a counter
        if line == '':
            empty_line_count += 1
            # once our counter hit's two, the loop is broken
            if empty_line_count ==2:
                break

        else:
            # resetting the counter when a non-empty line is read
            empty_line_count = 0
            # Add the entered line to the list
            message_lines.append(line)
    # joining all the collected lines to form the full email as one unbroken line.
    message = "\n".join(message_lines)

    score, matches = spam_tracker(message, keywords)
    likely_hood = spam_rating(score)

    print(f"\nYour email received a spam score of {score}")
    print(f"The odds of this email being spam are: {likely_hood}")

    if score > 0:
        print("These are the words/phrases found that indicate spam:")
        for word in matches:
            print(f" - {word}")
    else:
        print("No spam found. :)")

if __name__ == "__main__":
    main()
