

import pandas as pd
import numpy as np
from tabulate import tabulate
df = pd.read_excel(r"C:\Users\USER\Desktop\Merged Scrape List.xlsx")
print(df)

# df = df.fillna('')
# del df['Unnamed: 10']
# del df['Unnamed: 11']
# del df['Unnamed: 12']


# l = [12,25,36,53,64,75]
# l_mod = [0] + l + [max(l)+1]
# df2 = [df.iloc[l_mod[n]:l_mod[n+1]] for n in range(len(l_mod)-1)]





# insta=df2[0]
# fb=df2[1]
# wiki=df2[2]
# twt=df2[3]
# yt=df2[4]
# gs=df2[5]



# insta
# insta=insta.drop(insta.index[[9,11]])
# insta.to_markdown(r"C:\Users\USER\Desktop\insta.txt",index=False)




# fb = fb.reset_index(drop=True)




# fb=fb.drop(fb.index[[0,6,7,8,9,10,11,12]])




# fb = fb.rename(columns={'INSTAGRAM': 'FaceBook'})
# fb.to_markdown(r"C:\Users\USER\Desktop\fb.txt",index=False)



# wiki = wiki.reset_index(drop=True)
# wiki=wiki.drop(wiki.index[[0,7,8,9,10]])
# wiki = wiki.rename(columns={'INSTAGRAM': 'Wikipedia'})
# wiki.to_markdown(r"C:\Users\USER\Desktop\wiki.txt",index=False)



# twt = twt.reset_index(drop=True)
# # twt=twt.drop(wiki.index[[0,14,15,16]])
# twt = twt.rename(columns={'INSTAGRAM': 'Twitter'})
# twt.to_markdown(r"C:\Users\USER\Desktop\twt.txt",index=False)


# yt = yt.reset_index(drop=True)
# # twt=twt.drop(wiki.index[[0,14,15,16]])
# yt = yt.rename(columns={'INSTAGRAM': 'YouTube'})
# yt.to_markdown(r"C:\Users\USER\Desktop\yt.txt",index=False)





# gs= gs.reset_index(drop=True)
# # twt=twt.drop(wiki.index[[0,14,15,16]])
# gs = gs.rename(columns={'INSTAGRAM': 'General News scraper'})
# gs.to_markdown(r"C:\Users\USER\Desktop\gs.txt",index=False)






