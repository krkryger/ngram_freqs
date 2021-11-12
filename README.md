# N-gram frequencies
Simple utility to find the most common word n-grams from a corpus. Good for language learning, etc.

### Instructions

1. Find a monolingual corpus in your target language. I recommend using the [OpenSubtitles corpus](https://opus.nlpl.eu/OpenSubtitles.php). Click on your language in the leftmost column in the _lower table_ to download a .txt file.

2. Create a folder for your language in the repo and put the corpus file in it. Example: `.en/en.txt`

3. Run `ngram_freqs.py` with the following arguments:
    - `_language` - your target language (must be available for NLTK), ex: `english`
    - `_corpus` - path to your data, ex: `en/en.txt`
    - `_output_folder` - path to store the resulting n-grams, ex: `en/results/` (be sure to include the slash at the end)
    
Example code: `python ngram_freqs.py english en/en.txt en/results/`
    
    
### How it works

The script streams all the lines from your corpus path to create a list of tokens with NLTK. Depending on the size of your file, this can take up a lot of memory and take several hours. To help you follow the progress, the script prints out a checkpoint every 100 000 lines.
The tokens are then used to create 3-grams, 4-grams, 5-grams and 6-grams, by default including the 1000 most common ones for each type (you can change this with the argument `top_n` in the function `write_ngrams`).


### Contribution

Feel free to make a pull request if you have any improvements, especially regarding memory usage. Thanks!
