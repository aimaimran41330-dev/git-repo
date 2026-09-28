# Customer Satisfaction Prediction — E-Commerce (Olist)

Predicts whether an e-commerce customer will be satisfied (happy/unhappy)
from order details, using the Brazilian E-Commerce Public Dataset by Olist.

## Dataset
- Source: Brazilian E-Commerce Public Dataset by Olist (Kaggle: olistbr/brazilian-ecommerce)
- ~111,708 records, 35+ features after merging 6 relational tables
- Target: review_score >= 4 = happy (1), else unhappy (0)

## Reference Paper
Bachir, M.M. et al. (2024). "Enhancing Customer Satisfaction."
Brazilian Journal of Technology, v.7 n.4. DOI: 10.38152/bjtv7n4-011
Uses the same Olist dataset with Logistic Regression, Decision Tree, and Random Forest.

## Models
Logistic Regression, Decision Tree, Random Forest (best).

## Results (test set)
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|-------|----------|-----------|--------|------|---------|
| Logistic Regression | 0.702 | 0.834 | 0.755 | 0.793 | 0.693 |
| Decision Tree | 0.736 | 0.847 | 0.795 | 0.820 | 0.721 |
| Random Forest | 0.790 | 0.852 | 0.874 | 0.863 | 0.754 |

Best model: Random Forest — matches the paper's finding.

## How to Run
1. Open the notebook in Google Colab
2. Run all cells (dataset downloads automatically via kagglehub)
3. Outputs: metrics table, confusion matrix, saved model (.pkl)

## Files
- Customer_Satisfaction_Prediction_Olist.ipynb — main project
- requirements.txt — dependencies
- output/ — results and charts
