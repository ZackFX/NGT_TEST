import pandas as pd
import numpy as np
#from firebase import firebase

# Data Check
# Create a DataFrame
df = pd.read_csv('ngt_test_example_data (clean columns).csv')

# Fill NaN cases whit Value 0
df['NAV_Per_Share'] = df['NAV_Per_Share'].fillna(1)

# drop unnecessary columns
to_drop = ['Dividend_Payment_CCY', 'Dividend_PCCY', 'Dividend_Payment_Date', 'Dividend_Per_Share', 'Subfund_Long_Name']
df.drop(to_drop, inplace=True, axis=1)

# Calculate correlation between elements:
# ONES
A = df.iloc[1:252, 6].fillna(1)
B = df.iloc[253:503, 6].fillna(1)
C = df.iloc[504:755, 6].fillna(1)
D = df.iloc[755:1005, 6].fillna(1)

# TWOS
E = df.iloc[1006:1039, 6].fillna(1)
F = df.iloc[1040:1290, 6].fillna(1)
G = df.iloc[1291:1541, 6].fillna(1)
H = df.iloc[1542:1792, 6].fillna(1)
I = df.iloc[1793:2043, 6].fillna(1)

# THREES
J = df.iloc[2044:2293, 6].dropna()
K = df.iloc[2294:2543, 6].dropna()

L = [A, B, C, D, E, F, G, H, I, J, K]


def corr_(L):
    j = 0
    S = []
    while j < len(L):
        for i in range(len(L)):
            R = L[j].corr(L[i])
            S.append(R)
        j = j + 1
    return S


print(corr_(L))

# firebase = firebase.FirebaseApplication('https://nextgatetech-626ca.firebaseio.com/', None)
# data=df
# result=firebase.post('/nextgatetech-626ca', data)
# print(result)
