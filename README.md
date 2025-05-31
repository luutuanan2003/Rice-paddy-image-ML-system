# 🌾 Rice Paddy Image Classification System

This project was developed as part of a machine learning assignment for **COSC2753 (RMIT University, 2025A)**. The goal was to design a fully self-contained deep learning pipeline to detect **rice leaf diseases** from images — with the added challenge of building everything **from scratch without any pre-trained models or weights**.

---

## 🎯 Objectives and Constraints

While academic in context, the assignment mimicked real-world production constraints:

- ❌ No use of pre-trained architectures or ImageNet weights
- ✅ Models must be trained **entirely on the provided dataset**
- ⚖️ Handle class imbalance and rare disease detection
- 📷 Perform image cleaning, augmentation, and validation
- 📊 Evaluate not just accuracy, but generalization performance

This forced us to tailor every model decision (architecture, loss function, learning rate schedule, data balancing strategy) specifically to this dataset and task.

---

## 📦 Project Overview

The full pipeline is structured to support multiple tasks:

- **Task 1 – Disease Classification** ✅ (*complete*)
- **Task 2 – Variety Prediction** 🔜
- **Task 3 – Age Estimation** 🔜
- **Final Phase – Unified Deployment (Streamlit or Docker)** 🔜

All code is written in modular notebooks, fully documented and designed for reproducibility and future extension.

---


## 🚀 Current Task: Disease Classification (Task 1)

This model classifies paddy leaf images into **10 classes** — 9 disease types + 1 healthy class (`normal`).

| Architecture     | InceptionV3 (no pretrained weights) |
|------------------|--------------------------------------|
| Input Size       | 299×299                              |
| Optimizer        | RMSprop                              |
| Loss Function    | Categorical Crossentropy + Label Smoothing |
| Balancing        | Image augmentation + SMOTE + class weights |
| Final Accuracy   | ✅ ~93.5% train, ~92% validation      |

---

## 🧠 Dataset

The original dataset includes:
- 10,407 labeled images across 10 classes
- Each image has `label`, `variety`, and `age` metadata

⚠️ The dataset is not stored in this repository.  
You can download it from this link:  
📦 *(insert Google Drive or GitHub Release link here)*

