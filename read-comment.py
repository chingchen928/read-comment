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
