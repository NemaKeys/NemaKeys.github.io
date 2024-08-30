#from graphviz import Digraph
import graphviz
import pandas as pd
import openpyxl

def readSpreadSheet():
    fn = '../../Book1.xlsx'
    df = pd.read_excel(fn, sheet_name='Book1')
    df = df.fillna('')
    return df


def Edge2Node_1(df):
    keys = dict()
    for index, row in df.iterrows():
        KeyFrom = str(row['KeyFrom'])
        NodeFrom = str(row['NodeFrom']).strip()
        keys[KeyFrom] = NodeFrom
        KeyTo = str(row['KeyTo'])
        if KeyTo not in keys:
            keys[KeyTo] = ""

    for index, row in df.iterrows():
        KeyTo = str(row['KeyTo'])
        temp = keys[KeyTo]
        if len(temp) < 1:
            df.loc[index, 'NodeTo'] = KeyTo
        else:
            df.loc[index, 'NodeTo'] = temp


    df.to_csv("Edge2Node.csv", sep=',', encoding='utf-8')
    df.to_excel("Edge2Node.xlsx")
    return df



def main():
    # Use a breakpoint in the code line below to debug your script.
    df = readSpreadSheet()
    df = Edge2Node_1(df)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
