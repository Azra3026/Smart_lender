import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('your_dataset.csv') 
# plotting using histplot instead of distplot
plt.figure(figsize=(12, 5))

plt.subplot(121)
sns.histplot(data['ApplicantIncome'], color='r', kde=True)

plt.subplot(122)
sns.histplot(data['Credit_History'], kde=True)

plt.show()
