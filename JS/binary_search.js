/*
Title: binary search 
Author: carlostr
Date: 01/02/2024
*/

const list = [
    1,  2,  3,   4,  5,  6,  7,  8,  9, 10, 11, 12,
   13, 14, 15,  16, 17, 18, 19, 20, 21, 22, 23, 24,
   25, 26, 27,  28, 29, 30, 31, 32, 33, 34, 35, 36,
   37, 38, 39,  40, 41, 42, 43, 44, 45, 46, 47, 48,
   49, 50, 51,  52, 53, 54, 55, 56, 57, 58, 59, 60,
   61, 62, 63,  64, 65, 66, 67, 68, 69, 70, 71, 72,
   73, 74, 75,  76, 77, 78, 79, 80, 81, 82, 83, 84,
   85, 86, 87,  88, 89, 90, 91, 92, 93, 94, 95, 96,
   97, 98, 99, 100
 ]

function binarySearch(list,target){
    let first = 0;
    let last = list.length - 1;

    while (first <= last){
        let midpoint = Math.floor((first + last)/2);
        if (list[midpoint] == target) {
            return midpoint;
        } else if (list[midpoint] < target) {
            first = midpoint + 1;
        } else {
            last = midpoint - 1
        }
    }
    return null;
}

function verify(index){
    // Verifies if the index is found and prints in the console
    if (index != null){
        console.log(`Target was found on index: ${index}`)
    } else{
        console.log("Target not found !!!")
    }
}

let result = binarySearch(list,30);
verify(result)