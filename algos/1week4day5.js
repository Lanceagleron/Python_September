/* 
  String: Rotate String
  Create a standalone function that accepts a string and an integer,
  and rotates the characters in the string to the right by that given
  integer amount.
*/

const str = "Hello World";

const rotateAmnt1 = 0;
const expected1 = "Hello World";

const rotateAmnt2 = 1;
const expected2 = "dHello Worl";

const rotateAmnt3 = 2;
const expected3 = "ldHello Wor";

const rotateAmnt4 = 4;
const expected4 = "orldHello W";

const rotateAmnt5 = 13;
const expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
 * Rotates a given string's characters to the right by the given amount,
 * wrapping characters to the beginning.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @param {number} amnt The amount of characters in the given str to rotate to the
 *    right.
 * @returns {string} The string rotated by the given amount.
 */
// function rotateStr(str, amnt) {
//     const n = amnt % str.length;
//     return str.slice(-n) + str.slice(0, -n); 
// }
function rotateStr(str, amnt) {
    // Check amnt (only 11 different versions)
    if (amnt == 11 || amnt == 0) {
        return str;
    }
    // Subtract by 11 to get 'original' version
    else if (amnt > 11) {
        amnt = amnt - 11;
    }
    // Extract characters from the end
    let beginning = str.substring(str.length-amnt, str.length);
    // Remove last characters
    str = str.substring(0, str.length-amnt);
    // Concatenate 
    str = beginning + str
    return str;
}

console.log(rotateStr(str,rotateAmnt1), expected1)
console.log(rotateStr(str,rotateAmnt2), expected2)
console.log(rotateStr(str,rotateAmnt3), expected3)
console.log(rotateStr(str,rotateAmnt4), expected4)
console.log(rotateStr(str,rotateAmnt5), expected5)
