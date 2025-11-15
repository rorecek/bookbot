def get_num_words(text):
    return len(text.split())

def letter_counts(text):
    letters = {}
    for letter in text.lower():
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    
    sorted_list = []
    for letter, count in letters.items():
        if letter.isalpha():
            sorted_list.append({"letter": letter, "count": count})
    sorted_list.sort(reverse=True, key=lambda item: item["count"])

    return sorted_list