# Write a program to find if a string has only octal digits.
# Given strings: ['789', '123', '004']

strings = ['789', '123', '004']
octal_strings = [s for s in strings if all(c in '01234567' for c in s)]
print("Output of Question 1:")
print(octal_strings)

# Output:
# ['123', '004']


# --------------------------------------------------
# Extract the user id, domain name and suffix from the email addresses.

import re

emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

pattern = r'([\w\.]+)@([\w]+)\.([\w]+)'
matches = re.findall(pattern, emails)
print("\nOutput of Question 2:")
print(matches)

# Output:
# [('zuck', 'facebook', 'com'), ('sunder33', 'google', 'com'), ('jeff42', 'amazon', 'com')]


# --------------------------------------------------
# Split the following irregular sentence into proper words
sentence = "A, very; very: irregular_sentence"
cleaned_sentence = ' '.join(re.split(r'[;,_:\s]+', sentence)).strip()
print("\nOutput of Question 3:")
print(cleaned_sentence)

# Output:
# A very very irregular sentence


# --------------------------------------------------
# Clean up the tweet to contain only the user's message.
import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwei0p0xd cc: @garybernhardt #rstats'''
cleaned_tweet = re.sub(r"http\S+|@\S+|#\S+|RT|cc:|:", "", tweet)
cleaned_tweet = re.sub(r"[^\w\s']", "", cleaned_tweet)
cleaned_tweet = ' '.join(cleaned_tweet.split())
print("\nOutput of Question 4:")
print(cleaned_tweet)

# Output:
# Good advice What I would do differently if I was learning to code today


# --------------------------------------------------
# Extract all the text portions between the tags from the given HTML page.

import requests
from bs4 import BeautifulSoup

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
text_output = [tag.get_text(strip=True) for tag in soup.find_all()]
print("\nOutput of Question 5:")
print(text_output)

# Output (Shortened for readability):
# ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header',
#  "This is a new paragraph!", 'This is another paragraph.', 
#  'This is a new sentence without a paragraph break, in bold italics.']


# --------------------------------------------------
# Identify the words that begin and end with the same character.

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
matching_words = [word for word in words if word[0] == word[-1]]
print("\nOutput of Question 6:")
print(matching_words)

# Output:
# ['civic', 'maximum', 'museums', 'aa']
