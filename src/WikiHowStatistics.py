from tqdm import tqdm
import fire

def check_statistics(split:str = 'test'):
    numberOfWords = 0
    with open(f'./datasets/WikiHowIndices/all_{split}.txt') as f:
        titles = f.readlines()

    for title in tqdm(titles):
        with open('./datasets/WikiHow/' + title.strip() + '.txt') as f:
            summaryDocument = f.read()
        summaries = summaryDocument.split('@article')[0].split('@summary')
        summaries = ' '.join([summary.strip() for summary in summaries]).strip()
        numberOfWords += len(summaries.split())
    avg_len = numberOfWords/len(titles)
    print(f"Average Target Length: {avg_len:.4f}")


    residual = 0

    for title in tqdm(titles):
        with open('./datasets/WikiHow/' + title.strip() + '.txt') as f:
            summaryDocument = f.read()
        summaries = summaryDocument.split('@article')[0].split('@summary')
        summaries = ' '.join([summary.strip() for summary in summaries]).strip()
        residual += (len(summaries.split()) - avg_len) ** 2

    var = (residual/len(titles)) ** 0.5
    print(f"Variance: {var:.4f}")

if __name__ == '__main__':
    fire.Fire(check_statistics)