import string
import re


def process_file(fname, enc):
    # of n file for 'r'eading
    with open(fname, 'r', encoding=enc) as file:
        dat = file.read()  # read file
        dat = perform_re(dat)
    return dat.split()  # return read data, split at spaces


# end def process_file(fname, enc):


def write_results(fname, data, enc):
    # open a file for 'w'riting
    with open(fname, 'w', encoding=enc) as file:
        file.write(data)


# def write_results(fname, data, enc):


def words_to_dict(all_words, dictionary, count):
    total_count = count
    for w in all_words:
        w = clean_word(w)  # send word for cleaning
        if w in dictionary:
            dictionary[w] += 1  # increment count
            total_count += 1
        else:
            dictionary[w] = 1  # begin count for new word
            total_count += 1

    return total_count


#  end of def words_to_dict(all_words, dictionary):


def clean_word(word):
    for p in string.punctuation:
        word = word.replace(p, "")  # delete punctuation
    return word.lower()


def perform_re(text):
    text = re.sub(r"(CHAPTER) ([IVXLC]+.)", "\\1\\2", text)
    return text


def unique_words_finder(book):
    unique_words = {}
    total_words = 0
    book_words = process_file(book, "utf-8")
    total_words = words_to_dict(book_words, unique_words, total_words)
    return unique_words, total_words, book_words


def main():
    print("================================================================")
    print("Pick two books from these options of books to compare:")
    print("[1.] Alice")
    print("[2.] Peter Pan")
    print("[3.] The Time Machine")
    print("[4.] Through the Looking-Glass")
    print("[5.] Ann of the Island")
    print("================================================================")

    def getChoice(num):
        choice = input(f"Type the corresponding number of your desired book {num} =>")
        return choice

    book_one = getChoice(1)
    if 1 > int(book_one) or int(book_one) > 5:
        print("Invalid entry. Try again")
        getChoice(1)

    book_two = getChoice(2)
    if 1 > int(book_two) or int(book_two) > 5:
        print("Invalid entry. Try again")
        getChoice(1)
    print("-----------------------------------------------------------------")
    library_of_books = ["alice.txt", "peter-pan.txt", "time-machine.txt", "ttl-glass.txt", "ann_of_the_island.txt"]

    book_choice1_words, book1_no_of_words, book_words1 = unique_words_finder(library_of_books[(int(book_one) - 1)])
    print("Found {} unique words out of a total of {} words in Book 1: '{}'.".format(len(book_choice1_words.keys()),
                                                                                     book1_no_of_words,
                                                                                     library_of_books[
                                                                                         (int(book_one) - 1)]))
    print(list(book_choice1_words)[:5])  # print first few unique words
    print(".....................................................................")
    book_choice2_words, book2_no_of_words, book_words2 = unique_words_finder(library_of_books[int(book_two) - 1])
    print("Found {} unique words out of a total of {} words in Book 2: '{}'.".format(len(book_choice2_words.keys()),
                                                                                     book2_no_of_words,
                                                                                     library_of_books[
                                                                                         (int(book_two) - 1)]))
    print(list(book_choice2_words.keys())[:5])  # print first few unique words

    # to compare unique words in both books
    common_words = []
    common_words_count = 0
    for word1 in book_choice1_words.keys():
        for word2 in book_choice2_words.keys():
            if word1 == word2:
                common_words.append(word2)
                common_words_count += 1
    print("Book 1 and Book 2 have {} common words in them.".format(common_words_count))
    print(".....................................................................")

    # Calculating the Gap and TTR
    global books_diff
    if book1_no_of_words > book2_no_of_words:
        books_diff = book1_no_of_words - book2_no_of_words
    else:
        books_diff = book2_no_of_words - book1_no_of_words
    if books_diff > 3000:
        print(f"The gap in total number of words between the two books is {books_diff} which makes the TTR not reliable"
              f"for comparison ")
    else:
        print(f"The gap in total number of words between the two books is {books_diff} which makes the TTR acceptable"
              f" for comparison ")
    print(".....................................................................")

    print(f"TTR: for book: {library_of_books[(int(book_one) - 1)]} is",
          len(book_choice1_words.keys()) / len(book_words1))
    print(f"TTR: for book: {library_of_books[(int(book_two) - 1)]} is",
          len(book_choice2_words.keys()) / len(book_words2))
    print(".....................................................................")
    # end of calculating TTR

    # To search both texts for a word
    search_prompt = input("Enter a word you want to search ")
    search_prompt = search_prompt.lower()
    print(".....................................................................")
    result_in_book1 = book_choice1_words.get(search_prompt, 0)
    result_in_book2 = book_choice2_words.get(search_prompt, 0)
    if search_prompt in book_choice1_words:
        print(f"'{search_prompt}' appears {result_in_book1} times in {library_of_books[(int(book_one) - 1)]}")
    else:
        print(f"'{search_prompt}' appears 0 times in {library_of_books[(int(book_one) - 1)]}")
    #   end of if search_prompt in book_choice1_words:

    if search_prompt in book_choice2_words:
        print(f"'{search_prompt}' appears {result_in_book2} times in {library_of_books[(int(book_two) - 1)]}")
    else:
        print(f"'{search_prompt}' appears 0 times in {library_of_books[(int(book_two) - 1)]}")

    print(".....................................................................")
    print("-------------End of Program------------------")
    print("-------------Restart program to choose 2 new books------------------")

#   end of if search_prompt in book_choice1_words:

# end def main():


if __name__ == "__main__":
    main()
