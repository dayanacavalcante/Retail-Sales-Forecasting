# Imports
import pandas as pd
import os
from datetime import datetime
import plotly.graph_objects as go
import plotly.offline as py
import plotly.io as pio
import statsmodels.formula.api as smf

# Load Data
for dirname, _, filenames in os.walk('C:\\Users\\RenanSardinha\\Documents\\Data Science\\Projects\\Retail-Sales-Forecasting\\Data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

sales = pd.read_csv('C:\\Users\\RenanSardinha\\Documents\\Data Science\\Projects\\Retail-Sales-Forecasting\\Data\\mock_kaggle.csv')
print(sales)
print(sales.info())

sales['data'] = pd.to_datetime(sales['data'])

# Aggregate data at the monthly level and add the sales column
sales['data'] = sales['data'].dt.year.astype('str') + '-' + sales['data'].dt.month.astype('str') + '-01'
sales['data'] = pd.to_datetime(sales['data'])

# Groupby date and sales sum
sales = sales.groupby('data').venda.sum().reset_index()
print(sales)

# Data Transformation
# check if the data is stationary
# Plot Monthly Sales
plot_data = [go.Scatter(x = sales['data'], y = sales['venda'],)]
plot_layout = go.Layout(title='Montly Sales')
fig = go.Figure(data=plot_data, layout=plot_layout)
fig.show()
#pio.write_html(fig, file='figure.html', auto_open=True)

# Diff
df_diff = sales.copy()

# Add previous sales to the next row
df_diff['prev_sales'] = df_diff['venda'].shift(1)

# Drop the null values and calculate the difference
df_diff = df_diff.dropna()
df_diff['diff'] = (df_diff['venda'] - df_diff['prev_sales'])
print(df_diff)

# Plot it again and check if it is stationary now:
# Plot Sales diff
plot_data = [go.Scatter(x=df_diff['data'], y=df_diff['diff'])]
plot_layout = go.Layout(title='Diff Montly Sales')
fig2 = go.Figure(data=plot_data, layout=plot_layout)
fig2.show()
#pio.write_html(fig2, file='figure2.html', auto_open=True)

# Lock-back=12
# lag_1 to lag_12
# Create dataframe for transformation from time series to supervised
df_supervised = df_diff.drop(['prev_sales'], axis=1)

# Adding lags
for inc in range(1,13):
    field_name = 'lag_' + str(inc)
    df_supervised[field_name] = df_supervised['diff'].shift(inc)

# Drop null values
df_supervised = df_supervised.dropna().reset_index(drop=True)
print(df_supervised)


