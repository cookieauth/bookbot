def main():
    file_contents = None
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    words = count_words(file_contents)
    chars = count_characters(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{words} words found in the document')

    for key in chars:
        print(f'The character \'{key}\' was found {chars[key]} times.')
    print("--- End Report ---")


def count_words(text):
    total = 0
    for word in text.split():
        total += 1
    return total

def count_characters(text):
    dict = {}
    for char in text.lower():
        dict[char] = dict.get(char, 0) + 1
    return dict

main()