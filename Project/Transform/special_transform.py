import pandas as pd
import os

file_path = '../Project/files/Speciál_termékek/'
output_folder = '../Project/files/Speciál_termékek/Transformed/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

all_files = [f for f in os.listdir(file_path) if f.endswith('.csv')]
all_dataframes = []
for file_name in all_files:
    file_full_path = os.path.join(file_path, file_name)

    data = []
    with open(file_full_path, 'r', encoding='utf-8') as file:
        for line in file:
            row = line.strip().split(';')
            data.append(row)

    max_length = max(len(row) for row in data)

    columns = [f'Column_{i+1}' for i in range(max_length)]

    df = pd.DataFrame(data, columns=columns)

    for index, row in df.iterrows():
        if '%' in row['Column_1']:
            df.iloc[index, :] = df.iloc[index, :].shift(-1)

    for index, row in df.iterrows():
        if 'Hiányzó termékfotó' in row['Column_1']:
            df.iloc[index, :] = df.iloc[index, :].shift(-1)

    group = df.iloc[-1, 0]
    categ = df.iloc[-1, 1]
    name = df.iloc[-1, 2]
    
    columns_to_drop = ['Column_1', 'Column_3', 'Column_6', 'Column_7', 'Column_8', 'Column_9']

    columns_to_drop = [col for col in columns_to_drop if col in df.columns]

    if columns_to_drop:
        df.drop(columns_to_drop, axis=1, inplace=True)
    
    df.drop_duplicates()

    df.rename(columns={'Column_2': 'Termék neve', 'Column_4': 'Bolt', 'Column_5': 'Ár(Ft)'}, inplace=True)
    df['Ár(Ft)'] = df['Ár(Ft)'].str.replace(' Ft', '')
    df['Ár(Ft)'] = df['Ár(Ft)'].str.replace(' ', '')
    df.dropna(how='all', axis=1, inplace=True)

    df['Name'] = name
    df['Categ'] = categ
    df['Group'] = group
    
    df = df.drop(df.index[-1])

    all_dataframes.append(df)

combined_df = pd.concat(all_dataframes, ignore_index=True)

output_file_name = "Specials.xlsx"
output_file_path = os.path.join(output_folder, output_file_name)

combined_df.to_excel(output_file_path, index=False)