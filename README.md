# Stock Market and President Term Analysis
## Overview

The president_term_stock.py script will analyze the stock market within each of the president's term starting from 1985. 

Two plotly plots are generated: 
1. Stock market index versus time OHLC plot
![](https://github.com/aylindincer/Stock_Market_Analysis/blob/master/examples/OHLC_stock_presidents.png) 
2. Stock market percent change since inauguration for each president.
![](https://github.com/aylindincer/Stock_Market_Analysis/blob/master/examples/percent_change_presidents.png) 
Note: These plots are saved locally as an .html file type and are interactive.

The scripts perform the following steps:
- Pulls stock data from https://finance.yahoo.com
- Generates a president data frame
- Combines the stock data for each presidency term
- Setup the plots using plotly.offline

## To Use:
1. Download and install:
- python 3 (https://www.python.org/)
- pandas package (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
- yfinance package (https://pypi.org/project/yfinance/)
- plotly package (https://plotly.com/python/getting-started/#installation)

2. Download from this repository:
 - president_term_stock.py

3. Open the terminal and run the president_term_stock.py script.
```
python ./president_term_stock.py /absolute_path/to/output_directory
```
Note:  output directory should exist before running script.

4. Input a stock market index (options: '^DJI', '^IXIC', '^GSPC', '^RUT')

## Script Output Description

The output directory will contain the following: 
1.	OHLC_stock_presidents.html
2.	percent_change_presidents.html

**OHLC_stock_presidents.html**
: An OHLC chart displaying the open, high, low, and closing prices for each time point. A black vertical line is placed at the beginning of each president term.

**percent_change_presidents.html**
: A plot of the percent change relative to the stock price from the inaugration date for each president.

Both plots are interactive.  You are able to, zoom, select, hover over plot for specific values, or download plots as a png.
