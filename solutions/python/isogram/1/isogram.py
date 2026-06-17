def is_isogram(string):
    letters = string.lower().replace(" ","").replace("-", "")
    return len(letters)==len(set(letters))
        
    