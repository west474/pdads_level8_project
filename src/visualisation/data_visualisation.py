import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn bar chart.
# shows the average albedo for each spectral type.
def barchart(df):
    # average the values for sorting.
    df_avg = df.groupby('spec_T')['albedo'].mean().sort_values()
    df_sorted = df_avg.index.tolist()

    sns.barplot(
        x='albedo',
        y='spec_T',
        hue='spec_T',
        data=df.sort_values(by='spec_T'),
        order=df_sorted,
        palette='viridis',
        errorbar=None,
    )
    plt.title('Average Albedo by Spectral Type')
    plt.xlabel('Average Albedo')
    plt.ylabel('Spectral Type (spec_T)')
    plt.tight_layout()
    plt.show()

# seaborn violin plot.
# shows the distribution of albedo values for each spectral type.
def violinplot(df):
    sns.violinplot(
        x='spec_T',
        y='albedo',
        data=df,
    )
    plt.title('Albedo Distribution by Spectral Type')
    plt.xlabel('Spectral Type (spec_T)')
    plt.ylabel('Albedo')
    plt.show()

# matplotlib scatter plot.
# shows the relationship between diameter, albedo, and spectral type.
def scatterplot(df):
    plt.figure(figsize=(14, 6))
    plt.scatter(
        x=df['diameter'] * 1000,
        y=df['spec_T'],
        s=df['albedo'] * 3000,
        alpha=0.2,
    )
    plt.title('Diameter vs Spectral Type with Albedo as Size')
    plt.xlabel('Diameter (m) - Log Scale')
    plt.ylabel('Spectral Type (spec_T)')
    plt.grid(True)
    plt.xscale('log')
    plt.show()

# matplotlib piechart.
# shows the distribution of spectral types in the dataset.
def piechart(df):
    spec_count = df['spec_T'].value_counts()
    
    plt.figure(figsize=(10,10))
    plt.pie(
        spec_count,
        startangle=90,
        labels=['Carbonaceous (C)', 'Silicate (S)', 'Metallic (M)'],
        autopct='%.0f%%',
        pctdistance=0.70,
    )
    donut_hole = plt.Circle((0, 0), 0.30, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(donut_hole)
    plt.title('Distribution of Spectral Types')
    plt.show()




