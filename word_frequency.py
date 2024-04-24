import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Function to read the file and remove punctuation
def read_file_and_clean(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        return text

# Function to remove stop words and count word frequencies
def process_text(text):
    stop_words = set(stopwords.words('english'))
    words = text.lower().split()
    filtered_words = [word for word in words if word not in stop_words]
    word_frequencies = Counter(filtered_words)
    return word_frequencies

# Main function
def main():
    file_name = "random_paragraphs.txt"
    text = read_file_and_clean(file_name)
    word_frequencies = process_text(text)

    # Display the word frequency count to the console
    print("Word Frequency Count:")
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()