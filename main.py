

import pandas as pd

doc = "C:/Users/m_gray.DESKTOP-Q2TTLA7/Desktop/datasets/asteroids2.csv"
source = "https://www.kaggle.com/basu369victor/prediction-of-asteroid-diameter"

df = pd.read_csv(doc, low_memory=False)

# print(df.shape)
lst = list(df.columns)
# columns = [print(i) for i in list(df.columns)]
print(df.head())
# print(df.tail())
# print(df.isnull().sum())
# drop columns that are not needed - full

# renaming columns

# lst[22] = 'drop'
# lst[16] = 'drop', 23, 24
lst[1] = 'semi-major axis(au)'
lst[2] = 'eccentricity'
lst[25] = 'Magnitude slope parameter'
lst[3] = 'Inclination R(x-y ecliptic plane) deg'
lst[4] = 'Longitude of the ascending node'
lst[5] = 'argument of perihelion'
lst[6] = 'perihelion distance(au)'
lst[7] = 'aphelion distance(au)'
lst[8] = 'Orbital period'
lst[9] = 'data arc-span(d)'
lst[10] = 'Orbit condition code'
lst[12] = 'Absolute Magnitude parameter'
lst[19] = 'gravitational parameter'
lst[20] = 'BV color index'
lst[21] = 'UB color index'

num = 0
for i in lst:
    print(num, lst[num])
    num += 1




