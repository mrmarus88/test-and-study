#Напишите программу Python для поиска слова в строке, а также для поиска его места в исходной строке.
#The quick brown fox jumps over the lazy dog.

import re

word = input()
text = input()
if re.search(word,text):
    result = re.search(word,text)
    start = result.start()
    end = result.end()
    print('Found "{}" in "{}" from {} to {}'.format(''.join (word), text, start, end))
else: 
    print("did't found")

#print(re.search(word,text))
#print("did't found")