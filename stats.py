def num_of_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def num_of_characters(text):
    characters = text.lower()
    character_count = {}
    
    for character in characters:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1

    return character_count

def sort_on(dict):
    return dict["count"]

def sort_characters_by_count(char_counts):
    char_list = []

    for char, count in char_counts.items():
        char_dict = {"char": char, "count": count}
        char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list