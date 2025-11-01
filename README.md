# 🏛️ 3D_PointCloudProject

**3D_PointCloudProject** is a deep-learning-based system designed to generate accurate 3D models from 2D image sequences. The project focuses on **cultural heritage conservation**, providing a digital pipeline to preserve monuments and artifacts using modern computer vision techniques.

By integrating **Structure-from-Motion (SfM)**, **Multi-View Stereo (MVS)**, **point cloud vectorization**, and **mask-based segmentation**, the system creates high-fidelity 3D meshes suitable for virtual documentation, restoration, and visualization.

---

## 🌟 Objectives

* **Develop** a modular 3D reconstruction pipeline from 2D imagery
* **Implement** segmentation-based masking to remove occlusions (e.g., humans, birds)
* **Integrate** advanced reconstruction algorithms (BPA, Poisson)
* **Evaluate** system performance using real and open datasets

---

## 🧩 System Architecture

```
Image Collection
      ↓
Structure-from-Motion (COLMAP)
      ↓
Sparse Point Cloud Generation
      ↓
Segmentation & Masking (DeepLabv3 + Xception)
      ↓
Point Cloud Cleaning
      ↓
Mesh Reconstruction
    ├── Ball-Pivoting Algorithm (BPA)
    └── Poisson Surface Reconstruction
      ↓
Level of Detail (LOD) Generation
      ↓
Visualization (Three.js / Open3D)
```

---

## 🧪 Methodology

### 1. Image Acquisition

Captured from multiple angles (≈70% overlap) using:

| Device    | Focal Length | Resolution |
| :-------- | :----------- | :--------- |
| iPhone 12 | 13mm         | 3024×4032  |
| Sony a7IV | 35mm         | 7008×4672  |

### 2. Sparse Point Cloud Generation

* Used **COLMAP** for feature extraction, camera pose estimation, and bundle adjustment
* Generated accurate 3D point clouds from multiple viewpoints

### 3. Masking & Segmentation

* Applied **DeepLabV3 (Xception backbone)** trained on **ADE20K** dataset
* Segmented out dynamic occluders (humans, birds, etc.)

### 4. Point Cloud Vectorization

Two reconstruction algorithms used:

#### 🌀 Ball-Pivoting Algorithm (BPA)

* Rolls a virtual ball across the surface points to generate a triangular mesh
* Effective for well-sampled, clean data

#### 🧱 Poisson Reconstruction

* Implicit surface fitting method producing smooth, watertight meshes
* Controlled by parameters like tree depth, scale, and linear fitting

### 5. Visualization

Meshes exported as `.ply` files and visualized using:

* **Open3D** for rendering and analysis
* **Three.js** for web-based visualization
* **LOD generation** for scalable rendering performance

---

## 🧰 Technologies Used

| Tool / Library                | Purpose                         |
| ----------------------------- | ------------------------------- |
| **Python (Jupyter Notebook)** | Development environment         |
| **COLMAP**                    | Structure-from-Motion and MVS   |
| **Open3D**                    | Point cloud and mesh processing |
| **DeepLabV3 + Xception**      | Semantic segmentation           |
| **FFmpeg**                    | Frame extraction from videos    |
| **Three.js**                  | Web visualization               |
| **CloudCompare**              | Manual point cloud editing      |

---

## 🦾 Datasets

### 🔹 Open-Source

| Dataset           | Images | Size    | Notes                      |
| ----------------- | ------ | ------- | -------------------------- |
| Tanks and Temples | 251    | 1.56 MB | Standard benchmark dataset |

### 🔹 Custom Captured

| Dataset            | Images | Camera    | Loops | Description                |
| ------------------ | ------ | --------- | ----- | -------------------------- |
| Bowl               | 27     | Sony a7IV | 1     | Single small object        |
| Ganesh             | 36     | iPhone 12 | 1     | Statue reconstruction      |
| Banglamukhi Temple | 307    | iPhone 12 | 4     | Heritage site              |
| Statue             | 88     | iPhone 12 | 2     | Human-sized sculpture      |
| Stone Artifact     | 107    | iPhone 12 | 3     | Museum artifact            |
| Stupa_01           | 193    | iPhone 12 | 6     | Outdoor cultural structure |

---

## 📊 Results & Evaluation

| Dataset  | MSE ↓   | PSNR ↑ | SSIM ↑ | Processing Time |
| -------- | ------- | ------ | ------ | --------------- |
| Truck    | 2891.50 | 13.52  | 0.84   | 98m             |
| Bowl     | 5868.88 | 10.44  | 0.68   | 8m              |
| Ganesh   | 3127.58 | 13.17  | 0.63   | 28m             |
| Statue   | 5854.91 | 10.45  | 0.70   | 28m             |
| Stupa_01 | 3144.48 | 13.15  | 0.75   | 98m             |

**Key Observations:**

* Best results achieved with **high-resolution wide-angle** imagery
* Multi-loop datasets yielded superior reconstructions
* Masking improved output quality but increased processing time
