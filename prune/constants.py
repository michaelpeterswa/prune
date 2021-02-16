"""
Transliterates latin characters (english alphabet) into unicode 
anglo-saxon runic characters. 

Dictionary taken from: https://github.com/RollsW/Rune-Scribe/blob/master/runic.py
Wikipedia (for the unicode codes) https://en.wikipedia.org/wiki/Runic_(Unicode_block)

trimmed out punctuation marks (not necessary for my use case) 
"""
RUNE = {
    "a": "\u16AA",
    "b": "\u16D2",
    "c": "\u16B3",
    "d": "\u16DE",
    "e": "\u16D6",
    "f": "\u16A0",
    "g": "\u16B7",
    "h": "\u16BB",
    "i": "\u16C1",
    "j": "\u16C4",
    "k": "\u16e3",
    "l": "\u16DA",
    "m": "\u16D7",
    "n": "\u16BE",
    "o": "\u16A9",
    "p": "\u16C8",
    "q": "\u16E2",
    "r": "\u16B1",
    "s": "\u16CB",
    "t": "\u16CF",
    "u": "\u16A2",
    "v": "\u16A1",
    "w": "\u16B9",
    "x": "\u16C9",
    "y": "\u16A3",
    "z": "\u16CE"
}