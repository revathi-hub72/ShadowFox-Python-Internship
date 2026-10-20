
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project folder
folder = Path(__file__).parent
file_path = folder / "student-mat.csv"

# Load the real dataset
df = pd.read_csv(file_path, sep=";")

print("\nSTUDENT PERFORMANCE DATA ANALYSIS")
print("=" * 40)

# 1. Explore the dataset
print("\nFirst five records:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumn information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

# 2. Clean the data
print("\nMissing values before cleaning:")
print(df.isnull().sum().sum())

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates().dropna().copy()

print("\nRows after cleaning:", len(df))

# 3. Research question
print("\nResearch Question:")
print("How are study time and school absences related")
print("to students' final mathematics grades?")

print("\nAverage weekly study-time category:",
      round(df["studytime"].mean(), 2))
print("Average absences:", round(df["absences"].mean(), 2))
print("Average final grade:", round(df["G3"].mean(), 2))

print("\nCorrelation with final grade:")
print(df[["studytime", "absences", "G3"]].corr())

# 4. Visualizations
sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="studytime", y="G3",
            x_jitter=0.08, scatter_kws={"alpha": 0.5})
plt.title("Study Time vs Final Grade")
plt.xlabel("Weekly Study Time Category (1-4)")
plt.ylabel("Final Mathematics Grade (0-20)")
plt.tight_layout()
plt.savefig(folder / "study_time_vs_grade.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="absences", y="G3",
            scatter_kws={"alpha": 0.5})
plt.title("School Absences vs Final Grade")
plt.xlabel("Number of Absences")
plt.ylabel("Final Mathematics Grade (0-20)")
plt.tight_layout()
plt.savefig(folder / "absences_vs_grade.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="studytime", y="G3",
            errorbar=None)
plt.title("Average Final Grade by Study-Time Category")
plt.xlabel("Weekly Study Time Category (1-4)")
plt.ylabel("Average Final Grade")
plt.tight_layout()
plt.savefig(folder / "average_grade_by_study_time.png")
plt.show()

plt.figure(figsize=(7, 5))
sns.heatmap(
    df[["studytime", "absences", "G3"]].corr(),
    annot=True, cmap="Blues", fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(folder / "correlation_heatmap.png")
plt.show()

# 5. Findings
study_corr = df["studytime"].corr(df["G3"])
absence_corr = df["absences"].corr(df["G3"])

print("\nKEY FINDINGS")
print("=" * 40)
print(f"Study time and final-grade correlation: {study_corr:.2f}")
print(f"Absences and final-grade correlation: {absence_corr:.2f}")

print("\nConclusion:")
print("The graphs show the relationships between study time,")
print("absences, and final mathematics grades.")
print("Correlation does not prove causation.")

# 6. Save cleaned data and report
df.to_csv(folder / "cleaned_student_performance.csv", index=False)

with open(folder / "analysis_summary.txt", "w", encoding="utf-8") as f:
    f.write("Student Performance Data Analysis\n")
    f.write("Dataset: UCI Student Performance - Mathematics\n")
    f.write(f"Number of records: {len(df)}\n")
    f.write(f"Average final grade: {df['G3'].mean():.2f}\n")
    f.write(f"Study-time correlation: {study_corr:.2f}\n")
    f.write(f"Absences correlation: {absence_corr:.2f}\n")

print("\nAnalysis complete!")
print("Graphs, cleaned data, and summary saved in Task3.")
