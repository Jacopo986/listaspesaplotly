#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.graph_objects as go

listaspesa = [["""carciofi, peperoni, cavolfiori, zucchine, cipolle, aglio, carote, radicchio, 
sedano, verza, piselli, finocchio, fagioli, patate, prezzemolo"""],
              
              """pasta, grissini, pesce, carne, yogurt, riso, biscotti, cioccolata,
              gelato, granita, ghiaccioli, salumi, formaggi"""
              ,
              ['fragole', 'mele', 'pere', 'ciliegie' 'banane', 'pistacchi', 
                'frutta secca', 'licis', 'papaya', 'mango', 'uva', 'arance', 'angurie', ]]


listagenerale = ["verdure","cibo in generale","frutta"]


tabella = go.Figure(data=[go.Table(
    columnwidth= [100,100],
    header=dict(values=["<b>LISTA</b>","<b>****</b>"],align="center",height=30,font_size=15,font_family="bold"),
                                  cells=dict(values=[listagenerale,listaspesa], align="center",height=20))])


tabella.show()










