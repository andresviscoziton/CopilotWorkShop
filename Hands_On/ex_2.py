def count_words(text):
    words = text.split()
    return len(words)

def word_frequencies(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest, len(longest)

def shortest_word(text):
    words = text.split()
    shortest = min(words, key=len)
    return shortest, len(shortest)

def main():
    text = input("Enter text: ")
    print(f"Total number of words: {count_words(text)}")
    
    frequencies = word_frequencies(text)
    print("Word frequencies (most frequent to least frequent):")
    for word, freq in frequencies.items():
        print(f"{word}: {freq}")
    
    longest, longest_len = longest_word(text)
    print(f"Longest word: {longest} (Length: {longest_len})")
    
    shortest, shortest_len = shortest_word(text)
    print(f"Shortest word: {shortest} (Length: {shortest_len})")

if __name__ == "__main__":
    main()