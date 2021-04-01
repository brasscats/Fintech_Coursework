# Correlation exercise

# Import libraries and dependencies
import pandas as pdfrom pathlib import pathlib
import seaborn as sns
%mathplotlib inline


# Read the ice cream slaes data, set the 'month' as the index
ice_cream_data = Path"../____/ice_cream.csv"


# 


# Create seaborn heat map
sns.heatmap(Correlation, vmin=-1, vmax=1)






###Instructur exercise #2: Rolling averages
# Import libraries and dependencies
import pandas as pd
from pathlib import Path
%mathplotlib inline

#Read the TSLA data, set the date as the index, sort in forward chronological order
trsla


#### Student exercise #2
import pandas as pd
from pathlib import Path
%mathplot inline

# set the path 
nflx_data = Path("../Resources/nflx.csv")

# Read the CSV into a datafrmae and set the date as datatime index
nflx_df = pd.read_csv(nflx_data, index_col="date", infer_datetime_format=True, parse_dates=True)
nflx_df.sort_index()  #sort index
nflx_df.plot() # plot data frame


# set figure of the daily closing prices of NFLX
axie = nflx_df.plt(figsize(25,10))





### Instructer demo: Beta

#import libraries and dependencies
#read CSVs in the dataframs

#Calculate covariance of all daily retursn of AMZon vs. S&P 500
covariance = daily_retruns['AMZN'].cov(daily_returns['S&P 500'])
covariance

# calculate vaiance of all retursn of AMZOn vs. S&P 500
variance = dailiy_returns['S&P 500']


# Calc. 30-day rolling beta of amzn and plot the data
rolling_beta = rolling_covarince / rolling_variance
rolling_beta.plot(figsize=(20, 100)
                  
# Beta vs. Correlation
import seaborn as sns
sns.lmplot(x="S&P 500", y='AMZN', data=daily_returns, aspect=1.5, fit_reg=True)






###TA Exercise Lesson #4

# Calculate covariance of all daily returns of social meda





####Instructer Exercise #3 Portfolio Returns

#libraries & dependencies
#Read CSV file
#Create a new pivot table
all_prices = pd.concat([amd], ___)  

#Portfolio Returns
all_returns = all_prices.pct_change()
all.returns.head()

amd_weight = 0.5
mu_weight = 0.5

portfolio_returns = amd_weight * all_returns["AMD"] + mu_weight * all_retuns["MU"]
portfolio_returns.head()

weights = [0.5, 0.5]
portfolio_returns = all_returns.dot(weights)
portfolio_retruns.head()

####TA Demo: Student Activeity: Portfolio Planner, Pt. 1

#Import pandas & dependencies 
import pandas as pd
import pathlib as Path


# import CSVs

# create data frames
bk_df = pm.read_csv(nk_data)....


#Combine DataFrames, sort index and rename Columns
combined_df = pd.conca(nk_df, fang_df, jnj_df, luv_df, mu_df, nke_df, sbux_df, t_du, wdc_df, wrk_df], axis="coluns", join="inner")


####TA Demo: Student Activeity: Portfolio Planner, Pt. 2