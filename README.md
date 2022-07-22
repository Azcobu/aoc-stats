## Advent of Code Stats

Some simple exploration of Advent of Code problem completions. This isn't complete or exhaustive, just done out of curiosity really. Some findings:

* A total of 5,005,518 2-star solutions have been submitted as of writing, with another 505,596 1-star solutions.

* On average, 9.3% of people give up each day.

* The biggest single daily drop-off was for [2018 Day 15](https://adventofcode.com/2018/day/15), when solutions dropped by 42.2% compared to the previous day. 

#### What were the hardest problems?

One approach may be to look at 2-star completion percentages per problem, which also has the advantage of including all solutions, and not just the top 100 on the leaderboard. This needs to exclude Day 25 for each year though, as the second star there is conditional on finishing all the other problems for that year. Based on this, the problems with the lowest 2-star completion rates are:

| Year.Day | Completion % |
| --------- | ------------ |
| [2019.22](https://adventofcode.com/2019/day/22) | 61.99% |
| [2018.23](https://adventofcode.com/2018/day/23) | 64.79% |
| [2019.16](https://adventofcode.com/2019/day/16) | 70.32% |
| [2021.22](https://adventofcode.com/2021/day/22) | 72.25% |
| [2017.3](https://adventofcode.com/2017/day/3) | 74.28% |

Another approach might be to see how long the top 100 leaderboard took to fill for each problem:

| Year.Day | Completion Time (seconds) |
| --------- | ------------ |
| [2015.19](https://adventofcode.com/2015/day/19) | 13931 |
| [2015.1](https://adventofcode.com/2015/day/1) | 11176 |
| [2015.22](https://adventofcode.com/2015/day/22) | 10985 |
| [2016.11](https://adventofcode.com/2016/day/11) | 9855 |
| [2018.15](https://adventofcode.com/2018/day/15) | 8597 |

2015.1 is obviously the outlier here, as low population rather than difficulty caused the slow solution. The other two solutions from 2015 are also likely affected by this.

Finally, there's the percentage decline from the number of solutions submitted the previous day:

| Year.Day | Daily Drop-Off (%) |
| --------- | ------------ |
| [2018.15](https://adventofcode.com/2018/day/15) | 42.2% |
| [2016.11](https://adventofcode.com/2016/day/11) | 40.2% |
| [2017.3](https://adventofcode.com/2017/day/3) | 38.9% |
| [2019.18](https://adventofcode.com/2019/day/18) | 38.7% |
| [2019.3](https://adventofcode.com/2019/day/3) | 35.7% |

#### What were the hardest years?

A naive approach is simply summing the leaderboard completion times for all 25 days for each year, which results in the following:

![Summed times by year](images/aoc-sum-year.png?raw=true)

However, this metric is badly skewed by changing population - AoC was new in 2015, so not many people were attempting the puzzles for the first few days. Conversely, later solution times are driven down by the community learning what to expect in each year. AoC tends to reuse certain kinds of problems - each year there's usually a assembly language problem, a Game of Life problem, a maze traversal problem, and so on. So people know what might be coming and have libraries ready for those classes of problems, which drives down solution times.

#### Year visualizations

Some graphs of Advent of Code solution times by year, pulled from the leaderboard stats. 

<details>
<summary>2015</summary>

![2015](images/aoc-2015.png?raw=true)

</details>

<details>
<summary>2016</summary>

![2016](images/aoc-2016.png?raw=true)

</details>

<details>
<summary>2015</summary>

![2017](images/aoc-2017.png?raw=true)

</details>

<details>
<summary>2015</summary>

![2018](images/aoc-2018.png?raw=true)

</details>

<details>
<summary>2019</summary>

![2019](images/aoc-2019.png?raw=true)

</details>

<details>
<summary>2020</summary>

![2020](images/aoc-2020.png?raw=true)

</details>

<details>
<summary>2021</summary>

![2021](images/aoc-2021.png?raw=true)

</details>
