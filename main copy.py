print("greetings boots")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    num_char_list=[]
    for char in num_char:
        dict={}
        dict["character"]=char
        dict["num"]=num_char[char]
        num_char_list.append(dict)
    num_char_list.sort(reverse=True,key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} word were found in the document")   
    print(f"{num_char_list}") 
    for char in num_char_list:
        if char["character"].isalpha()==True:
            print (f"The {char['character']} letter is in here {char['num']}")
        else:
            pass
    print("--- End report ---")
    
def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_letters(text):
    return len(text)

def get_num_char(text):
    lower_text=text.lower()
    char_num={}
    for char in lower_text:
        if char in char_num:
            char_num[char]+=1
        else:
            char_num[char]=1
    return char_num
            


main()
