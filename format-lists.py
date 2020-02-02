#!/usr/bin/env python3

readme_content = """# The Zebra Project

*We do not endorse the harming of zebras in any way. This "project" is entirely for the humorous purpose of smashing random verbs with the word "zebra."*

In 7th grade, my engineering teacher assigned us a quick mental exercise as busywork: list one hundred things you could do with a zebra, with 1% extra credit for each additional one. By the next day, I had printed out my list of 500. Since then, my friends and I have slowly been accumulating more words. This repository contains the list in its entirety, alphabetized for your convenience, of things one could do with a zebra.

Those with some grammatical knowledge may realize that this is really a list of transitive verbs; transitivity is the property of whether or not a verb can take a direct object (here, a zebra).

We currently have **{count} things to do with a zebra**! The full list can be found in several formats, including [plain text], [numbered plain text], [markdown], and [HTML]. If you'd like to contribute, just submit a pull request to add a line at the end of `zebra.txt` and `sort.py` and `format-lists.py` will handle the rest.

[plain text]: zebra.txt
[numbered plain text]: formats/numbered.txt
[markdown]: formats/zebra.md
[HTML]: formats/zebra.html

## The List

"""

markdown_format = {
    'line-format': '{n}. {s}\n',
    'exceptions': {
        'Embolden the zebra': 'Enbolden **the zebra**',
        'Italicize the zebra': 'Italicize *the zebra*',
        'Strike the zebra': 'Strike ~~the zebra~~',
        'Subscript the zebra': 'Subscript <sub>the zebra</sub>',
        'Superscript the zebra': 'Superscript <sup>the zebra</sup>',
    }
}

formats = [
    {
        'file': 'README.md',
        'pre': readme_content,
        **markdown_format
    },
    {
        'file': 'formats/numbered.txt',
        'line-format': '{n}. {s}\n',
        'exceptions': {}
    },
    {
        'file': 'formats/zebra.md',
        **markdown_format
    },
    {
        'file': 'formats/zebra.html',
        'pre': '<ol>\n',
        'post': '</ol>\n',
        'line-format': '\t<li>{s}</li>\n',
        'exceptions': {
            'Embolden the zebra': 'Enbolden <b>the zebra</b>',
            'Italicize the zebra': 'Italicize <i>the zebra</i>',
            'Strike the zebra': 'Strike <strike>the zebra</strike>',
            'Subscript the zebra': 'Subscript <sub>the zebra</sub>',
            'Superscript the zebra': 'Superscript <sup>the zebra</sup>',
            'Underline the zebra': 'Underline <u>the zebra</u>',
        }
    }
]


print("Formatting list...")

lines = []
with open('zebra.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            lines.append(line)

for fmt in formats:
    with open(fmt['file'], 'w') as f:
        if 'pre' in fmt:
            f.write(fmt['pre'].format(count=len(lines)))
        n = 0
        for line in lines:
            n += 1
            line = line.strip()
            if line:
                try:
                    s = fmt['exceptions'][line]
                except KeyError:
                    s = line
                formatted_line = fmt['line-format'].format(n=n, s=s)
                f.write(formatted_line)
        if 'post' in fmt:
            f.write(fmt['post'].format(count=len(lines)))
        print(f"{n} lines written to {fmt['file']}")

print("Done!")
