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
- **Task 3 – Age Estimation** ✅ (*complete*)
- **Final Phase – Unified Deployment (Streamlit or Docker)** 🔜

All code is written in modular notebooks, fully documented and designed for reproducibility and future extension.

---


## 🧠 Dataset

The original dataset includes:
- 10,407 labeled images across 10 classes
- Each image has `label`, `variety`, and `age` metadata

⚠️ The dataset is not stored in this repository.  
You can download it from Kaggle. However, it has been modified so that the data is imbalance and not pure to facilitate the process of data engineering.

