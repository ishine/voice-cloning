from resemblyzer import VoiceEncoder, preprocess_wav
from pathlib import Path
import torch

fpath = Path("./wav/VIVOSSPK01_R001.wav")
wav = preprocess_wav(fpath)

encoder = VoiceEncoder()
embed = encoder.embed_utterance(wav)
print(type(embed))
print(embed.shape)

t = torch.tensor(embed)
print(t)
print(type(t))
