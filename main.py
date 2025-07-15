from stats import get_num_words,get_letter_count, sorted_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()

    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # print("============ BOOKBOT ============")
    file = sys.argv[1]
    # print(f"Analyzing book found at {file}...")
    book_text = get_book_text(file)
    # print("----------- Word Count ----------")
    words = get_num_words(book_text)
    print(f"Found {words} total words")

    letters = get_letter_count(book_text)
    #print(f"Letter frequencies: {letters}")
    goob = sorted_dict(letters)
    # print("--------- Character Count -------")
    for item in goob:
        print(f"{item['char']}: {item['num']}")
    # print("============= END ===============")

main()