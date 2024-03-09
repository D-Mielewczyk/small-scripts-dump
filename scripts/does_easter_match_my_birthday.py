import pandas as pd
from dateutil.easter import easter

start_year = 1800
end_year = 2250
birthday = "03-23"  # MM-DD

data = []

for year in range(start_year, end_year + 1):
    easter_date = pd.Timestamp(easter(year))
    is_easter_on_birthday = easter_date == pd.Timestamp(f"{year}-{birthday}")
    is_great_monday_on_birthday = (easter_date + pd.Timedelta(days=1)) == pd.Timestamp(
        f"{year}-{birthday}"
    )
    data.append([year, easter_date, is_easter_on_birthday, is_great_monday_on_birthday])

df = pd.DataFrame(
    data,
    columns=[
        "Year",
        "Easter",
        f"Is Easter on {birthday}",
        f"Is Great Monday on {birthday}",
    ],
)

easter_on_birthday_df = df[df[f"Is Easter on {birthday}"] == True]
great_monday_on_birthday_df = df[df[f"Is Great Monday on {birthday}"] == True]


separator_length = len(easter_on_birthday_df.to_string().split("\n")[0])

print(easter_on_birthday_df)
print("-" * separator_length)
print(great_monday_on_birthday_df)
