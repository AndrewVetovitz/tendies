from functools import reduce

def calculatePercentChange(df, changeColumn, newColumnName = 'PercentChange'):
    df[newColumnName] = df[changeColumn].pct_change(1)

def calculateInvestmentAggreatePercentage(df, percentChangeColumn, newColumnName = 'AggregatePercentageChange'):
    df.loc[0, newColumnName] = df.loc[0, percentChangeColumn]
    # Then iterate through the remaining rows and fill the calculated values:

    for i in range(1, len(df)):
        df.loc[i, newColumnName] = df.loc[i, percentChangeColumn] + df.loc[i - 1, newColumnName]

