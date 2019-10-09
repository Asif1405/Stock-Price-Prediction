def visualize():
    df = pd.read_csv(fila path) # getting the csv file
    df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d') #changing date to date time object
    df['year']=df.Date.dt.year  #creating year
    df['month']=df.Date.dt.month  #creating month
    df['day']=df.Date.dt.day    #creating day column
    
    
    #Folloing will show the graph of closing price with respect to time
    df.index = df['Date'] setting Date as index
    cl = df['Close'] 
    plt.figure(figsize=(16,8)) 
    plt.plot(cl, label='Closing Prices') 
    plt.title('Time Series') 
    plt.xlabel("Time(year-month)") 
    plt.ylabel("Closing Prices") 
    plt.legend(loc='best')
    plt.show()
    
    #following will show the barchart of closing price with respect to years
    df.groupby('year')['Close'].mean().plot.bar()
    plt.show()

    #following will show the barchart of closing price with respect to month
    df.groupby('month')['Close'].mean().plot.bar()
    plt.show()
    
    
    #following will show the scatter plot of closing price with respect to years and months
    temp=df.groupby(['year', 'month'])['Close'].mean() 
    temp.plot(figsize=(15,5), title= 'Closing Price(Monthwise)', fontsize=14)
    plt.show()
    
    #following will show the barchart of closing price with respect to days of a month
    df.groupby('day')['Close'].mean().plot.bar()
    plt.show()

    df.Timestamp = pd.to_datetime(df.Date,format='%Y-%m-%d')  getting timestrap object
    df.index = df.Timestamp

    #dividing train and test set
    train_set = df[:950]
    test_set = df[950:]
  
    #Plotting train and test data in same graph. it is a line chart
    train_set.Close.plot(figsize=(15,8), title= 'Closing Price', fontsize=14, label='train')

    test_set.Close.plot(figsize=(15,8), title= 'Closing Price', fontsize=14, label='test')

    plt.xlabel("Datetime")
    plt.ylabel("Closing Price")
    plt.legend(loc='best')
    plt.show()
    
    #plotting candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

    fig.update_layout(xaxis_rangeslider_visible=False)

    fig.update_layout(title='Canglestick', yaxis_title='Stock Price',
                      shapes = [dict(x0='2015-01-01', x1='2019-10-03', y0=0, y1=1, xref='x', yref='paper',
                      line_width=2)],annotations=[dict(x='2019-08-31', y=0.05, xref='x', yref='paper',
                      showarrow=False, xanchor='left', text='Increase Period Begins')])
    
    fig.show()
    
    #calculating the rolling(moving) averages
    short_rolling = df["Close"].rolling(window=20).mean()
    long_rolling = df["Close"].rolling(window=100).mean()

    
    #plotting original values along with rolling values
    fig, ax = plt.subplots(figsize=(16,9))

    ax.plot(df.index, df.Close, label='Original')
    ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
    ax.plot(long_rolling.index, long_rolling, label='100 days rolling')

    ax.set_xlabel('Date')
    ax.set_ylabel('Adjusted closing price ($)')
    ax.legend()
    plt.show()
