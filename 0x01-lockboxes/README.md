# Box Unlocking Problem

This repository contains a Python solution for the Box Unlocking Problem. The problem is defined as follows: given a set of boxes, where each box is identified by a unique ID and contains a list of IDs of other boxes that can unlock it, determine if it is possible to unlock all boxes.

## Code Structure

The code consists of two main functions: `createGraph` and `canUnlockAll`.

1. `createGraph(boxes)`: This function creates a graph representation of the given boxes. It takes a dictionary `boxes` as input, where the keys are box IDs (strings) and the values are lists of box IDs that can unlock the corresponding box. The function uses the `Graph` class from the `graphs` module to create the graph and add nodes and edges based on the input dictionary.

2. `canUnlockAll(boxes)`: This function determines if it is possible to unlock all boxes in the given configuration. It takes a list of lists `boxes` as input, where the index represents the box ID (string) and the values represent lists of box IDs that can unlock the corresponding box. The function calls the `createGraph` function to create a graph representation of the boxes, performs a depth-first search (DFS) on the graph to find the parent-child relationships between the boxes, and checks if there are any boxes with no parent (i.e., boxes that cannot be unlocked). It returns `True` if all boxes can be unlocked, and `False` otherwise.

## Usage

To use the code, you can call the `canUnlockAll` function with a list of lists representing the boxes and their unlocking relationships. For example:

```python
boxes = [
    ["2", "3"],
    ["4"],
    ["4"],
    []
]

result = canUnlockAll(boxes)
print(result)  # Output: True
```

In this example, the code will determine if it is possible to unlock all boxes in the given configuration, and the output will be `True` since all boxes can be unlocked.

## Installation

To run the code, you need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/.

Additionally, you need to install the `graphs` module, which is not a standard Python library. You can install it by running the following command in your terminal or command prompt:

```
pip install graphs
```

## Contributing

If you would like to contribute to this project, please feel free to fork the repository and submit a pull request. I would be happy to review and merge your changes.

## License

This code is licensed under the MIT License. See the `LICENSE` file for more information.