# MSCS532 Assignment 3: Understanding Algorithm Efficiency and Scalability

## Overview

This repository contains the implementation and analysis for Assignment 3 in MSCS532: Algorithms and Data Structures.

The assignment explores the efficiency and scalability of two important algorithmic techniques:

1. **Randomized Quicksort**
2. **Hashing with Chaining**

The project includes implementations, empirical performance testing, and analysis of the theoretical time complexity of both approaches.

---

## Project Structure

```text
MSCS532_Assignment3/
│
├── randomized_quicksort.py
├── deterministic_quicksort.py
├── benchmark.py
├── hash_table.py
├── README.md
└── .gitignore
```

### `randomized_quicksort.py`

Implements Randomized Quicksort. A pivot index is selected randomly from the current subarray and moved to the end before partitioning.

The implementation handles:

- Random input
- Already sorted input
- Reverse-sorted input
- Repeated elements
- Empty arrays

### `deterministic_quicksort.py`

Implements deterministic Quicksort using the **first element of each subarray as the pivot**.

This implementation is used as the baseline for comparison with Randomized Quicksort.

### `benchmark.py`

Empirically compares Randomized Quicksort and deterministic first-pivot Quicksort.

The benchmark tests arrays of sizes:

- 100
- 500
- 1000

For each size, four input distributions are tested:

- Random arrays
- Already sorted arrays
- Reverse-sorted arrays
- Arrays containing repeated elements

Execution time is measured using Python's `time.perf_counter()`.

### `hash_table.py`

Implements a hash table using **separate chaining** for collision resolution.

The implementation includes:

- Insert
- Search
- Delete
- Universal-style hash function
- Collision handling through chaining
- Load-factor tracking
- Dynamic resizing

Each index of the hash table contains a bucket. Multiple key-value pairs can be stored in the same bucket when a collision occurs.

---

## Requirements

- Python 3
- No external packages are required

The project uses only modules from the Python standard library.

---

## How to Run

Clone the repository and enter the project directory:

```bash
git clone https://github.com/aliza57606/MSCS532_Assignment3.git
cd MSCS532_Assignment3
```

### Run Randomized Quicksort

```bash
python randomized_quicksort.py
```

### Run Deterministic Quicksort

```bash
python deterministic_quicksort.py
```

### Run the Performance Benchmark

```bash
python benchmark.py
```

### Run the Hash Table Demonstration

```bash
python hash_table.py
```

---

## Randomized Quicksort Analysis

Randomized Quicksort randomly selects a pivot from the current subarray. This prevents the algorithm from consistently selecting a poor pivot simply because of the original ordering of the input.

The expected running time of Randomized Quicksort is:

```text
O(n log n)
```

Partitioning requires linear work across a level of the recursion, while randomized pivot selection produces an expected logarithmic recursion structure.

The worst-case running time remains:

```text
O(n²)
```

This can occur when extremely unbalanced partitions are repeatedly produced. Randomization does not eliminate the theoretical worst case, but it makes the behavior independent of a fixed input ordering.

---

## Empirical Quicksort Results

The following execution times were observed during testing.

| Array Size | Input Type | Randomized Quicksort | Deterministic Quicksort |
|---:|---|---:|---:|
| 100 | Random | 0.000200 s | 0.000134 s |
| 100 | Sorted | 0.000178 s | 0.000361 s |
| 100 | Reverse Sorted | 0.000170 s | 0.000605 s |
| 100 | Repeated Elements | 0.000252 s | 0.000182 s |
| 500 | Random | 0.001073 s | 0.000795 s |
| 500 | Sorted | 0.001060 s | 0.009253 s |
| 500 | Reverse Sorted | 0.001165 s | 0.015729 s |
| 500 | Repeated Elements | 0.002920 s | 0.002837 s |
| 1000 | Random | 0.002427 s | 0.001848 s |
| 1000 | Sorted | 0.002198 s | 0.034176 s |
| 1000 | Reverse Sorted | 0.002462 s | 0.063270 s |
| 1000 | Repeated Elements | 0.009811 s | 0.009128 s |

### Summary of Quicksort Findings

The deterministic implementation was slightly faster on random arrays in these tests. Randomized pivot selection introduces some additional overhead, so randomization does not necessarily make every individual execution faster.

A much larger difference appeared for **sorted and reverse-sorted arrays**. Because deterministic Quicksort always selects the first element as its pivot, these inputs repeatedly produce highly unbalanced partitions. Its performance therefore moves toward the `O(n²)` worst case.

Randomized Quicksort avoids systematically choosing the first or last ranked element simply because the input is ordered. Consequently, its performance remained much more stable on the sorted and reverse-sorted test cases.

Both implementations became slower on arrays containing many repeated elements. The implementations use two-way partitioning, so large numbers of equal values can still result in unbalanced partitions.

---

## Hashing with Chaining

The hash table uses a universal-style hash function of the form:

```text
h(k) = ((a × k + b) mod p) mod m
```

where:

- `k` is the key
- `p` is a large prime number
- `a` and `b` are randomly selected parameters
- `m` is the number of buckets

Different keys may still map to the same bucket. These collisions are handled using **chaining**, where multiple key-value pairs are stored within the bucket.

---

## Hash Table Complexity

Let the load factor be:

```text
α = n / m
```

where:

- `n` = number of stored key-value pairs
- `m` = number of buckets

Under simple uniform hashing, the expected time for search, insertion, and deletion in this implementation is approximately:

```text
O(1 + α)
```

When the load factor is maintained as a constant, these operations have expected `O(1)` performance.

---

## Dynamic Resizing

The implementation monitors the load factor of the hash table.

When:

```text
load factor > 0.75
```

the number of buckets is doubled.

All existing key-value pairs are then rehashed because changing the table size can change their bucket indexes.

For example, during testing the table began with three buckets and eventually expanded to twelve buckets while storing five items:

```text
Table size: 12
Number of items: 5
Load factor: 0.4166666666666667
```

Maintaining a relatively low load factor helps reduce long chains and keeps hash-table operations efficient.

---

## Collision Handling Example

Testing confirmed that different keys can map to the same bucket:

```text
Collision Test:
Bucket 0: []
Bucket 1: [(10, 'First'), (15, 'Second')]
Bucket 2: []
```

Keys `10` and `15` mapped to the same bucket in that test execution. Both entries remained available because the implementation stores colliding entries in the bucket using chaining.

Because the universal hash parameters are randomly generated when the program starts, exact bucket assignments can differ between executions.

---

## Conclusion

The experiments demonstrate how input characteristics and algorithm design affect performance.

Randomized Quicksort provides an expected running time of `O(n log n)` and avoids the systematic worst-case behavior that first-pivot deterministic Quicksort experiences on already sorted and reverse-sorted inputs.

Hashing with chaining provides efficient key-value operations when keys are distributed across buckets effectively. Monitoring the load factor and dynamically resizing the table helps limit collisions and maintain expected constant-time operations when the load factor remains bounded.