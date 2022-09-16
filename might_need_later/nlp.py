import re
import glob
import os

for file in glob.glob('./data/14/*.txt')[:]:
    try:
        with open(file, 'r', encoding="utf8") as f:
            text = f.read()
            text = re.sub(r'­\n+', '', text)
            with open('./data/' + re.sub('.txt', '_in_progress.txt', os.path.basename(file)), 'w') as fw:
                fw.write(text)
    except UnicodeEncodeError:
        continue
