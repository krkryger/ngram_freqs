import sys
import nltk
from tqdm import tqdm

_language = str(sys.argv[1])
_corpus = str(sys.argv[2])
_output_folder = str(sys.argv[3])

def stream_corpus(filepath=_corpus, language=_language):
    ct = 0
    for line in open(filepath, 'r', encoding='utf8'):
        ct += 1
        if ct%100000 == 0:
            print(ct)
        yield [token.lower() for token in nltk.word_tokenize(line, language) if token.isalpha()]


def write_ngrams(tokens, n, top_n):

    ngrams = nltk.ngrams(tokens, n)
    freqs = nltk.FreqDist(ngrams)

    filename = _output_folder + str(n) + '.txt'

    with open(filename, 'a', encoding='utf8') as f:
        for entry in freqs.most_common(n=top_n):
            line = str(entry[1]) + '\t' + ' '.join(entry[0])
            f.write(line)
            f.write('\n')

    print('\n', f'{i}-grams ready')


print('Creating tokens')
tokens = []
for line in stream_corpus():
    tokens.extend(line)

print('Creating ngrams')
for i in tqdm(range(3,7)):
    write_ngrams(tokens, n=i, top_n=1000)

print('Finished!')