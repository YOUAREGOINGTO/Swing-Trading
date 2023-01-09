#!/usr/bin/env python
# coding: utf-8

# ## ADR (SWING TRADING INDICATOR)

# The Code Only Works for Indian Stocks and you have to use the NSE Symbols.

# ## Logic

# In Swing Trading one has to Select the Stocks which have the Highest Probability to increase over next few days.

# ADR Takes last 20 Days into Account and by below formula we calculate the ADR Value

# ## Formula

# Formula = ((H1/L1) + (H2/L2) + ....+ (H20/L20))/20 -1 [H-High,L-Low] Calculation is For Last 20 Days.

# In[ ]:


symbol ="UNIONBANK" # NSE SYMBOLS


# In[14]:



from datetime import date
from datetime import datetime

current_datetime = datetime.now()

stock_data = nse.get_history(symbol = symbol ,start = date(2022,12,1),end = date.today())
r = stock_data.tail(20)
r["ADR"] = r['High']/r['Low']
k = (r["ADR"].mean() - 1)*100

k


# In[ ]:




