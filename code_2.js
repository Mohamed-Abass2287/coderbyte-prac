// find intersection of two lists of numbers
function FindIntersection(strArr) {
    // Convert input strings into arrays of numbers
    const list1 = new Set(strArr[0].split(", ").map(Number));
    const list2 = new Set(strArr[1].split(", ").map(Number));

    // Find the intersection and sort it
    const intersection = [...list1].filter(num => list2.has(num)).sort((a, b) => a - b);

    return intersection.length > 0 ? intersection.join(",") : "false";
}

// Example usage:
console.log(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]));
// Expected Output: "1,4,13"

// codeland username