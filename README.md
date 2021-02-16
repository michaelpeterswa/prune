# ᛈᚱᚢᚾᛖ
Anglo-Saxon Runic Python transpiler. Why? See Reddit post linked below.

https://www.reddit.com/r/ProgrammerHumor/comments/lk8rse/if_a_programming_language_that_uses_the_rune/

transpilation can go both ways, using prune() to encode, and deprune() to decode

example.py
```
def main():
    print("example!")

if __name__ == '__main__':
    main()
```
example.prune
```
ᛞᛖᚠ ᛗᚪᛁᚾ():
    ᛈᚱᛁᚾᛏ("ᛖᛉᚪᛗᛈᛚᛖ!")

ᛁᚠ __ᚾᚪᛗᛖ__ == '__ᛗᚪᛁᚾ__':
    ᛗᚪᛁᚾ()
```

## License
see ```LICENSE```
