def more_than_20(file):
    data = open (file, 'r')
    words = []
    words = [x.strip() for x in data if len (x.strip()) > 20]
    return words
    

#more_than_20('CROSSWD.txt')

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True
    
def uses_only(word, letters):
    for x in word:
        if x not in letters:
            return False
    return True
        
def all_uses_only(file,letters):
    file = open (file, 'r')
    file2 = [file]
    for word in file2:
        if uses_only(word, letters) == True:
            return word