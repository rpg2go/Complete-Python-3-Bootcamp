
### Review the following Python function. What does it do? How would you improve its efficiency?

def process_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num * num)
    return result

numbers = list(range(1, 1000000))
squared_evens = process_numbers(numbers)

## Using List Comprehension in Python

def process_numbers(numbers):
    return [num * num for num in numbers if num % 2 == 0]

# Notes: List comprehension is a concise way to create lists in Python. It allows you to generate a new list by applying an expression to each element in an iterable, typically replacing for loops for more readable and efficient code.
#   new_list = [expression for item in iterable if condition]

squares = []
for num in range(1, 6):
    squares.append(num ** 2)
print(squares)  # Output: [1, 4, 9, 16, 25]

squares = [num ** 2 for num in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]


### Filtering List of Dictionaries

data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 22}
]

# Filter people older than 25
filtered_data = [person for person in data if person["age"] > 25]
print(filtered_data)  # [{'name': 'Bob', 'age': 30}]


def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 3, 1, 2, 4]))  # [1, 2, 3, 4]




#### 1. Using Pandas for Efficient Data Handling

### Reading a Large CSV in Chunks
import pandas as pd  

chunk_size = 100_000  # Process 100K rows at a time
for chunk in pd.read_csv("large_dataset.csv", chunksize=chunk_size):
    # Perform operations on each chunk
    chunk["new_column"] = chunk["existing_column"] * 2  
    chunk.to_csv("processed_data.csv", mode="a", header=False, index=False)

#### 2. Using Generators Instead of Storing Large Lists in Memory

### Processing a Large Log File Line by Line
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # Yield one line at a time

# Processing the file without loading it entirely into memory
for line in read_large_file("large_log.txt"):
    process(line)  # Replace with actual processing logic


#### 3. Leveraging Multiprocessing for CPU-Intensive Tasks

### Parallel Processing of a Large Dataset
from multiprocessing import Pool  
import numpy as np  

# Function to process a chunk
def process_chunk(data_chunk):
    return [x**2 for x in data_chunk]  # Example: Squaring each number  

data = np.arange(1_000_000)  # Large dataset  

# Split data into chunks for parallel processing
num_workers = 4  
chunks = np.array_split(data, num_workers)  

# Use multiprocessing Pool to process in parallel
with Pool(num_workers) as pool:
    results = pool.map(process_chunk, chunks)  

# Combine results
flattened_results = [item for sublist in results for item in sublist]


#### 4. Using Async I/O for Network-Bound Tasks
import asyncio  
import aiohttp  

async def fetch_data(session, url):  
    async with session.get(url) as response:  
        return await response.json()  

async def main():  
    urls = ["https://api.example.com/data1", "https://api.example.com/data2"]  

    async with aiohttp.ClientSession() as session:  
        tasks = [fetch_data(session, url) for url in urls]  
        results = await asyncio.gather(*tasks)  

    print(results)  

asyncio.run(main())  

