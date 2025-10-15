from stats import get_num_words, character_counter, sort_char_counter
import sys

def get_book_text(book_filepath):
    with open(book_filepath) as book_file:
        book_content = book_file.read()
    return book_content

def print_report(filepath,num_words,characters):
    print("============ BOOKBOT ============")
    print(f"Analizying book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in characters:
        char = entry["char"]
        num = entry["num"]
        if not char.isalpha():
            continue
        print(f"{char}: {num}")
    print("============= END ==============")


def main():
    if not 2 == len(sys.argv):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit( 1 )
    book_filepath = sys.argv[1]
    content = get_book_text( book_filepath )
    characters = sort_char_counter(character_counter(content))
    num_words = get_num_words(content)
    print_report(book_filepath,num_words,characters)
    

main()
