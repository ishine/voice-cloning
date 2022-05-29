import random


def write_to_file(data, filename):
    with open(filename, "w") as f:
        for line in data:
            f.write(line)


with open("./full_filelist.txt", 'r') as f:
    data = f.readlines()

random.shuffle(data)

total = len(data)
train_num = int(0.7 * total)
test_num = int(0.2 * total)

train_data = data[:train_num]
test_data = data[train_num:train_num+test_num]
val_data = data[train_num+test_num:]

write_to_file(train_data, "../filelists/my_train_filelist.txt")
write_to_file(test_data, "../filelists/my_test_filelist.txt")
write_to_file(val_data, "../filelists/my_val_filelist.txt")
