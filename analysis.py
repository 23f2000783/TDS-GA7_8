# LLM-assisted by ChatGPT Codex/Jules
# Contact: 23f2000783@ds.study.iitm.ac.in
#
# Usage:
#   python analysis.py
# Outputs:
#   - chart_trend.png (quarterly scores vs industry target)
#   - summary.txt (key stats) and console output

import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("patient_satisfaction_2024.csv")
    avg = df["Patient_Satisfaction_Score"].mean()

    # Save summary
    summary = [
        f"Average score (2024): {avg:.2f}",
        f"Industry target: {df['Industry_Target'].iloc[0]:.2f}",
        f"Lowest quarter: {df.loc[df['Patient_Satisfaction_Score'].idxmin(), 'Quarter']}",
        f"Highest quarter: {df.loc[df['Patient_Satisfaction_Score'].idxmax(), 'Quarter']}",
        f"Gap to target: {df['Industry_Target'].iloc[0] - avg:.2f}",
    ]
    with open("summary.txt", "w") as f:
        f.write("\n".join(summary))
    print("\n".join(summary))

    # Visualization: quarterly trend and benchmark
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(df["Quarter"], df["Patient_Satisfaction_Score"], marker="o", label="Patient Satisfaction Score")
    ax.axhline(df['Industry_Target'].iloc[0], linestyle="--", label="Industry Target (4.5)")
    ax.set_title("Patient Satisfaction Scores – 2024 vs Industry Target")
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Score")
    ax.legend()
    fig.tight_layout()
    fig.savefig("chart_trend.png", dpi=150)

if __name__ == "__main__":
    main()
