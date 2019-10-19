import os
from pathlib import Path
import pandas as pd

smpl_dstr = Path('MeGlass/test')
output_path = Path('MeGlass_120x120')
train_gl = pd.read_csv(smpl_dstr / 'gallery_black_glass.txt',header=None)
train_wth_gl = pd.read_csv(smpl_dstr / 'gallery_no_glass.txt',header=None)
val_gl = pd.read_csv(smpl_dstr / 'probe_black_glass.txt',header=None)
val_wth_gl = pd.read_csv(smpl_dstr / 'probe_no_glass.txt',header=None)

os.mkdir('MeGlass_120x120/train')
os.mkdir('MeGlass_120x120/val')

os.mkdir('MeGlass_120x120/train/glass')
os.mkdir('MeGlass_120x120/train/noglass')
os.mkdir('MeGlass_120x120/val/glass')
os.mkdir('MeGlass_120x120/val/noglass')

itrt = [(train_gl, 'train', 'glass'), (train_wth_gl, 'train', 'noglass'), 
        (val_gl, 'val', 'glass'), (val_wth_gl, 'val', 'noglass')]

for pth in itrt:
    for i in range(len(pth[0])):
        file = pth[0].iloc[i][0] 
        os.replace(output_path / file, output_path / pth[1] / pth[2] / file)
    
        
print('Size of glasses validation')
print(len(os.listdir(output_path / 'val' / 'glass')))

print('Size of noglasses validation') 
print(len(os.listdir(output_path / 'val' / 'noglass')))
      
print('Size of glasses train') 
print(len(os.listdir(output_path / 'train' / 'glass')))
          
print('Size of noglasses train')
print(len(os.listdir(output_path / 'train' / 'noglass')))