#coding=utf-8
import re
count = 0
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
					numbered.write('%d. %s\n' % (count, line))
					markdown.write('%d. %s\n' % (count, markdown_line))
					html.write('\t<li>%s</li>\n' % html_line)
				html.write('</ol>\n')
print
print "Successfully formatted %d lines!" % count
print
print "Updating README..."
readme_content = ''
with open('README.md') as readme:
	readme_content = ''.join(readme.read())
with open('README.md', 'w') as readme:
	readme.write(re.sub(r'\*\d+ things to do with a zebra\*', '*%d things to do with a zebra*' % count, readme_content))
print "Done!"
raw_input("Press enter to continue... ")
