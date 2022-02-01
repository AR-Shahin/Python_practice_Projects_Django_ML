

from audioop import reverse


jobs = [
    [100, 2, "A", ]
    [19, 1, "B", ]
    [27, 2, "C", ]
    [15, 3, "E", ]
    [25, 1, "D", ]
]
jobs.sort(reverse=True)
print(jobs)
