# python bubble sort - MIT-0 - github.com/coneastdev/py-snips

# data sets
number_dataset = [5, 3, 1, 6, 8, 5, 4, 3, 2, 1, 0, 5, 3, 7, 6]
string_dataset = ["b", "l", "o", "k", "f", "r", "j"]

# algorithm
def bubble_sort(dataset: list) -> list:
    # make comparison loop repeat for every item in list
    for _ in dataset:
        # compare every item in list
        for index, variable in enumerate(dataset):
            # if last item pass to avoid out of bounds error
            if index == len(dataset) - 1:
                pass
            else:
                # if var in front is smaller switch
                if variable > dataset[index + 1]:
                    dataset[index] = dataset[index + 1]
                    dataset[index + 1] = variable
                else:
                    pass
    return dataset

# launch with data sets
if __name__ == "__main__":
    print(bubble_sort(number_dataset))
    print(bubble_sort(string_dataset))