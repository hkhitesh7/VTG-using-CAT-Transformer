import pdb
import torch as th
import math
import numpy as np
import torch
from run_on_video.video_loader import VideoLoader
from torch.utils.data import DataLoader
import argparse
from run_on_video.preprocessing import Preprocessing
import torch.nn.functional as F
from tqdm import tqdm
import os
import sys
from run_on_video import clip
import argparse

dataset = VideoLoader(
        './examples/charades.mp4',
        framerate=1,
        size=224,
        centercrop=True,
        overwrite=True,
        model_version='ViT-B/32'
    )

loader = DataLoader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=1,
        sampler=None,
    )

for k, data in enumerate(loader):
    print(data)