# CMPS 2200 Recitation 10## Answers

**Name:**__Raiya Dhalwala_______________________
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
The work of reachable is O(n+m) because it iterates through n and m

- **4)**
To see if a graph is connected, the worse case number of times we would need to call reachable would be the amount of n node times.

- **5)**
The work of connected is O(n+m) because the main part of the function calls on reachable, where the work is O(n+m)

- **7)**
If we switched the graph representation to an adjacency matrix, the work of reachable would change to O(n^2) because you have to iterate through all of the n nodes to check for edges. 