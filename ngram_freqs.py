import sys
import nltk
from tqdm import tqdm

# the command line arguments are as follows (see readme for further info)
_language = str(sys.argv[1])
_corpus = str(sys.argv[2])
_output_folder = str(sys.argv[3])

def stream_corpus(filepath=_corpus, language=_language):

    """
    Streams lines from a corpus file into a tokenized wordlist.

        Parameters:
            filepath (str): path to the corpus
            language (str): language used for tokenization (see NLTK languages)

        Yields:
            list of lowercased alphabetic tokens in the line.
    """

    ct = 0
    for line in open(filepath, 'r', encoding='utf8'):
        ct += 1
        # print out the line count every 100000 lines to track progress
        if ct%100000 == 0:
            print(ct)
        yield [token.lower() for token in nltk.word_tokenize(line, language) if token.isalpha()]


def write_ngrams(tokens, n, top_n, output_folder=_output_folder):

    """
    Writes the most frequent 3, 4, 5 and 6-grams into the output folder.

        Parameters:
            tokens (list): tokenized words from the corpus
            n (int): window of ngram
            top_n (int): number of most frequent n-grams to include
            output_folder (str): output path from the command line argument
    """

    ngrams = nltk.ngrams(tokens, n)
    freqs = nltk.FreqDist(ngrams)

    filename = output_folder + str(n) + '.txt'

    with open(filename, 'a', encoding='utf8') as f:
        for entry in freqs.most_common(n=top_n):
            line = str(entry[1]) + '\t' + ' '.join(entry[0])
            f.write(line)
            f.write('\n')

    print('\n', f'{i}-grams ready')


print('Creating tokens')
# Initialize a list
tokens = []
# Iterate the generator
for line in stream_corpus():
    # Append each tokenized line to the list
    tokens.extend(line)

print('Creating ngrams')
for i in tqdm(range(3,7)):
    write_ngrams(tokens, n=i, top_n=1000)

print('Finished!')