import plotly.graph_objects as go

def plot(elements): 
    fig = go.Figure()

    for elm in elements:
        df = elm[0]
        x = elm[1]
        y = elm[2]
        fig.add_scatter(x=df[x], y=df[y])

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month",                                        
                    stepmode="backward"),
                dict(count=6, label="6m", step="month",  
                    stepmode="backward"),
                dict(count=1, label="YTD", step="year", 
                    stepmode="todate"),
                dict(count=1, label="1y", step="year", 
                    stepmode="backward"),
                dict(step="all")
            ])
        )
    )
    fig.show()
