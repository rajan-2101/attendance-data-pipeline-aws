import pandas as pd
import matplotlib.pyplot as plt

# Load parquet file
df = pd.read_parquet("attendance.parquet")

# Convert timestamp column to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

print("Data Preview:")
print(df.head())

# -------------------------------
# 1. Attendance Distribution (Pie)
# -------------------------------
plt.figure()
df['status'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    colors=['#4CAF50', '#F44336']
)
plt.title("Attendance Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("attendance_distribution.png")


# -------------------------------
# 2. Daily Attendance Trend (Line)
# -------------------------------
plt.figure()
df.groupby(df['timestamp'].dt.date)['status'].count().plot(marker='o')
plt.title("Daily Attendance Trend")
plt.xlabel("Date")
plt.ylabel("Number of Records")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("attendance_trend.png")


# -------------------------------------
# 3. Attendance % per Student (Bar)
# -------------------------------------
attendance_pct = df.groupby('name')['status'].apply(
    lambda x: (x == 'Present').mean() * 100
)

plt.figure()
attendance_pct.sort_values().plot(kind='bar', color='#2196F3')
plt.title("Attendance % per Student")
plt.xlabel("Student Name")
plt.ylabel("Attendance %")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("attendance_percentage.png")


# -------------------------------
# Show plots (optional)
# -------------------------------
plt.show()