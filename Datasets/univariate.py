# plotting using histplot instead of distplot
plt.figure(figsize=(12, 5))

plt.subplot(121)
sns.histplot(data['ApplicantIncome'], color='r', kde=True)

plt.subplot(122)
sns.histplot(data['Credit_History'], kde=True)

plt.show()
