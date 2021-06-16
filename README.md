# Retail Sales Forecasting

Monthly Sales forecast using the LSTM (Long Short-term Memory) method.

## *Data*

The dataset has 937 rows x 4 columns with date, sale, stock and price columns. It was extracted from a Brazilian top retailer. The data was transformed to protect the identity of the retailer. Data refer to the years 2014, 2015 and 2016.

The data was taken from Kaggle: https://www.kaggle.com/tevecsystems/retail-sales-forecasting

```
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   data     937 non-null    object
 1   venda    937 non-null    int64
 2   estoque  937 non-null    int64
 3   preco    937 non-null    float64
dtypes: float64(1), int64(2), object(1)
```

Grouped dates monthly and added sales:

```
        data  venda
0  2014-01-01   3985
1  2014-02-01   2018
2  2014-03-01   2137
3  2014-04-01   1990
4  2014-05-01   2493
5  2014-06-01   2629
6  2014-07-01   1131
7  2014-08-01   1452
8  2014-09-01   2185
9  2014-10-01   2765
10 2014-11-01   1462
11 2014-12-01   1010
12 2015-01-01   2465
13 2015-02-01   1918
14 2015-03-01   3379
15 2015-04-01   2123
16 2015-05-01    647
17 2015-06-01   2880
18 2015-07-01   3104
19 2015-08-01   1826
20 2015-09-01   2790
21 2015-10-01   3974
22 2015-11-01   3214
23 2015-12-01   3914
24 2016-01-01   2365
25 2016-02-01   2832
26 2016-03-01   2206
27 2016-04-01   4028
28 2016-05-01   4407
29 2016-06-01   6347
30 2016-07-01   5154
```

## *Data Transformation*

* Conversion of data to stationary, if it not is;
* Conversion from time series to supervised to have the feature set of our LSTM model;
* Scale the data;





