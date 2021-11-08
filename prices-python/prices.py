import yfinance as yf
import pandas as pd
import plotdata
import calculations

covertColumns = ['Open', 'High', 'Close', 'Low']

plot = plotdata.plot
returns = calculations.returns
drawdown = calculations.drawdown
cagr = calculations.cagr

# msft = yf.Ticker("MSFT")
spy = yf.Ticker("SPY")
upro = yf.Ticker("UPRO")

spyData = spy.history(period="max")
spyData.attrs['Ticker'] = 'SPY'

uproData = upro.history(period="max")
uproData.attrs['Ticker'] = 'UPRO'

# get historical market data
dataFrames = [
    spyData, 
    uproData
]

for i in range(len(dataFrames)):
    #Reseting the index
    dataFrames[i] = dataFrames[i].reset_index()
    #Converting the datatype to float
    for j in covertColumns:
        dataFrames[i][j] = dataFrames[i][j].astype('float64')

    dataFrames[i] = dataFrames[i].set_index('Date')

    # dataFrames[i]['Cumulative Returns'] = returns(dataFrames[i]['Close'])
    dd = drawdown(dataFrames[i]['Close'])
    cag = cagr(dataFrames[i]['Close'])

    print(dataFrames[i].attrs['Ticker'])
    print(f"Draw Down: {dd.min():.2f}%")
    print(f"CAGR: {cag:.2f}%")
    print()

frames = [
    # [dataFrames[0], 'Date', 'Close'], 
    # [dataFrames[1], 'Date', 'Close'], 
    # [dataFrames[0], 'Date', 'Cumulative Returns'], 
    [dataFrames[1], 'Date', 'Cumulative Returns']
]

# plot(frames)
