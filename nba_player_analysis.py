import pandas as pd

# csv uzantılı dataset'i okuduk
df = pd.read_csv('dataset/nba.csv')

# ilk 10 kaydı çekmek için:
result = df.head(10)

# toplam kaç kayıt olduğunu görmek için:
result = len(df.index)

# tüm oyuncuların maaş ortalaması:
result = df['Salary'].mean()

# en yüksek maaş ne kadar:
result = df['Salary'].max()

# en yüksek maaşı alan oyuncu:
result = df[df['Salary'] == df['Salary'].max()]['Name'].iloc[0]

# yaşı 20-25 arasında olan oyuncuların ismi ve oynadıkları takım:
result = df[(df['Age'] >= 20) & (df['Age'] < 25)][['Name', 'Team', 'Age']].sort_values('Age', ascending=False)

# 'John Holland' isimli oyuncunun oynadığı takım:
result = df[(df['Name'] == 'John Holland')]['Team'].iloc[0]

# Takımlara göre oyuncuların ortalama maaş bilgisi:
result = df.groupby('Team').mean()['Salary']

# Kaç farklı takım var:
result = len(df.groupby('Team'))
result = df['Team'].nunique()

# her takımda oynayan oyuncu sayısı:
result = df['Team'].value_counts()

# ismi içinde 'and' geçen kayıtlar:
df = df.dropna()  # NaN kayıtları sildik hata almamak için
result = df[df['Name'].str.contains('and')]

# İkinci bir yol
def str_find(name):
    if "and" in name.lower():
        return True
    return False


result = df[df['Name'].apply(str_find)]

print(result)
