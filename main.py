import datetime
import pandas as pd


t = datetime.date.today()
start_year = 2011
current_year = t.year
gen_year_list = [
    start_year + count for count in range(1, (current_year - start_year) + 1)
]
country = "NO"

# If no headers are passed from a "legit" browser you will get 403.
headers = {
    "User-Agent": "Mozilla Firefox v14.0",
    "Connection": "keep-alive",
}

pd.options.plotting.backend = "plotly"

# df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))


for year in gen_year_list:
    country_year_scoreboard = f"https://ctftime.org/stats/{year}/{country}"

    df_country_year = pd.read_html(country_year_scoreboard, storage_options=headers)
    df = df_country_year[0].dropna(axis=1)  # drop cols containing NA
    result = df.to_json(orient="columns") # dump the table to json
    print(result)
    break

