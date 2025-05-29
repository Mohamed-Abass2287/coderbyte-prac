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

#  find intersection of two lists of numbers
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

# codelandUsernameValidations
def codelandUsernameValidations(username):
    # Check if the username is between 4 and 25 characters
    if len(username) < 4 or len(username) > 25:
        return "false"
    
    # Check if the first character is a letter
    if not username[0].isalpha():
        return "false"
    
    # Check for invalid characters
    for char in username:
        if not (char.isalnum() or char == '_'):
            return "false"
    
    # Check for consecutive underscores
    if '__' in username:
        return "false"
    
    # Check that username does not end with an underscore
    if username[-1] == '_':
        return "false"
    
    return "true"
# mifano majaribio:
print(codelandUsernameValidations("username"))
print(codelandUsernameValidations("123"))

# BasicRomanNumerals
def BasicRomanNumerals(strParam):
    "_define-ocg_"
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    varFiltersCg = list(strParam)
    total = 0
    varOcg = 0

    for i in range(len(varFiltersCg) - 1, -1, -1):
        current_value = roman_values[varFiltersCg[i]]
        if current_value < varOcg:
            total -= current_value
        else:
            total += current_value
            varOcg = current_value
    return total

print(BasicRomanNumerals(input()))
