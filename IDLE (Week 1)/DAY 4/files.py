countries = open('cotw.csv')

for lines in countries:
  print(lines.split()[0])
