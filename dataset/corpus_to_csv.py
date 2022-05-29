import pandas as pd

CORPUS_PATH = "./prompts.txt"

data = []
with open(CORPUS_PATH, "r") as f:
    d = f.readlines()

for line in d:
    l = line.split(' ')
    name = l[0]

    # extract id from name
    name_split = name.split('_')
    my_id = int(name_split[0][-2:])

    text = line.replace(l[0] + ' ',  '').strip().lower()
    data.append([name + '.wav', my_id, text])

df = pd.DataFrame(data, columns=['filename', 'spkr_id', 'sentence'])
df.to_csv("corpus.csv", index=False)
