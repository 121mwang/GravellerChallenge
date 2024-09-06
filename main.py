import numpy as np

def rollGravellerIterations(iterations):
    maxParalysisCount = 0
    rollCount = 0
    while maxParalysisCount < 177 and rollCount < iterations:
        rolls = np.random.randint(1, 5, 231)
        paralysisCount = np.sum(rolls == 4)
        if paralysisCount > maxParalysisCount:
            maxParalysisCount = paralysisCount
        rollCount += 1
    return (maxParalysisCount, rollCount)

info = rollGravellerIterations(1000000000)
print(f"Max paralysis count: {info[0]}, rolls: {info[1]}")