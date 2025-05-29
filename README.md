# MSCS-532 Assignment 3: Understanding Algorithm Efficiency and Scalability
### Oishani Ganguly

This repository contains Python implementations, empirical benchmarks, and an in-depth report for two core data structures and algorithms topics:

- **Randomized and Deterministic Quicksort (with benchmarking)**
- **Hash Table using Chaining (with universal hashing)**

All code, benchmarks, and the final report are included for reproducibility and clarity.

---

## Repository Structure

MSCS532_ASSIGNMENT3/
- `deterministic_quicksort.py`: Deterministic (first-pivot) quicksort implementation
- `randomized_quicksort.py`: Randomized quicksort implementation
- `quicksort_benchmark.py`: Script to benchmark both quicksort variants
- `quicksort_benchmark_results.txt`: Benchmark output (timings/results table)
- `hash_table_chaining.py`: Hash table (with chaining) implementation
- `MSCS-532_ Assignment 3_ Understanding Algorithm Efficiency and Scalability.pdf` # Final report
- `README.md`: This file

---

## Instructions: Running the Code

#### Setup
1. **Python Version**  
   Ensure you have Python 3.7 or higher installed. You can check your version with:
   ```bash
   python3 --version
   ```
2. **Dependencies**
All scripts use only Python standard library modules. No external installations are required.
3. **Clone the Repository**
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Oishani/MSCS532_Assignment3.git
   cd MSCS532_Assignment3
   ```

### 1. Quicksort Implementations & Benchmarking

Run the benchmarking script to compare Randomized and Deterministic Quicksort:
```bash
python3 quicksort_benchmark.py
```
Output will display the average runtime of each algorithm on various input sizes and distributions (random, sorted, reverse-sorted, and repeated elements).
Detailed benchmark results are also saved in `quicksort_benchmark_results.txt`.

You can also test the individual quicksort implementations directly:
```bash
python3 randomized_quicksort.py
python3 deterministic_quicksort.py
```

### 2. Hash Table with Chaining

Run the hash table implementation for demonstration and testing:
```bash
python3 hash_table_chaining.py
```
This script demonstrates insertion, searching, deletion, and chaining, with results printed to the console.

## Summary of Findings

### Part 1: Randomized Quicksort vs Deterministic Quicksort

- **Randomized Quicksort** selects a random pivot for each partition, making it robust against worst-case input and consistently achieving O(n log n) expected time, even for sorted or repeated data.
- **Deterministic Quicksort** (using the first element as pivot) performs similarly on random and repeated arrays but suffers dramatic slowdowns on already sorted or reverse-sorted arrays, quickly exceeding Python’s recursion limit for larger input sizes.
- **Empirical benchmarks** confirm the theory: randomized quicksort is efficient and stable across all tested distributions, while deterministic quicksort is only competitive when the input is random or has many repeated values.

### Part 2: Hash Table with Chaining

- The implemented hash table uses chaining to handle collisions, a universal hash function for even distribution, and supports efficient insert, search, and delete operations.
- Average-case operation times are constant when the load factor (α = n/m) is kept low. As the load factor increases, search and delete times grow linearly.
- Best practices for performance: dynamic resizing of the table when the load factor exceeds a threshold, use of a strong hash function, setting the table size to a prime number, and employing chaining for collision resolution.
- Testing confirms that all operations remain efficient, and the structure is robust against a variety of edge cases and key types.

### Report
The full analysis, experimental results (including tables and explanations), and theoretical discussion can be found in `MSCS-532_ Assignment 3_ Understanding Algorithm Efficiency and Scalability.pdf`
