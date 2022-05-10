import re
import emoji
import nltk

nltk.download('words')
words = set(nltk.corpus.words.words())

## usage: train_corpus['text'] = train_corpus['text'].apply(preprocess)
def preprocess(tweet):
    tweet = tweet.replace(r"&amp;?", r"and")
    tweet = tweet.replace('&lt;', r'<')
    tweet = tweet.replace('&gt;', r'>')
    tweet = re.sub("@[A-Za-z0-9]+ ", "", tweet)  # Remove @ sign
    tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", " ", tweet)  # Remove http links
    tweet = re.sub(r"[^\w\s]", " ", tweet)  # remove punctuations
    tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI)  # Remove Emojis
    tweet = re.sub(r" +", " ", tweet)  # remove excess white spaces
    tweet = tweet.strip()  # remove white spaces at the beginning & end of the string
    tweet = tweet.lower()

    return tweet