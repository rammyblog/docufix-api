

def get_txt_word(filename):
    with open('.'+filename, 'r') as reader:
        word = ''
        for line in reader.readlines():
            word+=line
        return word 