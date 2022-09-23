/*
  Recursive Binary Search
  Input: SORTED array of ints, int value
  Output: bool representing if value is found
  Recursively search to find if the value exists, do not loop over every element.
  Approach:
  Take the middle item and compare it to the given value.
  Based on that comparison, narrow your search to a particular section of the array
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

/**
 * Add params if needed for recursion
 * Recursively performs a binary search (divide and conquer) to determine if
 * the given sorted nums array contains the given number to search for.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the searchNum was found in the sortedNums array.
 */
// don't be afraid to add parameters!
    function binarySearch(sortedNums, searchNum) {
        var lo = 0
        var hi = sortedNums.length - 1
        var mid
        //Setting variable for the function ^
        while (lo <= hi){
            mid = Math.floor((lo+hi)/2)
            //Finding the middle of the array, rounding down to the nearest integer
            if(sortedNums[mid] > searchNum)
                hi = mid-1;
                //If the number is greater than the search num, change hi to mid-1
            else if (sortedNums[mid] < searchNum)
                lo = mid+1;
                //If the number is less than the search num, change lo to mid+1
            else
                return true
                //Runs until sortedNums[mid] == searchNum
        }
        return false
        //If searchNum not found, return false
    }
    



console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true
console.log(binarySearch(nums3, searchNum3)); // true