# Unified Video-Language Temporal Grounding: Enhancing Open-World Video Understanding with Cross-Attention Transformers

[![arXiv](https://img.shields.io/badge/arXiv-2401.xxxxx-b31b1b.svg)](https://arxiv.org/abs/2401.xxxxx)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.10+-ee4c2c.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Official implementation of **VTG using CAT (Cross-Attention Transformer)** for joint Moment Retrieval (MR) and Highlight Detection (HD) in videos.

> **Paper**: [Unified Video-Language Temporal Grounding: Enhancing Open-World Video Understanding with Cross-Attention Transformers](https://arxiv.org/abs/2401.xxxxx)  
> **Authors**: Vikram Singh, Lov Kumar, Anoop Kumar Patel  
> **Institution**: National Institute of Technology, Kurukshetra

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Reproducing Results](#reproducing-results)
- [Pretrained Models](#pretrained-models)
- [Results](#results)
- [Citation](#citation)
- [License](#license)

---

## 📖 Overview

This repository contains the implementation of **VTG (Video-Language Temporal Grounding)**, a unified cross-attention transformer framework for jointly performing Moment Retrieval (MR) and Highlight Detection (HD) in open-world video understanding.

**Key Contributions:**
- Unified architecture for MR and HD using Cross-Attention Transformers (CAT)
- Pseudo-supervision scheme using CLIP (ViT-B/32) for scalable pre-training
- State-of-the-art performance on QVHighlights, Charades-STA, TACoS, YouTubeHL, and TVSum
- 3-5% absolute improvement in mAP over existing methods

---

## 🚀 Key Features

- **Unified Architecture**: Single model for both MR and HD tasks
- **Cross-Attention Mechanism**: Dynamic attention between video clips and text tokens
- **Multi-Head Self-Attention**: Captures inter-frame and intra-frame relevancy
- **Three Prediction Heads**:
  - Foreground Indicator (binary)
  - Boundary Offsets (temporal intervals)
  - Saliency Scores (continuous)
- **CLIP-based Pseudo-labeling**: Automatic annotation generation
- **Scalable Pre-training**: Leverages 4.2M unlabelled videos

---

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- CUDA 11.3+ (for GPU training)
- 24GB+ GPU memory (for full training)

### Setup

```bash
# Clone the repository
git clone https://github.com/hkhitesh7/VTG-using-CAT-Transformer.git
cd VTG-using-CAT-Transformer

# Create and activate conda environment
conda create -n vtg python=3.8 -y
conda activate vtg

# Install PyTorch (CUDA 11.3)
pip install torch==1.10.0+cu113 torchvision==0.11.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html

# Install other dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
