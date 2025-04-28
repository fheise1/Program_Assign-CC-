# Programming Assignment: Dijkstra's Algorithm

## Execution Instructions

### Requirements
- Python 3.x
- Spark

### How to Run
1. Download and place these files in the same directory:
   - `dijkstra.py`
   - `weighted_graph.txt`

2. While in the directory, run the program with:
   ```bash
   python dijkstra.py weighted_graph.txt [START_NODE]
   (for example: python dijkstra.py weighted_graph.txt 0)

3. Results
    - The program will print shortest distances from the starting node to all other nodes in the format:
        Shortest distances from node [START_NODE]:
        Node 0: 0
        Node 1: 5.0
        Node 2: INF
        ...

4. Saving the results
    - python dijkstra.py weighted_graph.txt 0 > results.txt