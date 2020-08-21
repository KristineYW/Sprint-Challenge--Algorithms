'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Store the target string as a variable
    substring = "th"

    # Handle the edge cases, like where the input word contains fewer than 2 letters
    if len(word) < 2:
        return 0
    
    # Begin recursive algorithm
    # If the first two letters of the input word is the substring, return 1 and then recurse through the rest of the word 
    if substring in word[:2]:
        return 1 + count_th(word[2:])
    # If the first two letters of the input word is NOT the substring, return 0 and recurse through the rest of the word
    else: 
        return 0 + count_th(word[1:])