# lowest 2-star completion %
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(fname):
    with open(fname, 'rb') as infile:
        return pickle.loads(infile.read())

def longest_times(times):
    longest = {}

    for year, data in times.items():
        for day, stars in data.items():
            longest[(year, day)] = stars['2'][100]
    return sorted(longest.items(), key=lambda x:x[1], reverse=True)[:10]

def longest_years(times):
    yeartime = {}
    new = []

    for year, data in times.items():
        yeartime[year] = 0
        for day, stars in data.items():
            yeartime[year] += stars['2'][100]
    
    for year, total in sorted(yeartime.items(), key=lambda x:x[1], reverse=True):
        new.append({'year':year, 'total':total})

    df = pd.DataFrame.from_dict(new)
    bp = sns.barplot(x='year', y='total', data=df)
    plt.title(f'Advent of Code Summed Solution Times By Year')
    plt.xlabel('Year')
    plt.ylabel('Summed Solution Time (seconds)')
    #plt.show()
    fig = bp.get_figure()
    fig.savefig(f'AoC Sum By Year.png')

def stripplot(times, year):
    df = pd.read_csv(r'd:\tmp\aoc-results.txt')
    df = df[df['year'] == year]
    plt.style.use("seaborn")

    k = sns.lmplot(x="day", y="time", hue='stars', data=df, order=2, line_kws={'linewidth':2},
                  scatter=False, legend=False, height=7, aspect=8/5)
    stripplot = sns.stripplot(x="day", y="time", hue='stars', dodge=True, data=df) # marker="*", size=8

    handles, labels = stripplot.get_legend_handles_labels()
    l = plt.legend(handles[0:2], ['One Star', 'Two Stars'])

    #stripplot.get_legend().remove()
    #sns.catplot(x='day', y='time', hue='stars', data=df, kind="violin", linewidth=0.5)
    #sns.barplot(x="day", y="time", hue='stars', data=df, ci = 0, linewidth=3)
    #sns.boxplot(x="day", y="time", hue='stars', data=df)

    plt.ylim(bottom=0)
    plt.title(f'Advent of Code {year} Top 100 Leaderboard Times')
    plt.xlabel('Day')
    plt.ylabel('Solution Time (Seconds)')

    plt.tight_layout()
    #plt.show()
    fig = stripplot.get_figure()
    fig.savefig(f'aoc-{year}.png')

def showall(times):
    new = []
    for year in range(2015, 2022):
        for day in range(1, 26):
            new.append({'year':f'{year}.{day}', 'time':times[year][day]['2'][100]})

    df = pd.DataFrame.from_dict(new)
    #plt.figure(figsize=(4, 20))
    fig = plt.gcf()

    # Change seaborn plot size
    #fig.set_size_inches(6, 18)
    #sns.set(font_scale=0.25)
    #bar = sns.barplot(x='time', y='year', orient='h', data=df, ci=0)

    #ax = df.plot(x='year', y='time', kind='barh', edgecolor='black', linewidth=0, figsize=(6, 30))

    plt.tight_layout()
    plt.savefig(f'aoc-all.jpg', dpi=100)

    plt.show()
    #fig = bar.get_figure()
    #fig.savefig(f'AoC All.jpg', dpi=300)

def gen_yearly_charts(times):
    for y in range(2015, 2022):
        print(f'Rendering graph for {y}.')
        stripplot(times, y)

def main():
    complete = load_data(r'd:\tmp\aoc-comp-dict.txt')
    times = load_data(r'd:\tmp\aoc-results-dict.txt')
    #print(times)
    #print(longest_times(times))
    #longest_years(times)
    #stripplot(times, 2015)
    gen_yearly_charts(times)
    #showall(times)

if __name__ == '__main__':
    main()
