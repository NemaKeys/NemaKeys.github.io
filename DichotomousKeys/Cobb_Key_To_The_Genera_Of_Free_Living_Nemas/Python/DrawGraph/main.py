#from graphviz import Digraph
import graphviz
import pandas as pd
import openpyxl

def readSpreadSheet():
    fn = '../../Book1_Working_On_2024_08_28.xlsx'
    df = pd.read_excel(fn, sheet_name='Book1')
    df = df.fillna('')
    return df

def label2(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    str = ""
    for i in grouped_words:
        str = str + i + "\n"
    return str



def draw(df):
    #http://nemaplex.ucdavis.edu/Uppermnus/nematamnu.htm#Taxonomic_Keys
    #http://nemaplex.ucdavis.edu/Taxadata/Tylenchidaekey2008.htm
    GraphTitle = 'Cobb\nKEY TO THE GENERA\nOF\nFREE-LIVING_NEMAS'
    g = graphviz.Digraph('GraphTitle', comment="FOO",filename = 'NematodaKey.gv') #, node_attr={'color': 'lightblue2', 'style': 'filled'} )
    g.graph_attr['rankdir'] = 'LR'
    g.attr(label=GraphTitle)
    g.node('000', label=GraphTitle,fillcolor='red',style="filled",rank='same')
    g.edge('000', '1', label2(''))

    #cnt=0
    #cntm = 1300
    for index, row in df.iterrows():
        KeyFrom = str(row['KeyFrom'])
        KeyTo = str(row['KeyTo']).strip()
    #    g.node(KeyFrom, rank='same')
        if not KeyTo.isnumeric():
            g.node(KeyTo, shape='doubleoctagon', label=KeyTo)


    cnt=0
    for index, row in df.iterrows():
        KeyFrom = str(row['KeyFrom'])
        KeyTo = str(row['KeyTo']).strip()


        #if KeyTo.isdigit():
        #    KeyTo = KeyTo.zfill(3)
        #if KeyFrom.isdigit():
        #    KeyFrom = KeyFrom.zfill(3)

        Description = str(row['Edge']).strip()
        if len(Description) < 2:
            continue
        #g.node(KeyFrom, KeyTo,fillcolor='aqua',style="filled" )
        g.edge(KeyFrom,KeyTo, label2(Description))
        #if cnt > cntm:
        #  break
        #cnt = cnt +1


    #g.render('NematodaKey.gv', format='svg', view=True,engine='neato')
    g.render('NematodaKey.gv', format='svg', view=True,engine='dot')
    #g.render('NematodaKey.gv', format='svg', view=True,engine='fdp') #NOT WORKING
    #g.render('NematodaKey.gv', format='svg', view=True,engine='nop') #NOT WORKING
    #g.render('NematodaKey.gv', format='svg', view=True,engine='sfdp')
    #g.render('NematodaKey.gv', format='jpg', view=False,engine='dot')
    #g.render('NematodaKey.gv', format='plain', view=True,engine='dot')
    #g.render('NematodaKey.gv', format='pdf', view=False,engine='dot')


    #g.node('', '',fillcolor='aqua',style="filled" )
    #g.edge('','', label2('')
    #g.edge('','', label2('')


def main():
    # Use a breakpoint in the code line below to debug your script.
    df = readSpreadSheet()
    draw(df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
