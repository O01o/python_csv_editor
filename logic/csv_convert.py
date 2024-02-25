import os
import pandas as pd

def file_rename(path: str, add_text: str):
    dir_name = os.path.dirname(path)
    base_name = os.path.basename(path)
    file_name, ext = os.path.splitext(base_name)
    base_name = f"{file_name}_{add_text}{ext}"
    return os.path.join(dir_name, base_name)

def wide2long(path: str, name: str, overwrite: bool):
    df: pd.DataFrame = pd.read_csv(path)
    if not overwrite: path = file_rename(path, add_text="melt")
    print(df.columns[0])
    df_melted = df.melt(id_vars=[df.columns[0]], var_name=name, value_name='value')
    df_melted.to_csv(path, index=False)