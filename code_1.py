def FindIntersection(strArr):
    # Convert the input strings to sets of integers
    list1 = set(map(int, strArr[0].split(", ")))
    list2 = set(map(int, strArr[1].split(", ")))

    # Find the intersection and return sorted result
    intersection = sorted(list1 & list2)

    return ",".join(map(str, intersection)) if intersection else "false"

# Example usage:
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
# Output: "1,4,13"


def FindIntersection(strArr):
    # Convert input strings into sets of integers
    list1 = set(map(int, strArr[0].split(", ")))
    list2 = set(map(int, strArr[1].split(", ")))

    # Find the intersection and return sorted result
    intersection = sorted(list1 & list2)

    return ",".join(map(str, intersection)) if intersection else "false"

# Example usage:
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
# Expected Output: "1,4,13"
