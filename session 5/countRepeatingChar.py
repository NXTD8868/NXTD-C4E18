word=input('enter words: ')
word=list(word)
def count_letter(letter_to_count):
    dic={

    }
    for i in range(len(word)):
        if letter_to_count[i]!=' ':
            if word[i] in dic:
                dic[word[i]]+=1
            else:
                dic[word[i]]=1
    return dic
a = count_letter(word)
for key in a:
    print(f'{key}: {a[key]}')

