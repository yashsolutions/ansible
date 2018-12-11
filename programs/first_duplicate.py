content = []
content.append(("Sam hates dogs and dogs hate Sam.", "dogs"))
content.append(("sam hates dogs and dogs hate sam.", "dogs"))
content.append(("Sam hates dogs and sam hates cats.", "hates"))
content.append(("Sam hate dogs and dogs hate Sam.", "dogs"))


import re

def get_first_duplicate_word(sentense):
	count = []
	words = re.split(' |\.|\"|\!|,|;', sentense)
	for word in words:
		word = word.strip()
		if word in count:
			return word
		else:
			count.append(word)


for sentense, answer in content:
	if answer != get_first_duplicate_word(sentense):
		print('WRONG', answer, get_first_duplicate_word(sentense))
	else:
		print('RIGHT')
