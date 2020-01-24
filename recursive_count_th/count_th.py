'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: # Here's the base case
        return 0
    # Check to see if word starts with 't' and has an 'h' after. If it does, add to count and
    # re-run function after cutting the 't' and 'h' out.
    elif word[0] == 't' and word[1] == 'h':
        word = word[2:]
        return 1 + count_th(word)
    # If word doesn't start with 't' and 'h', cut out the first letter and run the new word
    # through the function.
    else:
        word = word[1:]
        return count_th(word)
