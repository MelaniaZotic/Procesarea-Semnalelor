import pandas as pd

# Citirea fisierului CSV
file_path = 'Train.csv'
df = pd.read_csv(file_path)

# Convertirea coloanei 'Datetime' la tipul de date datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], format='%d-%m-%Y %H:%M')

# Setarea coloanei 'Datetime' ca index
df.set_index('Datetime', inplace=True)

# Selectarea porțiunii corespunzătoare pentru 3 zile
start_date = '2012-08-25 00:00:00'
end_date = '2012-08-28 00:00:00'
selected_data = df[start_date:end_date]

# Afisarea datelor selectate
print(selected_data)