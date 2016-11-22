count = 0
with open('zebra.txt') as src:
	with open('numbered.txt', 'w') as numbered:
		for line in src:
			count += 1
			numbered.write('%d. %s' % (count, line))

print "Successfully copied %d lines" % count
raw_input("Press enter to continue... ")
