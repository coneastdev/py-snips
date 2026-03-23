# python linear search - MIT-0 - github.com/coneastdev/py-snips

# data sets
number_dataset = [5, 3, 1, 6, 8, 5, 4, 3, 2, 1, 0, 5, 3, 7, 6]
string_dataset = ["b", "l", "o", "k", "f", "r", "j"]
float_dataset = [9.99, 2.6, 7.02, 5.92, 0.01, 4.0, -1.2]

# algorithm
def linear_search(dataset: list, key: str) -> int | None:
    # go through every item and find key
    for index, variable in enumerate(dataset):
        if str(variable) == key:
            return index
        
    # none found
    return None

# launch with data sets
if __name__ == "__main__":
    print(linear_search(number_dataset, "6"))
    print(linear_search(string_dataset, "j"))
    print(linear_search(float_dataset, "9.99"))
    print(linear_search(float_dataset, "-31.03"))
