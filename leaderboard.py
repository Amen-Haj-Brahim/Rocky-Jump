import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("leaderboard.csv")
print(data["name"])
plt.title("leaderboard")
plt.xlabel("person")
plt.ylabel("score")
plt.bar(data["name"],data["record"])
plt.show()
