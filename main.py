def main():
    file_and_path = "books/frankenstein.txt"
    file_contents = get_file_contents(file_and_path)
    file_word_count = get_file_wordcount(file_contents)
    file_character_count = get_charactercount(file_contents)
    print_report(file_and_path,file_word_count,file_character_count)

def get_file_contents(file_and_path):
    with open(file_and_path) as f:
        file_contents = f.read()
    return file_contents

def get_file_wordcount(text):
    words = text.split()
    return len(words)

def get_charactercount(text):
    text_to_count = text.lower()
    dict_count = {}
    for i in text_to_count:
        if i in dict_count.keys():
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    return dict_count

def convert_dictionary(dict):
    result_list = []
    for key in dict:
        if key.isalpha():      
            result_list.append({ 'letter': key, 'num': dict[key]})
    result_list.sort(reverse=True, key=sort_on)
    return result_list

def sort_on(dict):
    return dict["num"]

def print_report(path,wordcount,charactercount):
    character_count_list = convert_dictionary(charactercount)

    print (f"--- Begin report of {path} ---")
    print (f"{wordcount} words found in the document")
    print ()
    for i in character_count_list:
        print(f"The '{i['letter']}' character was fount {i['num']} times")
    print ("--- End report ---")
      
main()
