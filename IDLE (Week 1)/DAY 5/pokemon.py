import pandas as pd
 
poke = pd.read_csv('Pokemon.csv')
poke_power = poke[['Name', 'Total']].sort_values(by='Total',ascending=False).head(6) # 1.
print(poke_power)

print('\n')

poke_non_legendary = (poke[poke['Legendary'] == False])
my_top_6 = poke_non_legendary[['Name', 'Total', 'Legendary']].sort_values(by='Total',ascending=False).head(6) # 2.
print(my_top_6)

print('\n')

no_duplicates_poke = poke_non_legendary[['Name', 'Type 1', 'Total', 'Legendary']].sort_values(by='Total',ascending=False)
no_duplicates_poke = no_duplicates_poke.drop_duplicates('Type 1').head(6)
print(no_duplicates_poke)
