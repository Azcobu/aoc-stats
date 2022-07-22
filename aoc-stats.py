# lowest 2-star completion %
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import statistics

def load_data(fname):
    with open(fname, 'rb') as infile:
        return pickle.loads(infile.read())

def longest_times(times):
    longest = {}

    for year, data in times.items():
        for day, stars in data.items():
            longest[(year, day)] = stars['2'][100]
    longprobs = sorted(longest.items(), key=lambda x:x[1], reverse=True)



    print('| Year.Day | Completion Time (secs) |\n| --------- | ------------ |')
    for line in longprobs[:5]:
        aoc_url = f'https://adventofcode.com/{line[0][0]}/day/{line[0][1]}'
        print(f'| [{line[0][0]}.{line[0][1]}]({aoc_url}) | {line[1]} |')

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
    fig.savefig(f'images/aoc-sum-year.png')

def stripplot(times, year, mode='show'):
    df = pd.read_csv(r'd:\tmp\aoc-results.txt')
    df = df[df['year'] == year]
    plt.style.use("seaborn")

    k = sns.lmplot(x="day", y="time", hue='stars', data=df, order=5, line_kws={'linewidth':2},
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
    plt.ylabel('Solution Time (seconds)')

    plt.tight_layout()
    if mode == 'show':
        plt.show()
    fig = stripplot.get_figure()
    fig.savefig(f'images/aoc-{year}.png')

def showall(times):
    new = []
    curryear = date.today().year

    for year in range(2015, curryear):
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
    for y in range(2015, date.today().year):
        print(f'Rendering graph for {y}.')
        stripplot(times, y, 0)

def completion_table(comp):
    new = {}
    for year, data in comp.items():
        for day, stars in data.items():
            if day != 25:
                new[f'{year}.{day}'] = round((1 - stars[1]/ (stars[0] + stars[1])) * 100, 2)

    compsort = sorted(new.items(), key=lambda x:x[1])
    print('| Year.Day | Completion % |\n| --------- | ------------ |')
    for line in compsort[:5]:
        y, _, d = line[0].partition('.')
        aoc_url = f'https://adventofcode.com/{y}/day/{d}'
        print(f'| [{line[0]}]({aoc_url}) | {line[1]}% |')

def day_diffs(comp):
    diffs = {}
    for year, data in comp.items():
        for day, stars in data.items():
            if day != 1:
                diff = 1 - (comp[year][day][0] / comp[year][day-1][0])
                diffs[f'{year}.{day}'] = diff
    
    print(f'Mean daily drop-off is {statistics.mean(diffs.values())*100:.3}%')
    print(f'Median daily drop-off is {statistics.median(diffs.values())*100:.3}%')

    print('| Year.Day | Daily Drop-Off (%) |\n| --------- | ------------ |')
    for line in sorted(diffs.items(), key=lambda x:x[1], reverse=1)[:5]:
        y, _, d = line[0].partition('.')
        aoc_url = f'https://adventofcode.com/{y}/day/{d}'
        print(f'| [{line[0]}]({aoc_url}) | {line[1]*100:.3}% |')

def completion_stats(comp):
    done1, done2 = 0, 0
    year_comps = {k:0 for k in range(2015, 2022)}
    for year, data in comp.items():
        for day, stars in data.items():
            done2 += stars[0]
            done1 += stars[1]
            year_comps[year] += stars[0]

    print(f'{done2} have done 2 stars problems, {done1} have done 1 star.')
    print(f'{done1/done2:.3}')
    print(year_comps)

def main():
    comp = load_data(r'd:\tmp\aoc-comp-dict.txt')
    times = load_data(r'd:\tmp\aoc-results-dict.txt')
    #print(times)
    #print(longest_times(times))
    #longest_years(times)
    #stripplot(times, 2015)
    #gen_yearly_charts(times)
    #showall(times)
    #completion_table(comp)
    day_diffs(comp)
    #completion_stats(comp)

if __name__ == '__main__':
    main()
