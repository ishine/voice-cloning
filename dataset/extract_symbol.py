_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
_letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
_extra = " ̪̪̪"

# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa) + list(_extra)

# Special symbol ids
SPACE_ID = symbols.index(" ")


def get_extra(file_path, extra):
    with open(file_path, 'r') as f:
        data = f.readlines()

    extra = []
    for line in data:
        line = line.strip()
        text = line.split('|')[-1]
        for c in text:
            if c not in symbols and c not in extra:
                extra.append(c)

    return extra


extra = []
extra.extend(get_extra("../filelists/my_val_filelist.txt.cleaned", extra))
extra.extend(get_extra("../filelists/my_test_filelist.txt.cleaned", extra))
extra.extend(get_extra("../filelists/my_train_filelist.txt.cleaned", extra))
print(extra)

with open("extra.txt", 'w') as f:
    for c in extra:
        f.write(c)
