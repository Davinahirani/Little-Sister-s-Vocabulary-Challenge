def add_prefix_un():
    """
    Add the 'un' prefix to a word provided by the user.

    :return: str - The root word prepended with 'un'.
    """
    word = input("Enter a word: ")
    prefixed_word = "un" + word
    print(f"Adding 'un' prefix to '{word}' gives '{prefixed_word}'")
    return prefixed_word


def make_word_groups():
    """
    Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :return: str - A string of prefix followed by vocabulary words with prefix applied.

    This function takes a prefix and multiple words as input from the user
    and returns a string with the prefix and the words with prefix applied,
    separated by ' :: '.

    For example: input 'en', 'close', 'joy', 'lighten' returns
    'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = input("Enter a prefix: ")
    words = input("Enter words separated by commas: ").split(',')
    words_with_prefix = [prefix + word.strip() for word in words]
    words_string = ' :: '.join(words_with_prefix)
    result = prefix + ' :: ' + words_string
    print(f"Transformed vocabulary words into string: '{result}'")
    return result


def remove_suffix_ness():
    """
    Remove the suffix 'ness' from a word provided by the user while adjusting the spelling.

    :return: str - The word with suffix removed and spelling adjusted.
    """
    word = input("Enter a word: ")
    if word.endswith('ness'):
        root_word = word[:-4]
        if root_word.endswith('i'):
            root_word = root_word[:-1] + 'y'
        print(f"Removing 'ness' suffix from '{word}' gives '{root_word}'")
        return root_word
    print(f"No 'ness' suffix found in '{word}'. Returning original word.")
    return word


def adjective_to_verb():
    """
    Change the adjective within a sentence provided by the user to a verb.

    :return: str - The word that changes the extracted adjective to a verb.
    """
    sentence = input("Enter a sentence: ")
    index = int(input("Enter the index of the word to transform: "))
    
    words = sentence.split()
    
    if index < 0:
        index = len(words) + index  # Adjust negative index to wrap around to the end of the sentence

    if 0 <= index < len(words):
        adjective = words[index].rstrip('.')
        transformed_word = adjective + 'en' if not adjective.endswith('en') else adjective
        print(f"Changing adjective '{adjective}' to verb gives '{transformed_word}'")
        return transformed_word
    else:
        print("Invalid index or out of range. No transformation applied.")
        return "Invalid index or out of range."


# Test the functions
add_prefix_un()
make_word_groups()
remove_suffix_ness()
adjective_to_verb()
