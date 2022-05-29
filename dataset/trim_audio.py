import librosa
import os
import soundfile
import pandas as pd
from tqdm import tqdm


dirs = os.listdir("./waves")
dirs = [d for d in dirs if os.path.isdir("./waves/" + d)]

filenames = []
for d in dirs:
    cur_dir = os.path.join("./waves", d)
    files = os.listdir(cur_dir)
    files = [f for f in files if ".wav" in f]
    filenames.extend([os.path.join(cur_dir, f) for f in files])

for file_path in tqdm(filenames):
    au, sr = librosa.load(file_path)
    clip, _ = librosa.effects.trim(au, top_db=20)
    file_name = file_path.split("/")[-1]
    soundfile.write("./wav/" + file_name, clip, sr)
