import numpy as np
aqi = np.array([int(input()), int(input()), int(input())])
print(np.mean(aqi))
print(np.max(aqi))
print(np.min(aqi))
print(np.sum(aqi))
filtered = aqi[aqi > 50]
print(filtered)