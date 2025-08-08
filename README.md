# Retail Market Basket Analysis

## What This Project Is About

This project digs into customer shopping habits using the Apriori algorithm. It finds products that are often bought together, helping retailers understand buying patterns and make smarter decisions — like how to arrange products or run promotions.

What’s Inside

market_basket_analysis.py — The main Python script where all the data cleaning, analysis, and visualization happens.

groceries.csv — The dataset of shopping transactions that we analyze.

strong_association_rules.csv — The output file with the most interesting and useful product association rules.


## How to Get Started

1. Make sure you have Python 3 installed on your computer.


2. Install the libraries needed by running:

pip install pandas mlxtend matplotlib


3. Run the script by typing this in your terminal or command prompt:

python market_basket_analysis.py



## What the Script Does

Loads and tidies up the shopping data.

Converts the data into a format that the Apriori algorithm can understand.

Finds sets of products that frequently appear together (with at least 5% support).

Generates association rules and filters out only the strongest ones (confidence above 60% and lift above 1.2).

Prints easy-to-understand explanations of the top rules.

Saves those important rules to a CSV file you can check out anytime.

Shows a nice bar chart of the 10 most popular products.


## Want to Explore More?

Feel free to tweak the support, confidence, and lift thresholds in the script to find more or fewer patterns, depending on what you want to discover.

## License

This project is open for everyone to use and learn from.


---

Got questions or ideas? Don’t hesitate to reach out!


---
