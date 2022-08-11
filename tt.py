def reverse_words(text):
    s=""
    for i in text.split(" "):
        
        s=s+i[::-1]+" "
    return s
print(reverse_words("hello world"))