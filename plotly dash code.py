#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 22:37:43 2018

@author: aggrajat
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import pandas as pd
import plotly.graph_objs as go
# Create your connection.
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )
cnx = sqlite3.connect('./db.sqlite3')
df = pd.read_sql_query("SELECT * FROM Optracker_optrackertable", cnx)
print(df.head())
app = dash.Dash()

app.layout = html.Div(children=[
       html.H4(children='OPPORTUNITY TRACKER'),
       generate_table(df)
])
cnx.close()
df.reset_index(drop=True)
type_of_oppertunity_count=df.groupby(['type_of_opportunity']).size().reset_index(name='counts')
type_of_oppertunity_count_table=type_of_oppertunity_count
type_of_oppertunity_count_table.columns = ["Type of Opportunity","Counts"]

status_vs_team_name=df.groupby(['status','team_name']).size().reset_index(name='counts')
status_vs_team_name.columns=['Status','Team Name',"Counts"]

status_vs_count=df.groupby(['status']).size().reset_index(name='counts')
status_vs_count.columns=['Status',"Counts"]

Assign_to_vs_count=df.groupby(['assign_to']).size().reset_index(name='counts')
Assign_to_vs_count.columns=['Assign To',"Counts"]


colors = {
    'background': '#000000',
   'text': '#7FDBFF'
}
#print(type_of_oppertunity_count['type_of_opportunity'][0])
app.layout = html.Div(children=[html.Div(style={'backgroundColor': "#0000000"}, children=[html.Div(style={'backgroundColor': "#0000000"}, children=[
html.A(html.Button('back', className='three columns'),
    href='http://10.92.108.178:8000/Optracker/')
,
    html.H1(
        children='OPPORTUNITY TRACKER',
        style={
            'textAlign': 'center',
            #'color': colors['text']
        }
    ),

    html.Div(children='Process V/S Tools', style={
        'textAlign': 'center',
        #'color': colors['text']
    }),

    dcc.Graph(
        id='g1',
        figure={
            'data': [
                {'x': [type_of_oppertunity_count["Type of Opportunity"].iloc[0]], 'y': [type_of_oppertunity_count["Counts"].iloc[0]], 'type': 'bar', 'name': 'Process'},
                {'x': [type_of_oppertunity_count["Type of Opportunity"].iloc[1:]], 'y': [type_of_oppertunity_count["Counts"].iloc[1]], 'type': 'bar', 'name': 'Tools'},
            ],
            'layout': {
                #'plot_bgcolor': "#0000000",
                #'paper_bgcolor': "#0000000",
                #'font': {
                    #'color': colors['text']
               # }
            }
        }
    )
], className="six columns"),
    html.Div(style={'backgroundColor':  "#0000000"}, children=[
    #html.H1(
        #children='OPPORTUNITY TRACKER',
        #style={
            #'textAlign': 'center',
            #'color': colors['text']
       # }
    #),

    html.Div(children='OPEN V/S WORK IN PROGRESS V/S Closed', style={
        'textAlign': 'center',
        #'color': colors['text'],

    }),

    dcc.Graph(
        id='g2',
        figure={
            'data': [
                {'x': [status_vs_count["Status"].iloc[0]], 'y': [status_vs_count["Counts"].iloc[0]], 'type': 'bar', 'name': 'Open'},
                {'x': [status_vs_count["Status"].iloc[1]], 'y': [status_vs_count["Counts"].iloc[1]], 'type': 'bar', 'name': 'Work in progress'},
#                {'x': [status_vs_count["Status"].iloc[2:]], 'y': [status_vs_count["Counts"].iloc[2]], 'type': 'bar', 'name': 'closed'},
            ],
            'layout': {
                #'plot_bgcolor': colors['background'],
                #'paper_bgcolor': colors['background'],
                #'font': {
                    #'color': colors['text']
               # }
            }
        }
    )
]),
html.Div(style={'backgroundColor':  "#0000000"}, children=[
#    html.H1(
#        children='OPPORTUNITY TRACKER',
#        style={
#            'textAlign': 'center',
#            'color': colors['text']
#        }
#    ),

    html.Div(children='Assign To', style={
        'textAlign': 'center',
        #'color': colors['text'],
    }),

    dcc.Graph(
        id='g3',
        figure={
            'data': [
                {'x': Assign_to_vs_count["Assign To"], 'y': Assign_to_vs_count["Counts"], 'type': 'bar', 'name': ''},
                #{'x': [Assign_to_vs_count["Assign To"].iloc[1]], 'y': [Assign_to_vs_count["Counts"].iloc[1]], 'type': 'bar', 'name': 'Work in progress'},
            ],
            'layout': {
                #'plot_bgcolor': colors['background'],
                #'paper_bgcolor': colors['background'],
                #'font': {
                 #   'color': colors['text']
                #}
            }
        }
    )
])])])#,className="six columns")
#    ],className="row")
#    ,html.Div(children=[
#       html.H4(children='OPPORTUNITY TRACKER'),
#       generate_table(status_vs_count)
#]),
#
#html.Div(children=[
#       html.H4(children='OPPORTUNITY TRACKER'),
#       generate_table(type_of_oppertunity_count)
#]),
#    html.Div(children=[
#       html.H4(children='OPPORTUNITY TRACKER'),
#       generate_table(Assign_to_vs_count)
#]),




if __name__ == '__main__':
    app.run_server(debug=True,host='10.92.108.178',port=8060)
