data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(count)
print('There are', len(data), 'comments')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('Average:', sum_len / len(data), 'words per comments')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new), 'comments less than 100 words')
print(new[2].strip())

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good), 'comments included the word good')
print(good[24])
