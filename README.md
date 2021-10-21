# algorithmic-complexity
Repository for writing algorithims and working on time complexity.

## How to use
This repository requires Python3 to run correctly. To install dependencies (numpy for numerical operations)
```
pip install -r requirements.txt
```

To run tests in the repo:
```
pytest
```

## Results
### Shuffle sort:
- The requirement: An algorithm that takes the elements of an array and randomly orders them
- Python's shuffle sort (from Python's random module) has a runtime of O(n), as can be seen from the following graph:

![built in shuffle](./shuffle/builtin_time_results.png)