import re

def srh_word(string):
    new_string = re.sub(pattern=r'\b[0-1][0-9]:[0-5][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]:[0-5][0-9]\b', string=string, repl='(TBD)')
    new_string = re.sub(pattern=r'\b[0-1][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]\b', string=new_string, repl='(TBD)')
    return new_string

def main():
    put = input()

    text = srh_word(put)

    print(text)

if __name__ == '__main__':
    main()