from tqdm import tqdm

numberOfWords = 0
# titles = os.listdir('./WikiHow-Dataset/articles/')
with open('./datasets/WikiHowIndices/all_train.txt') as f:
    titles = f.readlines()

for title in tqdm(titles):
    with open('./datasets/WikiHow/' + title.strip() + '.txt') as f:
        summaryDocument = f.read()
    summaries = summaryDocument.split('@article')[0].split('@summary')
    summaries = ' '.join([summary.strip() for summary in summaries]).strip()
    numberOfWords += len(summaries.split())
avg_len = numberOfWords/len(titles)
print(avg_len)


residual = 0

for title in tqdm(titles):
    with open('./datasets/WikiHow/' + title.strip() + '.txt') as f:
        summaryDocument = f.read()
    summaries = summaryDocument.split('@article')[0].split('@summary')
    summaries = ' '.join([summary.strip() for summary in summaries]).strip()
    residual += (len(summaries.split()) - avg_len) ** 2

print((residual/len(titles)) ** 0.5)
