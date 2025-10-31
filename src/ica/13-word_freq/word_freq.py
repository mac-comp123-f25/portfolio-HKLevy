import string
def compute_frequencies(file_path):
    file_in = open(file_path,'r')
    text = file_in.read()
    word_list = text.split()
    final_words=[]
    for word in word_list:
        newWord = word.strip(string.punctuation)
        bestWord = newWord.lower()
        final_words.append(bestWord)
    freq_dict = {}
    for word in final_words:
        freq_dict[word] = final_words.count(word)
    return freq_dict
print(compute_frequencies('../TextFiles/alice.txt'))

def rank_frequencies(freq_dict):
    list_of_tups=[]
    for word, freq in freq_dict.items():
        list_of_tups.append((freq,word))
    list_of_tups.sort()
    list_of_tups.reverse()
    final_list=[]
    for tup in list_of_tups:
        final_list.append((tup[1],tup[0]))
    return final_list
print(rank_frequencies(compute_frequencies('../TextFiles/alice.txt')))