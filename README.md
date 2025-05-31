# 🌾 Rice Paddy Image Classification System

This is a deep learning-based end-to-end system for classifying rice paddy plant diseases using images. The project is part of a broader multi-task pipeline, with Task 1 completed and Tasks 2 & 3 coming soon.

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

