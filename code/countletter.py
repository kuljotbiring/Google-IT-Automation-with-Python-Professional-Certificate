# counts the number of occurences of letters in a file.
def count_letters(text):
    # make an empty dictionary to hold results
    results = {}

    # iterate over text letters
    for letter in text:
        if letter not in results:
            results[letter] = 0

        results[letter] += 1

    return results


print(count_letters("google"))
