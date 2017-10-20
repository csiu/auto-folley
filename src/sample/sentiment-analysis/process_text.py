import nltk
import re

def text_process(text):
    # Resolve new lines
    processed_text = text.split('\n')
    processed_text = ' '.join(processed_text)
    # To lowercase
    processed_text = processed_text.lower()
    # Tokenize/remove punctuation & digits
    processed_text = nltk.wordpunct_tokenize(re.sub('[^a-zA-Z_ ]', '', processed_text))

    # Make back to string
    processed_text = ' '.join(processed_text)
    return(processed_text)


# Example
text = "Ride around nights mostly.\nSubways, buses."
text_process(text)
# 'ride around nights mostly subways buses'
