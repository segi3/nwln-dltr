### remove newline from youtube subtitle file

import glob

from regex import F

input_files = glob.glob('.\masukan\*.txt')

for file in input_files:
    with open(file) as f:
        lines = [line.rstrip() for line in f]
  
    target_location = file.replace('masukan', 'hasil')

    f = open(target_location, 'w')

    for line in lines: # tanpa newline
        f.write(line)

    # for line in lines: # hapus line yg hanya newline
    #     if line != '':
    #         f.write(line + '\n')