from stats import count_words, get_book_text, count_characters, sort_on, chars_to_sorted_list
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]



    with open(path_to_book, "r") as book:
        book_contents = get_book_text(book) # Read the file contents once
        word_count = count_words(book_contents)  # Pass the contents as a string
        returned_dict = count_characters(book_contents)  # Pass the contents as a string
        # print(returned_dict)  # Print the dictionary
        sorted_chars = chars_to_sorted_list(returned_dict)

                # Now print your report using sorted_chars
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_book}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

    for char_dict in sorted_chars:
        character = char_dict["char"]
        count = char_dict["num"]
        if character.isalpha():
            print(f"{character}: {count}")
    


main()