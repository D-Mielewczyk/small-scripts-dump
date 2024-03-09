import pandas as pd
from dateutil.easter import easter

start_year = 2000
end_year = 2250
birthday = '03-23' # MM-DD

data = []

for year in range(start_year, end_year + 1):
    easter_date = pd.Timestamp(easter(year)) # Convert easter date to Timestamp here
    is_birthday = easter_date == pd.Timestamp(f'{year}-{birthday}')
    data.append([year, easter_date, is_birthday])

# Creation of DataFrame
df = pd.DataFrame(data, columns=['Year', 'Easter', f'Is Great Sunday on {birthday}'])

print(df.head(), "-"*50, sep="\n")
print(df[df[f'Is Great Sunday on {birthday}'] == True])
