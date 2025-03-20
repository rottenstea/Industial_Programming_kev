import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load CSV file
file_path = "Vienna_population_trend.csv"  # Change this to your actual file path
df = pd.read_csv(file_path, delimiter="\t")

# Set Seaborn style
sns.set_theme(style="darkgrid")

# Create the line plot
plt.figure(figsize=(8, 6))
sns.lineplot(x=df["year"], y=df["male"], label="Male Population", color="blue")
sns.lineplot(x=df["year"], y=df["female"], label="Female Population", color="red")
sns.lineplot(x=df["year"], y=df["population"], label="Total Population", color="black", linestyle="dashed")

# Add titles and labels
plt.title("Population Evolution of Vienna")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()

# Show the plot
plt.show()

