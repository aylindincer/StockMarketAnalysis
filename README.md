# StockMarketAnalysis
An analysis of how certain major events affects the stock market.

Description: This program is used to visualize how different major events affect the stock market. The two topics that can be analyzed using this program are:

1) US Presidents 

2) FDA approval release dates for clinical trials / pharmaceutical companies.

Specifically, the former topic will compare how different presidents affected the stock market during their term and the latter topic will analyze how different FDA release date (approval of drug or approval of clinical trials phase 1, phase 2, etc) can affect the pharmaceutical stock prices.


Expected Output:
1) OHLC (open high low close) chart (vertical line = price range, Left tick = opening price, Right tick = closing price)

2) Stock Price Percent Change

**Please make sure necessary packages below are installed**

Package Dependencies:
1) pandas_datareader (can install using 'conda')
2) fix_yahoo_finance (https://pypi.org/project/fix-yahoo-finance/#description)
    Install using pip install fix-yahoo-finance  (not available on conda)
3) datetime (can install using 'conda')
4) requests (can install using 'conda')
5) re (can install using 'conda')
6) pandas (can install using 'conda')
7) beautifulsoup4 (can install using 'conda')
8) plotly (can install using 'conda')
*******************************************************************

**Instructions**:


Step 1: Choose a topic to analyze.

Topics: Presidency or FDA

1) Presidency: Output will be two plotly graphs.  
        One will be an OHLC (open high low chart) of the stock market index over time
        with the president inauguration dates presented as vertical lines on the chart.
        The other will be a line plot of percent change of the stock market index relative
        to the index from the inauguration date.
2) FDA: Output will be two plotly graphs.
        One will be an OHLC of the pharmaceutical stock price over time
        with the FDA release dates for that specific company presented as vertical lines 
        on the chart.
        The other will be a line plot of percent change of that specific stock price 
        relative to the price from the FDA release date.
        
Step 2: Choose the stock (dependent on the topic you selected previously).

1) For the Presidency topic, you must choose one:
        ^DJI, ^IXIC, ^GSPC,^RUT
        Warning: Input must include '^' character as shown above.
    
2) For the FDA topic, you must choose one:
         ZGNX,ARDM,SPPI,PRTK,GTXI,HEB,FCSC,ACOR,ALKS,MNKD,HRTX,CTIC,ARLZ,JAZZ,VVUS,
         DEPO,PLX,DRRX,PTIE,SGEN,PCRX,ALIM,INCY,ATRS,INSY,CRIS,CORT,EBS,RGEN,ARNA,AMRN,
         HALO,NAVB,SUPN,EXEL,IMGN,DVAX,TTNP,ENDP,AVDL
         
**Notes**:
1) The stock market data start and end dates are hardcoded as 1985-01-29 and the current date. 
Start Date was chosen since that is the earliest data available for all stocks on 
Yahoo! Finance. If there is only stock data up to 2010, it will only include that 
much data. 

2) The fix_yahoo_finance is extremely finicky, meaning it may take a few tries 
to pull data from webpage.
