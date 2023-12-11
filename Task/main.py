import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('/Users/maxhotiuk/3_sem_programming/Task/titanic.csv')

survivors = df['Survived'].value_counts()

dead_count = df[df['Survived'] == 0]['Pclass'].value_counts()

print("Survivors: ", survivors)
print(dead_count)

bins = [0, 30, 60, df['Age'].max()]
labels = ['Young', 'Middle', 'Old']

df['AgeCategory'] = pandas.cut(df[df['Survived'] == 1]['Age'], bins=bins, labels=labels)

age_counts = df['AgeCategory'].value_counts()

age_counts.plot(kind='bar')
plt.title('Distribution of survivors by age category')
plt.xlabel('Age category')
plt.ylabel('Number of survivors')
plt.show()

print("Survivors: ", survivors)
print(dead_count)

gender_counts = df['Sex'].value_counts()

gender_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of passengers by gender')
plt.show()