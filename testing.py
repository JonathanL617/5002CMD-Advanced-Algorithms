import time
from HashTable import HashTable
from Product import BabyProduct


def create_large_dataset(num_products=1000):
    """Create a large dataset of products for testing"""
    products = []
    categories = ["clothing", "toys", "feeding", "diapering", "bathing",
                  "nursery", "safety", "health", "travel", "books"]

    print(f"Generating {num_products} products...")
    for i in range(num_products):
        cat = categories[i % len(categories)]
        product = BabyProduct(
            f"P{i:05d}",
            f"Product {i}",
            cat.capitalize(),
            10.99 + (i % 100),
            50 + (i % 50)
        )
        products.append((cat, product))

    return products


def setup_hash_table(products):
    """Insert products into hash table"""
    print("Inserting into Hash Table...")
    ht = HashTable(50)  # Larger capacity for better distribution

    start = time.time()
    for category, product in products:
        ht.insert(category, product)
    end = time.time()

    insert_time = (end - start) * 1000
    print(f"Hash Table insertion time: {insert_time:.4f} ms")
    return ht


def setup_array(products):
    """Insert products into one-dimensional array"""
    print("Inserting into Array...")
    array = []

    start = time.time()
    for category, product in products:
        array.append((category, product))
    end = time.time()

    insert_time = (end - start) * 1000
    print(f"Array insertion time: {insert_time:.4f} ms")
    return array


def search_hash_table(ht, category, product_id):
    """Search in hash table by category and product ID"""
    products = ht.search(category)
    if products:
        for p in products:
            if p.get_product_id() == product_id:
                return p
    return None


def search_array(array, category, product_id):
    """Search in array using linear search (O(n))"""
    for cat, product in array:
        if cat.lower() == category.lower() and product.get_product_id() == product_id:
            return product
    return None


def benchmark_searches(search_func, data, searches, label):
    """Run multiple searches and measure average time"""
    print(f"\n{label}")
    print("-" * 70)

    total_time = 0
    found_count = 0

    for category, product_id in searches:
        start = time.time()
        result = search_func(data, category, product_id)
        end = time.time()

        elapsed = (end - start) * 1000
        total_time += elapsed

        if result:
            found_count += 1

    avg_time = total_time / len(searches)
    print(f"  Total searches: {len(searches)}")
    print(f"  Found: {found_count}")
    print(f"  Total time: {total_time:.6f} ms")
    print(f"  Average time per search: {avg_time:.6f} ms")

    return total_time, avg_time


def main():
    print("=" * 70)
    print("PERFORMANCE COMPARISON: HASH TABLE vs ONE-DIMENSIONAL ARRAY")
    print("=" * 70)

    # Create large dataset
    print("\n[Step 1] Creating large dataset...")
    NUM_PRODUCTS = 10000000  # Change this number to test with different sizes
    products = create_large_dataset(NUM_PRODUCTS)
    print(f"Created {len(products)} products\n")

    # Setup Hash Table
    print("[Step 2] Setting up Hash Table...")
    hash_table = setup_hash_table(products)
    print()

    # Setup Array
    print("[Step 3] Setting up One-Dimensional Array...")
    array = setup_array(products)
    print()

    # Create search queries (search for items at different positions)
    print("[Step 4] Preparing search queries...")
    search_queries = []
    categories = ["clothing", "toys", "feeding", "diapering", "bathing",
                  "nursery", "safety", "health", "travel", "books"]

    # Search for items at beginning, middle, and end
    for i in [0, 100, 500, 1000, 2000, 3000, 4000, 4500, 4900, 4999]:
        if i < NUM_PRODUCTS:
            cat = categories[i % len(categories)]
            product_id = f"P{i:05d}"
            search_queries.append((cat, product_id))

    print(f"Created {len(search_queries)} search queries")

    # Benchmark Hash Table
    print("\n" + "=" * 70)
    print("[Step 5] BENCHMARKING...")
    print("=" * 70)

    ht_total, ht_avg = benchmark_searches(
        search_hash_table,
        hash_table,
        search_queries,
        "HASH TABLE SEARCH (O(1) average)"
    )

    # Benchmark Array
    arr_total, arr_avg = benchmark_searches(
        search_array,
        array,
        search_queries,
        "ARRAY LINEAR SEARCH (O(n))"
    )

    # Display Results
    print("\n" + "=" * 70)
    print("FINAL RESULTS")
    print("=" * 70)
    print(f"Dataset Size:              {NUM_PRODUCTS} products")
    print(f"Number of Searches:        {len(search_queries)}")
    print("-" * 70)
    print(f"Hash Table Total Time:     {ht_total:.6f} ms")
    print(f"Array Total Time:          {arr_total:.6f} ms")
    print("-" * 70)
    print(f"Hash Table Avg/Search:     {ht_avg:.6f} ms")
    print(f"Array Avg/Search:          {arr_avg:.6f} ms")
    print("-" * 70)
    print(f"Time Difference:           {arr_total - ht_total:.6f} ms")
    print(f"Hash Table is FASTER by:   {arr_total / ht_total if ht_total > 0 else 0:.2f}x")
    print("=" * 70)

    # Visual Comparison
    print("\n" + "=" * 70)
    print("VISUAL COMPARISON")
    print("=" * 70)

    ht_bar = "█" * int(ht_avg * 10)
    arr_bar = "█" * int(arr_avg * 10)

    print(f"Hash Table: {ht_bar} {ht_avg:.4f} ms")
    print(f"Array:      {arr_bar} {arr_avg:.4f} ms")


if __name__ == '__main__':
    main()