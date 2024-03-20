# ML-Project-3-Association-Rule-Mining-Apriori
In this README template:

- ## Overview
This project implements the Apriori algorithm for association rule mining. Association rule mining is a technique used to identify patterns or relationships among items in large datasets. The Apriori algorithm is a classic algorithm for finding frequent itemsets and deriving association rules from them.

## Requirements
- Python (version >= 3.6)
- Pandas
- NumPy
- from mlxtend.frequent_patterns import apriori
- from mlxtend.frequent_patterns import association_rules

## Generate frequent item sets that have a support of atleast 7%
Based on the frequent itemsets, generate association rules that capture relationships between items.

Calculate metrics such as support, confidence, and lift for each rule:

Support: The proportion of transactions that contain both the antecedent and consequent of the rule.

Confidence: The conditional probability that a transaction containing the antecedent also contains the consequent.

Lift: The ratio of the observed support of the rule to the expected support if the antecedent and consequent were independent.
