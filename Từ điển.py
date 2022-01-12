dict =  {
            'dog' : 'chó',
            'cat' : 'mèo',
            'fish' : 'cá',
            'crab' : 'cua',
            'cow' : 'bò',
            'pig' : 'heo',
            'bird' : 'chim',
        }
def translate_dict(dict_db,word):
    for item in dict_db.keys():
        if item ==word:
            print(dict_db.get(item))
            break
        else:
            print('Cant translate')
            break
if __name__ == "__main__":
    word = str(input('Please enter your word: '))
    translate_dict(dict,word)