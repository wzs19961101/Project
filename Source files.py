import pandas as pd
from bs4 import BeautifulSoup



cf_link = 'https://finance.yahoo.com/quote/AAPL/cash-flow?p=AAPL'

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(cf_link)
import time
time.sleep(10)
html = driver.execute_script('return document.body.innerHTML;')
soup = BeautifulSoup(html,'html.parser')

close_price = [entry.text for entry in soup.find_all('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})]
after_hours_price = [entry.text for entry in soup.find_all('span', {'class':'C($primaryColor) Fz(24px) Fw(b)'})]
print(after_hours_price)

features = soup.find_all('div', class_='D(tbr)')

headers = []
temp_list = []
label_list = []
final = []
index = 0

#create headers
for item in features[0].find_all('div', class_='D(ib)'):
    headers.append(item.text)

#statement contents
while index <= len(features)-1:
    #filter for each line of the statement
    temp = features[index].find_all('div', class_='D(tbc)')
    for line in temp:
        #each item adding to a temporary list
        temp_list.append(line.text)
    #temp_list added to final list
    final.append(temp_list)
    #clear temp_list
    temp_list = []
    index+=1

df = pd.DataFrame(final[1:])
df.columns = headers


# function to make all values numerical (or - for NaNs)
def convert_to_numeric(column):
    first_col = [i.replace(',', '') for i in column]
    second_col = [i.replace('-', '') for i in first_col]
    final_col = pd.to_numeric(second_col)

    return final_col


for column in headers[1:]:
    df[column] = convert_to_numeric(df[column])

final_df = df.fillna('-')
print(final_df)

# Discounted Cash Flow Formula
#DCF = cf/(1+r)^1 + cf/(1+r)^2 + cf/(1+r)^3····cf/(1+r)^n
#cf - cash flow
#r - interest rate
# picking up cash flow from the table
cf_1 = final_df.iloc[11,1]
cf_2 = final_df.iloc[11,2]
cf_3 = final_df.iloc[11,3]
cf_4 = final_df.iloc[11,4]
cf = [cf_1, cf_2, cf_3, cf_4]
print(cf)
growth_rate = ((cf_1 - cf_2)/cf_2 + (cf_2 - cf_3)/cf_3 + (cf_3 - cf_4)/cf_4)/3
k = growth_rate
print(k)
PV = cf_1 / (k/(1+0.03 - k))
R = k/(1+0.03 - k)
print(R)
print(PV)

import yfinance as yf
AAPL = yf.Ticker("AAPL")

# get stock info
AAPL.info

Share_Outstanding = AAPL.info["sharesOutstanding"]
print(Share_Outstanding)
stock_valuation = PV*1000/Share_Outstanding
print ("stock_valuation",stock_valuation)
print("price",after_hours_price)
import  numpy_financial
PV_2 = numpy_financial.pv(R,100,-1*cf_1)
stock_valuation2 = PV_2*1000/Share_Outstanding
print (PV_2)
print (stock_valuation2)

