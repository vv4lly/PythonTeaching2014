__author__ = 'mark'

import string

strange_text = """OK, so I have a piece of 'plain' text that I want save. If I only have unaccented latin characters that conform to the old 'ASCII' standard character set, then I'm probably OK. But what if I'm not an English-speaker? What if I want to store some accented characters like à or á or even characters like ß or å.

When we get further away from European character sets and consider sets like Greek, Cyrillic, Hewbrew or Arabic it gets more complicated. When we get to South and East Asia - Hindi, Korean, Chinese etc. - it gets even more complicated still.

Examples:

Σ Φ Ψ Ω

Л П Ф Ц Ч Ш Ы Ю Я

ਅ ਆ ਇ ਈ ਉ ਊ

玲 瑩 羚 聆 鈴 零 靈 領 例 禮 醴 隸

♠ ♡ ♢ ♣ ♤ ♥ ♦ ♧ ♨ ♩ ♪ ♫ ♬
"""

fh = open("strange_text.txt", "w")

fh.write(strange_text)
fh.close()
my_list = []

fh = open("strange_text.txt", "r")
for line in fh:
    line = line.split()
    for char in line:
        char = char.strip()
        char = char.strip(string.punctuation)
        my_list.append(char.strip())

print(my_list)