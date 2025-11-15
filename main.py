import sys
from stats import get_num_words
from stats import letter_counts

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = get_book_text(path)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + path + "...")

    word_count = get_num_words(content)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    for item in letter_counts(content):
        print(f"{item["letter"]}: {item["count"]}")
    # print(get_num_words(content))
    # print(content)
    print("============= END ===============")

main()
