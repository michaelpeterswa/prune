import os
from .constants import RUNE

def list_runes():
    print(RUNE)

def prune(input):
    output = []
    for line in input:
        outline = ""
        for ch in line:
            if ch in RUNE:
                outline += RUNE[ch]
            else:
                outline += ch
        output.append(outline)
    return output

def deprune(input):
    output = []
    for line in input:
        outline = ""
        for ch in line:
            try:
                val = list(RUNE.values()).index(ch)
                outline += list(RUNE.keys())[val]
            except:
                outline += ch
        output.append(outline)
    return output

def execute(infile):
    '''
    incredibly jank solution
    '''
    os.system("python " + infile)