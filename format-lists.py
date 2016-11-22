#coding=utf-8

count = 0
readme_content = """# The Zebra Project

In 7th grade, my engineering teacher assigned us a quick mental exercise as busywork: list one hundred things you could do with a zebra. By the next day, I had printed out my list of 500. Since then, my friends and I have slowly been accumulating more words. This repository contains the list in its entirety, alphabetized for your convenience, of things one could do with a zebra.

We currently have **%d things to do with a zebra**! The full list can be found in several formats, including [plain text], [numbered plain text], [markdown], and [HTML]. If you'd like to contribute, just submit a pull request to add a line at the end of `zebra.txt` and `format-lists.py` will handle the rest.

[plain text]: zebra.txt
[numbered plain text]: formats/numbered.txt
[markdown]: formats/zebra.md
[HTML]: formats/zebra.html

## The List

%s"""

# FFS Python, there has got to be a better way to do this...
print "Alphabetizing list..."
new_list = ''
with open('zebra.txt') as src:
	new_list = '\n'.join(sorted(line.strip() for line in src.readlines() if line.strip()))
with open('zebra.txt', 'w') as src:
	src.write(new_list)
print "Formatting list..."
with open('zebra.txt') as src:
	with open('formats/numbered.txt', 'w') as numbered:
		with open('formats/zebra.md', 'w') as markdown:
			with open('formats/zebra.html', 'w') as html:
				html.write('<ol>\n')
				for line in src:
					line = line.strip()
					count += 1
					markdown_line = line
					html_line = line
					if line == 'Embolden the zebra':
						print "Emboldening the zebra..."
						markdown_line = 'Enbolden **the zebra**'
						html_line = 'Enbolden <b>the zebra</b>'
					elif line == 'Italicize the zebra':
						print "Italicizing the zebra..."
						markdown_line = 'Italicize *the zebra*'
						html_line = 'Italicize <i>the zebra</i>'
					elif line == 'Underline the zebra':
						print "Underlining the zebra..."
						html_line = 'Underline <u>the zebra</u>'
					elif line == 'Strike the zebra':
						print "Striking the zebra..."
						markdown_line = 'Strike ~~the zebra~~'
						html_line = 'Strike <strike>the zebra</strike>'
					numbered.write('%d. %s\n' % (count, line))
					markdown.write('%d. %s\n' % (count, markdown_line))
					html.write('\t<li>%s</li>\n' % html_line)
				html.write('</ol>\n')
print
print "Successfully formatted %d lines!" % count
print
print "Updating README..."
with open('README.md', 'w') as readme:
	with open('formats/zebra.md') as markdown:
		readme.write(readme_content % (count, ''.join(markdown.readlines())))
print "Done!"
raw_input("Press enter to continue... ")
