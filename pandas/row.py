import pandas as pd
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar)
print(myvar.loc["day1"])
print(myvar.loc["day2"])