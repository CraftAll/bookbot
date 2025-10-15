
def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def character_counter(text):
    characters = {}
    for char in text.lower():
        if not char in characters:
            characters[char]=0
        characters[char]+=1
    return characters

def sort_char_counter(counter):
    sort_char_counter = []
    for char in counter:
        sort_char_counter.append({"char":char,"num":counter[char]})
    sort_char_counter.sort(key=lambda entry: entry["num"], reverse=True)
    return sort_char_counter
