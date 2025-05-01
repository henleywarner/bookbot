from stats import count_words, get_book_text, count_characters

def main():
    with open("books/frankenstein.txt", "r") as book:
        book_contents = get_book_text(book) # Read the file contents once
        count_words(book_contents)  # Pass the contents as a string
        returned_dict = count_characters(book_contents)  # Pass the contents as a string
        print(returned_dict)  # Print the dictionary

main()