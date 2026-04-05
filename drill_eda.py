import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Task 1: Summary Statistics
# ----------------------------
def compute_summary(df):
    numeric_df = df.select_dtypes(include='number')
    
    # Create summary where statistics are rows
    summary = pd.DataFrame(index=['count', 'mean', 'median', 'std', 'min', 'max'])
    
    for col in numeric_df.columns:
        summary[col] = [
            numeric_df[col].count(),
            numeric_df[col].mean(),
            numeric_df[col].median(),
            numeric_df[col].std(),
            numeric_df[col].min(),
            numeric_df[col].max()
        ]
    
    # Save CSV
    summary.to_csv("output/summary.csv")
    return summary

# ----------------------------
# Task 2: Distribution Plots
# ----------------------------
def plot_distributions(df, columns, output_path):
    # Create 2x2 subplot figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes = axes.flatten()
    
    for i, col in enumerate(columns):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# ----------------------------
# Task 3: Correlation Heatmap
# ----------------------------
def plot_correlation(df, output_path):
    numeric_df = df.select_dtypes(include='number')
    corr = numeric_df.corr(method='pearson')
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# ----------------------------
# Main function
# ----------------------------
def main():
    # Create output folder if not exists
    os.makedirs("output", exist_ok=True)
    
    # Load CSV
    df = pd.read_csv("data/sample_sales.csv")
    
    # Task 1: Compute summary
    compute_summary(df)
    
    # Task 2: Plot distributions (choose first 4 numeric columns)
    numeric_cols = df.select_dtypes(include='number').columns[:4].tolist()
    plot_distributions(df, numeric_cols, "output/distributions.png")
    
    # Task 3: Plot correlation heatmap
    plot_correlation(df, "output/correlation.png")

# ----------------------------
# Run main if script is executed
# ----------------------------
if __name__ == "__main__":
    main()