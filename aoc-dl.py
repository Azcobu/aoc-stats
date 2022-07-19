import re
import requests
import pickle
import time

def save_csv(instr, filename):
    with open(f'd:\\tmp\\{filename}', 'w') as outfile:
        outfile.write(instr)
                    
def gen_times_csv(indata):
    outstr = ['year,day,stars,position,time\n']
    for year in range(2015, 2022):
        for day in range(1, 26):
            for stars in ['2', '1']:
                for pos in range(1, 101):
                    if year in indata and day in indata[year]:
                        timestr = indata[year][day][stars][pos]
                        outstr.append(f'{year},{day},{stars},{pos},{timestr}\n')
    return ''.join(outstr)  

def gen_completion_csv(indata):
    outstr = ['year,day,both,one\n']
    for year, data in indata.items():
        for day, completed in data.items():
            outstr.append(f'{year},{day},{completed[0]},{completed[1]}\n')
    return ''.join(outstr)

def save_pickle(indata, filename):
    with open(f'd:\\tmp\\{filename}', 'wb') as outfile:
        pickle.dump(indata, outfile)

def load_pickle():
    with open(r'd:\tmp\aoc-results-dict.txt', 'rb') as infile:
        return pickle.loads(infile.read())

def dl_page(url):
    try:
        print(f'Retrieving {url}...')
        r = requests.get(url, allow_redirects=True)
        time.sleep(2)
    except Exception as err:
        print(err)
    return r.text

def get_leaderboard_times():
    results = {}

    for year in range(2015, 2022):
        results[year] = {}
        for day in range(1, 26):
            results[year][day] = {'2':{}, '1':{}}
            url = f'http://adventofcode.com/{year}/leaderboard/day/{day}'
            page = dl_page(url)
            times = re.findall(re.compile('>Dec \d\d  \d\d:\d\d:\d\d<'), page)

            for pos in range(200):
                starstr = '2' if 0 <= pos <= 99 else '1'
                t = times[pos]
                h, m, s = int(t[9:11]), int(t[12:14]), int(t[15:17])
                secs = h * 3600 + m * 60 + s
                posstr = pos - 99 if starstr == '1' else pos + 1
                results[year][day][starstr][posstr] = secs
    return results

def get_completion_stats():
    completion = {}

    for year in range(2015, 2022):
        completion[year] = {k:[] for k in range(1, 26)}

        url = f'https://adventofcode.com/{year}/stats'
        page = dl_page(url)
        #print(page)
        nums = [int(x[:-7]) for x in re.findall(r'\d+</span>', page)]
        day = 25
        for both, one in zip(nums[::2], nums[1::2]):
            completion[year][day] = [both, one]
            day -= 1
    return completion

def main():
    #res = get_leaderboard_times()
    #save_pickle(res, 'aoc-times-dict.txt')
    #res = load_pickle()
    #output = gen_times_csv(res)
    #save_csv(output, 'aoc-times.txt')
    comp = get_completion_stats()
    save_pickle(comp, 'aoc-comp-dict.txt')
    compstr = gen_completion_csv(comp)
    save_csv(compstr, 'aoc-comp.txt')
    
if __name__ == '__main__':
    main()
