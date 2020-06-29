import cmudict
import pandas as pd
import random
bad = pd.read_csv('https://query.data.world/s/wxidoxlb6gsqxqvsxvkcyxf4nolwpo')
words = cmudict.entries()
num = len(words)
random.seed()

def makeline(syllables, final):
    remaining = syllables
    line = ""
    while (remaining > 0):
        found = False
        nums = 0
        word = words[random.randint(15, num)]
        while (found == False):
            naughty = False
            nums = 0
            for y in word[1]:
                for z in y:
                    if z.isdigit():
                        nums += 1
            if nums > remaining:
                nums = 0
                word = words[random.randint(15, num)]
                continue
            for x in bad:
                if x in word[0]:
                    naughty = True
                    break
            if naughty == True:
                 word = words[random.randint(15, num)]
                 continue
            found = True
        line = line + word[0] + " "
        remaining -= nums
    if final == False:
        line += "/"
    print(line)

def makehaiku():
    makeline(5, False)
    makeline(7, False)
    makeline(5, True)

makehaiku()


