
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

