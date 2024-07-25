import matplotlib.pyplot as plt
import pandas as pd

tasks_extended = {
    'Task': [
        'Data Collection', 
        'Data Preprocessing', 
        '(Linear Regression algorithm)', 
        'Model Evaluation and Feedback'
    ],
    'Start': [
        '2024-05-02', 
        '2024-05-08', 
        '2024-05-12', 
        '2024-06-02'
    ],
    'Finish': [
        '2024-05-07', 
        '2024-05-11', 
        '2024-06-01', 
        '2024-06-10'
    ]
}

# Create a DataFrame
df_extended = pd.DataFrame(tasks_extended)
df_extended['Start'] = pd.to_datetime(df_extended['Start'])
df_extended['Finish'] = pd.to_datetime(df_extended['Finish'])
fig, ax = plt.subplots(figsize=(12, 6))
for i, task in df_extended.iterrows():
    ax.barh(task['Task'], (task['Finish'] - task['Start']).days + 1, left=task['Start'])
ax.set_xlabel('Date')
ax.set_ylabel('Task')
ax.set_title('Stock Prediction Project - Extended Dates Gantt Chart')
plt.xticks(pd.date_range(start='2024-05-02', end='2024-06-10', freq='D'), rotation=45)
plt.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()
