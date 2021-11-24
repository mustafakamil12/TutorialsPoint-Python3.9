def find_delimiter(lst):
    """Find common delimiter for all strings in the list.

    Arguments:
    list -- list of strings to search for delimiters

    Returns:
    List of possible delimiters if there is one. Otherwise empty list.
    """
    delimiters = []
    for letter in lst[0]:
        is_possible_dilimiter = True
        for item in lst[1:]:
            if letter not in item:
                # If the letter doesn't apper in each item -- not a delimiter
                is_possible_dilimiter = False
        if is_possible_dilimiter and letter not in delimiters:
            # If the letter appears in every string and doesn't in the list yet
            delimiters.append(letter)
    return delimiters

lst = ['john#doe', 'foo#bar', 'a#cat']
print(find_delimiter(lst))
