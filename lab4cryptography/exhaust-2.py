# WARNING: Running this script can make your system unresponsive or crash.
# Use it with caution and preferably on a system where you can afford a crash.

def exhaust_memory():
    try:
        # Create a list to hold large lists
        memory_hog = []
        while True:
            # Allocate a large list with a million elements
            memory_hog.append([0] * 1000000)
    except MemoryError:
        print("Memory exhausted!")

if __name__ == "__main__":
    exhaust_memory()