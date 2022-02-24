from audioop import reverse


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as text:
        text_string = text.read()
        # print(text_string[0:200])
        # print(f"{len(text_string)} lines in the file.")
        # delete punctuation
        text_string = text_string.replace(".", "")
        text_string = text_string.replace(",", "")
        text_string = text_string.replace("'", "")
        text_string = text_string.replace("?", "")
        text_string = text_string.replace("!", "")
        text_string = text_string.replace(":", "")
        text_string = text_string.replace("[", "")
        text_string = text_string.replace("]", "")
        text_string = text_string.replace("\"", "")
        text_string = text_string.replace("’", "")
        text_string = text_string.replace("-", "")
        text_string = text_string.replace("—", "")
        # lowercase
        text_string = text_string.lower().split()
        # need to make a new dictionary for the no stop words to go into
        no_stop_words = {}
        # need to write the loop for the file
        for word in text_string:
            # need to check if the words in the file are in STOP_WORDS
            if word not in STOP_WORDS:
                if word in no_stop_words:
                    # need to keep count how often a word is used
                    # if the word is in the dictoinary already add 1 to its value
                    no_stop_words[word] += 1
                # if the word is not in the dictionary no stop words add this to the dictionary and give it a value of 1
                else:
                    no_stop_words[word] = 1
                    # need to sort

    # after I get the count I need to sort it
        sorted_values = dict(sorted(no_stop_words.items(),
                                    key=lambda seq: seq[1], reverse=True))
        # need to format
        # print(sorted_values)
        for key in sorted_values:
            print(
                f"{key:>20} | {sorted_values[key]:2} {'*' * sorted_values[key]}")
    # best practice to close the file
        text.close()


# python word_frequency.py praise_song_for_the_day.txt
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
