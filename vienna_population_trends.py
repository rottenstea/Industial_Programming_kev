import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")


# Load CSV file
file_path = "Vienna_population_trend.csv"  
df = pd.read_csv(file_path, delimiter="\t")

plt.figure(figsize=(8, 6))
sns.lineplot(x=df["year"], y=df["male"], label="Male Population", color="blue")
sns.lineplot(x=df["year"], y=df["female"], label="Female Population", color="red")
sns.lineplot(x=df["year"], y=df["population"], label="Total Population", color="black", linestyle="dashed")

plt.title("Future population evolution of Vienna")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()

plt.show()

