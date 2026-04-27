import pandas as pd
data = {
    "city": [input(), input(), input()],
    "aqi": [int(input()), int(input()), int(input())]
}
df = pd.DataFrame(data)
print(df)
print(df["aqi"].mean())
print(df.groupby("city").mean())
print(df[df["aqi"] > 50])