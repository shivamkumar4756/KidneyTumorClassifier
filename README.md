# Kidney Disease Classification Deep Learning Project

## Workflows
1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml
9. app.py

## How to Run?

### Steps

#### Step 1: Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/shivamkumar4756/KidneyTumorClassifier
cd KidneyTumorClassifier
```

#### Step 2: Create and Activate a Conda Environment
Create a new conda environment with Python 3.8 and activate it:

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

#### Step 3: Install Requirements
Install all necessary dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### Step 4: Run the Application
Launch the Flask application:

```bash
python app.py
```

# MLflow & DVC Setup Guide

## Running MLflow UI
To start the MLflow UI, run the following command:
```sh
mlflow ui
```

## Setting Up MLflow Tracking with DagsHub
Export the following environment variables to enable MLflow tracking with DagsHub:
```sh
export MLFLOW_TRACKING_URI=https://dagshub.com/shivamkumar4756/KidneyTumorClassifier.mlflow
export MLFLOW_TRACKING_USERNAME=shivamkumar4756
export MLFLOW_TRACKING_PASSWORD=42207de24f8045d4b172cef364ff92cdea712e58
```

Alternatively, you can set them directly in your Python script:
```python
import os

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/shivamkumar4756/KidneyTumorClassifier.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "shivamkumar4756"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "42207de24f8045d4b172cef364ff92cdea712e58"
```

Run your script with MLflow tracking enabled:
```sh
python script.py
```

---

## DVC Commands
To initialize and use DVC for tracking experiments and orchestrating pipelines, use the following commands:

1. **Initialize DVC**:
```sh
dvc init
```

2. **Reproduce pipeline**:
```sh
dvc repro
```

3. **Visualize pipeline**:
```sh
dvc dag
```

---

## About MLflow & DVC
### **MLflow**
- **Production Grade** experiment tracking.
- Tracks all experiments with detailed logging.
- Supports model logging and tagging for better reproducibility.

### **DVC (Data Version Control)**
- **Lightweight** experiment tracker for POC (Proof of Concept) projects.
- Helps in managing datasets and model versions efficiently.
- Can perform **orchestration**, helping in creating reproducible pipelines.

Both tools can be used together for better experiment tracking and reproducibility in ML projects.





