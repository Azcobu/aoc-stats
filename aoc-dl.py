import re
import requests
import pickle
import time

def save_csv(instr):
    with open(r'd:\tmp\aoc-results.txt', 'w') as outfile:
        outfile.write(instr)
                    
def gen_csv(indata):
    outstr = ['year,day,stars,position,time\n']
    for year in range(2015, 2022):
        for day in range(1, 26):
            for stars in ['2', '1']:
                for pos in range(1, 101):
                    if year in indata and day in indata[year]:
                        timestr = indata[year][day][stars][pos]
                        outstr.append(f'{year},{day},{stars},{pos},{timestr}\n')
    return ''.join(outstr)  

def save_pickle(indata):
    with open(r'd:\tmp\aoc-results-dict.txt', 'wb') as outfile:
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

def parse_pages():
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

def main():
    res = parse_pages()
    save_pickle(res)
    #res = load_pickle()
    output = gen_csv(res)
    save_csv(output)
    
if __name__ == '__main__':
    main()
