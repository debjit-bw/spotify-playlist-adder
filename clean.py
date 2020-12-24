import re

def legit(word):
    s = 0
    s += sum([word.lower() == filler for filler in ['video', 'official', 'latest', 'trailer']])
    s += word[0] == '('
    s += word[-1] == ')'
    s += word[-1] == '.'
    s += word[-1] == '!'
    return s

def clean(strng):
    strng = strng.lower().replace('full song', ' ').replace('video song', ' ')
    strng = "".join([chr for chr in list(strng) if chr not in ['…', '|', '-', ',', '+', '?', '/', '\'']])
    strng = strng[strng.find(')')+1:-4]
    return " ".join([word for word in strng.split() if legit(word) == 0])

with open("cleaned.txt", mode = 'w', encoding="utf8") as out:
    for line in open("raw.txt", encoding="utf8"):
        line = line.rstrip('\n')
        out.write(clean(line))
        out.write('\n')