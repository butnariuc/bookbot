import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

from stats import num_of_words, num_of_characters, sort_characters_by_count

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def main():
    text = get_book_text(path)
    word_count = num_of_words(text)
    char_counts = num_of_characters(text)
    sorted_chars = sort_characters_by_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
