def word_count(text):
    count = 0
    words = text.split()
    
    for word in words:
        count += 1
    return count

def char_count(text):
    alpha_track = {}
    lower_text = text.lower()

    for char in lower_text:
        if char.isalpha(): 
            if char in alpha_track:
                alpha_track[char] += 1
            else:
                alpha_track[char] = 1
    return alpha_track

def report(text, words, chars):
    sorted = {}
    num = float("inf")

    while chars:
        key = ''
        largest = 0
        for char in chars:
            value = chars[char]
            if value < num and value > largest:
                key = char
                largest = value
        chars.pop(key)
        sorted[key] = largest
        
    print(f"--- Begin report of {text} ---")
    print(f"{words} words found in the document\n")
    for char in sorted:
        print(f"The {char} character was found {sorted[char]} times")
    print("--- End report ---")


def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
    words = word_count(file_contents) 
    chars = char_count(file_contents)
    report(file_path, words, chars)

main()
