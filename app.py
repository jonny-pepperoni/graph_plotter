import pandas as pd
from matplotlib import pyplot as plt

# Importing dataset
df = pd.read_csv(r"D:\Projects\graph_plotter\x-axis.csv",
                 skiprows=1, header=None, sep=";", decimal=",")
# Dropping the missing rows.
df_dropped = df.dropna(subset=[1])


def plot_CSV_with_header(args):
    x_axis = args[0]
    y_axis = args[1]
    # fig = plt.figure()
    plt.plot(x_axis, y_axis)
    plt.show()


if __name__ == "__main__":
    plot_CSV_with_header(df_dropped)
