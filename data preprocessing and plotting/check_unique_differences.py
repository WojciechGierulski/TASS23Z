import pandas as pd

# Wczytaj pierwszy plik CSV
df1 = pd.read_csv('FINANSES_dataset.csv')

# Wczytaj drugi plik CSV
df2 = pd.read_csv('ORGANIZATIONS_dataset.csv')

# Unikalne wartości z pierwszego pliku
unikalne_wartosci_df1 = set(df1['Country']).union(set(df1['Partner']))

# Unikalne wartości z drugiego pliku
unikalne_wartosci_df2 = set(df2['country1']).union(set(df2['country2']))

# Wartości występujące tylko w jednym pliku
wartosci_tylko_df1 = unikalne_wartosci_df1 - unikalne_wartosci_df2
wartosci_tylko_df2 = unikalne_wartosci_df2 - unikalne_wartosci_df1

# Wyświetl wyniki
# print("Unikalne wartości z pierwszego pliku:", unikalne_wartosci_df1)
# print("Unikalne wartości z drugiego pliku:", unikalne_wartosci_df2)
print("Wartości występujące tylko w pierwszym pliku:\n", wartosci_tylko_df1)
print("\n\nWartości występujące tylko w drugim pliku:\n", wartosci_tylko_df2)
