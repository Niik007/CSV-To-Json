import pandas as pd
import json

csv_file = pd.read_csv('data.csv')
csv_file = csv_file.dropna()

j2 = (csv_file.groupby(
    ['Base URL', 'Level 1 - Name', 'Level 1 - ID', 'Level 1 - URL', 'Level 2 - Name', 'Level 2 - ID', 'Level 2 URL'])
      .apply(lambda x: x[
    ['Level 3 - Name', 'Level 3 - ID', 'Level 3 URL']].to_dict(
    'records'))
      .reset_index()
      .rename(columns={0: 'children'}))

k2 = (j2.groupby(['Base URL', 'Level 1 - Name', 'Level 1 - ID', 'Level 1 - URL'])
      .apply(lambda x: x[
    ['Level 2 - Name', 'Level 2 - ID', 'Level 2 URL', 'children']].to_dict(
    'records'))
      .reset_index()
      .rename(columns={0: 'children'}))

n2 = (k2.groupby(['Base URL'])
      .apply(lambda x: x[
    ['Level 1 - Name', 'Level 1 - ID', 'Level 1 - URL', 'children']].to_dict(
    'records'))
      .reset_index()
      .rename(columns={0: 'children'})
      .to_json(orient='records'))

parsed = json.loads(n2)
for i in parsed:
    new_df = json.dumps(i, indent=2, sort_keys=False)
    with open('new_output.json', 'w') as cf:
        cf.write(new_df)

