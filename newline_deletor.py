### remove newline from youtube subtitle file

import glob

input_files = glob.glob('.\masukan\*.txt')

print('working on files:')

for file in input_files:

    print(file + '..........', end='')
    with open(file) as f:
        lines = [line.rstrip() for line in f]
  
    target_location = file.replace('masukan', 'hasil')

    f = open(target_location, 'w')

    for line in lines: # tanpa newline
        f.write(line)

    print('done')
    # for line in lines: # hapus line yg hanya newline
    #     if line != '':
    #         f.write(line + '\n')
print('finished')