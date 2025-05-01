# Jamboree Graduate Admission Prediction Case Study

## Project Overview
The **Jamboree Graduate Admission Prediction** case study aims to build a predictive model that estimates a student's chances of getting admitted to top graduate schools, particularly Ivy League institutions. The model takes into account various factors, including GRE scores, TOEFL scores, University Rating, Statement of Purpose (SOP) and Letters of Recommendation (LOR) strength, Undergraduate GPA, and Research Experience. This project aims to assist students applying for graduate programs by helping them understand their chances and improving their preparation.

### Objective
To develop a machine learning model that predicts the probability of admission for graduate students based on the factors mentioned above. The goal is to help Jamboree’s students in improving their chances of gaining admission to prestigious universities by providing data-driven insights.

---

## Problem Definition

Jamboree has introduced a feature that predicts the probability of students getting into an Ivy League graduate program based on their attributes. The problem here is to create a model that analyzes several variables to predict the "Chance of Admit" for a student.

**Problem Breakdown:**
- **Input Features**:
  - **GRE Scores**: GRE score (out of 340)
  - **TOEFL Scores**: TOEFL score (out of 120)
  - **University Rating**: University rating (out of 5)
  - **SOP and LOR Strength**: Statement of Purpose and Letters of Recommendation strength (out of 5)
  - **Undergraduate GPA**: Undergraduate GPA (out of 10)
  - **Research Experience**: Binary variable (0 or 1) indicating whether the student has research experience.

- **Output**:
  - **Chance of Admit**: The target variable (ranging from 0 to 1) representing the probability of admission to a graduate program.

### Goal
To develop a predictive model that can estimate the chances of getting admitted to a top graduate school. The model will provide an admission probability based on key attributes and help Jamboree guide students effectively.

---

## Dataset Description

The dataset contains the following columns:

1. **Serial No.**: A unique identifier for each record.
2. **GRE Scores**: GRE test score (out of 340).
3. **TOEFL Scores**: TOEFL test score (out of 120).
4. **University Rating**: Rating of the university (out of 5).
5. **SOP and LOR Strength**: Strength of the Statement of Purpose (SOP) and Letters of Recommendation (LOR) (out of 5).
6. **Undergraduate GPA**: Grade Point Average (out of 10).
7. **Research Experience**: Binary indicator (0 or 1) for whether the student has research experience.
8. **Chance of Admit**: The target variable, representing the probability of admission (ranging from 0 to 1).

---

## Installation

To set up and run this project, follow the steps below:

### Clone the Repository
```bash
git clone https://github.com/Jinkz04/jamboree-linear-regression
cd jamboree-linear-regression
