import yfinance as yf
import pandas as pd
import plotdata
import calculations

covertColumns = ['Open', 'High', 'Close', 'Low']

plot = plotdata.plot
transformPercentageChange = calculations.calculatePercentChange
transformInvestOnColumnChange = calculations.calculateInvestmentAggreatePercentage

# msft = yf.Ticker("MSFT")
spy = yf.Ticker("SPY")
upro = yf.Ticker("UPRO")

print(upro.actions)

# get historical market data
df = spy.history(period="max")
dfu = upro.history(period="max")

dataFrames = [
    df, 
    dfu
]

for i in range(len(dataFrames)):
    #Reseting the index
    dataFrames[i] = dataFrames[i].reset_index()
    #Converting the datatype to float
    for j in covertColumns:
        dataFrames[i][j] = dataFrames[i][j].astype('float64')
    
    transformPercentageChange(dataFrames[i], 'Close', 'PercentChange')

    dataFrames[i]['Cumulative Returns'] = 10000 * (dataFrames[i]['PercentChange'] + 1).cumprod()
    dataFrames[i]['Cumulative Returns'][0] = 10000
    print(dataFrames[i].head())

frames = [
    # [dataFrames[0], 'Date', 'Close'], 
    # [dataFrames[1], 'Date', 'Close'], 
    # [dataFrames[0], 'Date', 'Cumulative Returns'], 
    [dataFrames[1], 'Date', 'Cumulative Returns']
]

plot(frames)

# show actions (dividends, splits)
# msft.actions

# # show dividends
# msft.dividends

# # show splits
# msft.splits

# # show financials
# msft.financials
# msft.quarterly_financials

# # show major holders
# msft.major_holders

# # show institutional holders
# msft.institutional_holders

# # show balance sheet
# msft.balance_sheet
# msft.quarterly_balance_sheet

# # show cashflow
# msft.cashflow
# msft.quarterly_cashflow

# # show earnings
# msft.earnings
# msft.quarterly_earnings

# # show sustainability
# msft.sustainability

# # show analysts recommendations
# msft.recommendations

# # show next event (earnings, etc)
# msft.calendar

# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# msft.isin

# # show options expirations
# msft.options

# # show news
# msft.news