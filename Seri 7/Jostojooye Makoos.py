sentence=input()
word=input()
sentence=sentence.lower()
sentence =sentence.replace(',',' ')
sentence =sentence.replace('.',' ')
sentence =sentence.replace('!',' ')
sentence = sentence.replace('(', ' ')
sentence = sentence.replace(')', ' ')
sentence = sentence.replace('-', ' ')
sentence = sentence.replace('_', ' ')
sentence = sentence.replace('@', ' ')
sentence = sentence.replace('#', ' ')
sentence = sentence.replace('$', ' ')
sentence = sentence.replace('%', ' ')
sentence = sentence.replace('^', ' ')
sentence = sentence.replace('&', ' ')
sentence = sentence.replace('*', ' ')
sentence = sentence.replace('{', ' ')
sentence = sentence.replace('}', ' ')
sentence = sentence.replace('[', ' ')
sentence = sentence.replace(']', ' ')
sentence = sentence.replace('`', ' ')
sentence = sentence.replace('~', ' ')
sentence = sentence.replace('|', ' ')
sentence = sentence.replace('"', ' ')
sentence = sentence.replace("'", ' ')
sentence = sentence.replace("1", ' ')
sentence = sentence.replace("2", ' ')
sentence = sentence.replace("3", ' ')
sentence = sentence.replace("4", ' ')
sentence = sentence.replace("5", ' ')
sentence = sentence.replace("6", ' ')
sentence = sentence.replace("7", ' ')
sentence = sentence.replace("8", ' ')
sentence = sentence.replace("9", ' ')
sentence = sentence.replace("0", ' ')
sentence = sentence.replace("+", ' ')
sentence = sentence.replace("=", ' ')
sentence = sentence.replace("<", ' ')
sentence = sentence.replace(">", ' ')
sentence = sentence.replace("?", ' ')
sentence=sentence.split()
word=word.lower()
word=word.strip()
tekrari1=sentence.count(word)
tekrari2=sentence.count(word[::-1])
tekrari3=tekrari1+tekrari2
print(tekrari3)

            