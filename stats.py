def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    data = {}
    for letters in text:
        if letters.lower() not in data:
            data[letters.lower()] = 1
        else:
            data[letters.lower()] += 1
    return data

def sorty(data):
    return data["num"]

def sorted_dict(data):
    list = []
    for item in data:
        if item.isalpha():
            list.append({"char" : item, "num" : data[item]})
    list.sort(reverse=True, key = sorty)
    return list