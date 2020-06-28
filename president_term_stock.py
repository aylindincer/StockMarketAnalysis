#!/usr/bin/env python3

#----------------------------
#Title: president_term_stock.py
#Author: Aylin Dincer
#Script Version: 1.0
#Version Date: November 20, 2018s
#----------------------------

# Import python packages
#----------------------------------
from datetime import datetime, timedelta, date
from pandas_datareader import data as pdr
import pandas as pd
import os
import yfinance as yf
import plotly.offline
from plotly.subplots import make_subplots
import plotly.graph_objs as go
#----------------------------------

# Date Functions
#----------------------------------
# Function used to add 30 day to date.
def add_30days(d1):
    add_days = timedelta(days = 30)
    return (d1 + add_days)
    
# Function used to subtract 10 days from date   
def sub_10days(d1):
    sub_days = timedelta(days = 10)
    return datetime.strftime((d1 - sub_days), "%Y-%m-%d")
    
# Function used to find the difference between two dates   
def days_between(d1, d2):
    return (d2 - d1).days
#----------------------------------
    
# Start and End Dates for Stock Data.
#----------------------------------
startdate = '1985-01-29'
enddate = datetime.today().strftime('%Y-%m-%d')
#----------------------------------

#Setup working directory
#----------------------------------
workdir = input('Output directory path (absolute):')
while not os.path.exists(workdir):
    raise FileNotFoundError('Unable to locate output directory path.')
#----------------------------------

# Setup stock data
#----------------------------------
stockindex = ['^DJI', '^IXIC', '^GSPC', '^RUT']
print('\n','Available major stock indexes:' ,'\n', ','.join(stockindex))
stock = input('What stock are you interested in? ').upper()
    
while stock not in stockindex:
    print('{} is not an available stock. Please type again.'.format(stock))
    stock = input('What stock are you interested in? ').upper()

 
# Download stock data using fix_yahoo_finance
yf.pdr_override()
        
stkdata = None
count = 0
while (stkdata is None) and (count <= 10):
    try:
        stkdata = pdr.get_data_yahoo(stock, start=startdate, end=enddate)
    except ValueError:
        print('Issues connecting to server...Another attempt will be made.')
        pass
    count += 1
    
# Format Dates to datetime    
stkdata.index = [datetime.fromtimestamp(datetime.timestamp(row)).date() for row in stkdata.index]
#----------------------------------

#Create president data frame
#----------------------------------
presdates = {'President': ['George H. W. Bush', 'Bill Clinton','George W. Bush','Barak Obama', 'Donald Trump'],
        'TermBegan': [datetime.strptime('01/20/1989','%m/%d/%Y').date(),
                      datetime.strptime('01/20/1993','%m/%d/%Y').date(),
                      datetime.strptime('01/20/2001','%m/%d/%Y').date(),
                      datetime.strptime('01/20/2009','%m/%d/%Y').date(),
                      datetime.strptime('01/20/2017','%m/%d/%Y').date()],
         'TermEnd': [datetime.strptime('01/20/1993','%m/%d/%Y').date(),
                     datetime.strptime('01/20/2001','%m/%d/%Y').date(),
                      datetime.strptime('01/20/2009','%m/%d/%Y').date(),
                      datetime.strptime('01/20/2017','%m/%d/%Y').date(),
                      date.today(),]
        }

president_df = pd.DataFrame(presdates, columns = ['President', 'TermBegan', 'TermEnd'])
#----------------------------------

#Make a dictionary combing stock data at time presidency term
#----------------------------------
d = {}
for president in president_df.President:
    d[president] = pd.DataFrame(columns = stkdata.columns.copy())
        
    for president, df, in d.items():
        pres_temp = president_df[president_df.President.str.contains(president)]
        d[president] = stkdata.loc[(stkdata.index >= pres_temp.TermBegan.iloc[0]) & (stkdata.index < pres_temp.TermEnd.iloc[0])].copy()      

    # Calculate percent change and date difference from Term Began Stock Price and Date.
    for president, df, in d.items():
        d[president]['PercentChange'] = [((d[president].Close[i] - d[president].Close[0]) / d[president].Close[0]) * 100 for i in range(len(d[president]))]
        d[president]['RelDate'] = [days_between(d[president].index[0], d[president].index[i]) for i in range(len(d[president]))]
#----------------------------------

# Plotly 
#----------------------------------
# Stock Market Index vs Time
# Initialize OHLC chart using the stock market data
plotly.offline.init_notebook_mode()

stkdata_ohlc = go.Ohlc(x = stkdata.index,
                       open = stkdata.Open,
                       high = stkdata.High,
                       low = stkdata.Low,
                       close = stkdata.Close,
                       name = 'Stock Prices')

# Percent Change vs Days Since Inauguration
# Initilize the line plots for each president
tracelist = []
for president, df, in d.items():
    pres_stkdata_plot = go.Scatter(x = d[president].RelDate,
                                   y = d[president].PercentChange,
                                   name = president,
                                   line = dict(width = 2, dash = 'solid'))
    tracelist.append(pres_stkdata_plot)

         
        
# Overlay a vertical line for each president based on term start date
shapes = list()
annotations = list()
for i ,j in zip(president_df.TermBegan, president_df.President):
    shapes.append({'type': 'line',
                   'xref': 'x',
                   'yref': 'y',
                   'x0': i,
                   'y0': 0,
                   'x1': i,
                   'y1': stkdata.Open.max(),
                   'opacity': 0.5,
                   'line': {
                       'color': 'rgb(30, 30, 30)',
                       'width': 1}})
    
# Print the name of each president below the vertical line.
    annotations.append({'x':i,
                        'y': 0,
                        'xref':'x',
                        'yref':'y',
                        'text': j,
                        'showarrow': True,
                        'arrowhead': 7,
                        'ax': 0,
                        'ay': 10})
# Setup figure 1 and 2
fig1 = make_subplots(rows=1, cols=1)
fig2 = make_subplots(rows=1, cols=1)

# Update the labels, titles, shapes, and annotations for each figure.
fig1['layout'].update(yaxis = dict(title = 'Stock Market Index'),
                      xaxis = dict(rangeslider = dict(visible = False), title = 'Time'),
                      annotations = annotations, 
                      shapes = shapes,
                      title = 'OHLC Chart Stock Prices from 1985-01-29 to ' + enddate)
fig2['layout'].update(yaxis = dict(title = 'Percent Change (%)'),
                      xaxis = dict(rangeslider = dict(visible = False), title = 'Days From Inauguration'), 
                      title = 'Percent Change Relative to Inauguration Stock Price')
            
# Add the stock market index data to figure 1
fig1.append_trace(stkdata_ohlc, 1, 1)
    
# Add the percent change data for each president to figure 2
for i in range(len(tracelist)):
    fig2.append_trace(tracelist[i], 1, 1)

# Load the figure and save locally
plotly.offline.plot(fig1, filename='OHLC_stock_presidents.html') 
plotly.offline.plot(fig2, filename='percent_change_presidents.html') 