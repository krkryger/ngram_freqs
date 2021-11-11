import nltk
from tqdm import tqdm

def stream_corpus(filepath='data/ru.txt'):
    ct = 0
    for line in open(filepath, 'r', encoding='utf8'):
        ct += 1
        if ct%100000 == 0:
            print(ct)
        yield [token for token in nltk.word_tokenize(line, 'russian') if token.isalpha()]

def write_ngrams(tokens, n, top_n):

    ngrams = nltk.ngrams(tokens, i)
    freqs = nltk.FreqDist(ngrams)

    filename = 'data/'+str(i)+'.txt'

    with open(filename, 'a', encoding='utf8') as f:
        for entry in freqs.most_common(n=100):
            line = str(entry[1]) + '\t' + ' '.join(entry[0])
            f.write(line)
            f.write('\n')

    print(f'{i}-grams ready')


print('Creating tokens')
tokens = []
for line in stream_corpus():
    tokens.extend(line)

print('Creating ngrams')
for i in tqdm(range(3,7)):
    write_ngrams(tokens, i, 3)

print('Finished!')











    


