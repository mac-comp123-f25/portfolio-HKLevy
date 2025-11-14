def count_words(word,long_text):
    new_text=' '+long_text+' '
    new_word=' '+word+' '
    answer=new_text.count(new_word)
    return answer

print(count_words('ban','abandon ban the ban'))