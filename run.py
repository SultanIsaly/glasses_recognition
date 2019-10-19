import argparse
import os
from pathlib import Path

from PIL import Image

import torch
import torch.nn as nn
from torchvision import datasets, models, transforms

parser = argparse.ArgumentParser(description='Great Description To Be Here')
parser.add_argument('--input', action="store")
args = parser.parse_args()


model_ft = torch.load('models/model_squeeze_1_1')
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model_ft = model_ft.to(device)
model_ft.eval()

data_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


source_dir = Path(args.input)
with torch.no_grad():
    for file in os.listdir(source_dir):
        test_image = Image.open(source_dir / file)    #Image.open(Path(data_dir) / file)
        test_image_tensor = data_transforms(test_image)

        inputs = test_image_tensor.to(device)
        outputs = model_ft(inputs.reshape((1,inputs.shape[0],inputs.shape[1],inputs.shape[2])))
        _, preds = torch.max(outputs, 1)
        if preds == 0:
            print(file)