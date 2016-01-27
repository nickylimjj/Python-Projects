def load_list(Filename):
    print 'Loading words...'
    with open(Filename) as f:
        for line in f.readlines():
            words = line.split()
            raw_input('Completed. Hit Enter to continue...')
        f.close()
    return words

def isWord(word,dic):
    return word in dic

dictionary = load_list('words.txt')
print isWord('chocolate',dictionary)
print isWord('nanoet',dictionary)