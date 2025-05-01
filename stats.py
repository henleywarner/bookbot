import string

def get_book_text(book):
    book_contents = book.read()
    return book_contents  # Return the book contents as a string

def count_words(book_contents):
    words = book_contents.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")

def count_characters(book_contents):
    all_lower = book_contents.lower()  # Convert the contents to lowercase
    char_dict = {} # Initialize an empty dictionary
    for char in all_lower:
        if char in char_dict: #if we've seen it before...
            char_dict[char] += 1
        else: #we haven't seen it before...
            char_dict[char] = 1
    return char_dict