import re

with open('testFiles/hw1.txt', 'r') as file:
    rawString = file.read().replace('\n', '')

rawString = rawString.replace(' ', '')
rawString = rawString.lower()
rawString = re.sub(r'[^\w\s]', '', rawString)


def frequency(txt, sign):
    counter: int = 0
    for s in txt:
        if s != sign:
            continue
        counter += 1
    return counter


valDict = {}

for s in 'abcdefghijklmnopqrstuvwxyz':
    howMany = frequency(rawString, s)
    percent = 100 * howMany / len(rawString)
    valDict.update({s: percent})

valDict = {k: v for k, v in sorted(
    valDict.items(), key=lambda item: item[1], reverse=True)}

for key, val in valDict.items():
    val = str(round(val, 2))
    print('\'' + key + '\'' + ' - ' + val + '%')
