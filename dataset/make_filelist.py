import pandas as pd

df = pd.read_csv("./vlsp_corpus.csv")
df['filename'] = "dataset/vlsp_wav/" + df['filename']

with open("./vlsp_full_filelist.txt" , 'w') as f:
    for i, row in df.iterrows():
        out = row['filename'] + "|" + str(row['spkr_id']) + "|" + row["sentence"] + "\n"
        f.write(out)
