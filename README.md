# Wine-Quality-Prediction
Perfect 👍
What you pasted is **excellent content**, but it’s **duplicated and mixed**.
Below is a **CLEAN, WELL-STRUCTURED, SINGLE VERSION** that you can **paste directly into `README.md`**.

I’ve **merged + organized everything** into a **professional flow** (like real industry repos).

---

# 📌 Project Details

## 🍷 Wine Quality Prediction Using Machine Learning

---

## 🔹 Project Description

This project is an **end-to-end Machine Learning application** that predicts the **quality of red wine** based on its **physicochemical properties**.
The goal is to provide an **objective, data-driven approach** to wine quality assessment, reducing dependency on manual tasting and subjective judgment.

The trained machine learning model is deployed using a **Flask web application**, allowing users to input wine attributes and receive a **real-time quality prediction**.

---

## 🔹 Problem Statement

Wine quality evaluation is traditionally subjective and depends heavily on expert tasters. This project aims to:

* Reduce subjectivity in wine quality assessment
* Predict wine quality using measurable chemical properties
* Demonstrate a complete **machine learning lifecycle**, from training to deployment

---

## 🔹 Dataset Used

* **Dataset Name:** Red Wine Quality Dataset
* **Source:** UCI Machine Learning Repository
* **File:** `Raw_Data/winequality-red.csv`
* **Records:** ~1,600 wine samples
* **Target Variable:** `quality` (integer score, typically between 3 and 8)

Each row represents a wine sample with measured chemical attributes and a corresponding quality score.

---

## 🔹 Input Features (Model Parameters)

The model is trained using the following **11 physicochemical features**:

| Feature Name         | Description                        |
| -------------------- | ---------------------------------- |
| Fixed Acidity        | Non-volatile acids in wine         |
| Volatile Acidity     | Acetic acid content                |
| Citric Acid          | Adds freshness and flavor          |
| Residual Sugar       | Remaining sugar after fermentation |
| Chlorides            | Salt content                       |
| Free Sulfur Dioxide  | Prevents microbial growth          |
| Total Sulfur Dioxide | Total SO₂ content                  |
| Density              | Density of wine                    |
| pH                   | Acidity level                      |
| Sulphates            | Wine preservative                  |
| Alcohol              | Alcohol percentage                 |

⚠️ **Feature order is critical** and must remain consistent between training and inference.

---

## 🔁 End-to-End Machine Learning Workflow

This project follows a complete **end-to-end ML pipeline**, from raw data ingestion to real-time prediction.

---

### 🧹 Data Collection & Preprocessing

1. Loaded the dataset using **pandas**
2. Performed data quality checks:

   * Verified missing values
   * Validated data types and ranges
3. Analyzed feature distributions and correlations
4. No categorical encoding was required (all features are numeric)
5. Separated features and target (`quality`) for model training

---

### 📊 Exploratory Data Analysis (EDA)

EDA was conducted to understand:

* Distribution of wine quality scores
* Impact of alcohol content on wine quality
* Influence of acidity and sulphates on quality

Visualizations were created using **Matplotlib** and **Seaborn** to identify patterns affecting the target variable.

---

### 🧠 Model Training Process

1. Split the dataset into **training and testing sets**
2. Trained a **scikit-learn classification model** to predict wine quality
3. Tuned hyperparameters to improve generalization
4. Evaluated performance on unseen test data
5. Validated the model using accuracy and other evaluation metrics

All training and experimentation steps are documented in:

```
Wine_Quality_Prediction_Notebook.ipynb
```

---

### 💾 Model Serialization

* The trained model was serialized using **pickle**
* Saved as `model.pkl`
* This artifact is reused during deployment for inference

Serialization allows predictions without retraining the model.

---

### 🌐 Model Deployment & Inference

1. Flask application loads `model.pkl` at startup
2. Users enter wine parameters through a web form
3. Inputs are:

   * Converted to numeric values
   * Ordered to match training feature order
   * Reshaped into a 2D NumPy array
4. The model performs inference
5. The predicted wine quality score is displayed instantly

---

### 🔄 End-to-End System Flow

```
User Input (Web UI)
        ↓
Flask Backend
        ↓
Input Validation & Formatting
        ↓
Trained ML Model (model.pkl)
        ↓
Quality Prediction
        ↓
Result Displayed to User
```

---

## 🔹 Model Output Interpretation

* The model predicts an **integer wine quality score**
* Typical range: **3 to 8**

Example:

```
Predicted Wine Quality: 5
```

Interpretation:

* **3–4** → Low quality
* **5–6** → Average quality
* **7–8** → Good / High quality

---

## 🛠️ Deployment Workflow Summary

* Model training occurs offline in Jupyter Notebook
* Trained model is saved once as `model.pkl`
* Flask serves predictions using the trained model
* Application supports local and Docker-based deployment

---

## 🔐 Key Design Considerations

* Strict feature order consistency
* Model version compatibility (NumPy & scikit-learn)
* Separation of training and serving workflows
* Lightweight and maintainable architecture

---

## 🎯 Key Learning Outcomes

* Complete ML lifecycle implementation
* Practical ML deployment using Flask
* Handling real-world serialization and dependency issues
* Feature alignment between training and inference
* Building interview-ready ML projects

---


