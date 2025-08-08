import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Load the CSV file
data = pd.read_csv("groceries.csv")

# Step 2: Convert rows into list of items (force strings) 
transactions = []
for i in range(len(data)):
    basket = data.iloc[i].dropna().astype(str).tolist()
    transactions.append(basket)

# Show first 3 baskets (optional)
print("Sample baskets:", transactions[:3])

# Step 3: One-hot encode transactions
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Step 4: Apply Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.05, use_colnames=True)

# Step 5: Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Step 6: Filter strong rules
rules = rules[(rules['confidence'] > 0.6) & (rules['lift'] > 1.2)]

# Sort rules by lift descending
rules = rules.sort_values(by="lift", ascending=False)

# Show top 10 filtered rules
print("\nTop 10 filtered strong rules:\n", rules.head(10))

# Step 7: Interpret rules in plain language
print("\nPlain language interpretation of top rules:\n")
for idx, row in rules.head(10).iterrows():
    print(f"If a customer buys {list(row['antecedents'])}, "
          f"they are {row['confidence']*100:.1f}% likely to also buy {list(row['consequents'])} "
          f"(Lift = {row['lift']:.2f}).")

# Step 8: Save filtered rules to CSV
rules.to_csv("strong_association_rules.csv", index=False)
print("\nFiltered strong rules saved to 'strong_association_rules.csv'")

# Step 9: Visualize top 10 most frequent items
item_freq = df.sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(8,5))
item_freq.plot(kind='bar', color='skyblue')
plt.title("Top 10 Most Frequent Items")
plt.xlabel("Item")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


