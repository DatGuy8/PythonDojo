const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

function listSeparator(arr, separator) {
    var text = "";
    for (var i = 0; i < arr.length; i++) {
        text += (arr[i]);
        if (i < arr.length - 1) {
            text += separator;
        }
        return text;
    }
}

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

console.log(listSeparator(arr1, separator1))


const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

const nums2 = [5, 6, 7, 8, 9];
const expected2 = "5-9";

const nums3 = [1, 2, 3, 7, 9, 15, 16, 17];
const expected3 = "1-3, 7, 9, 15-17";



function pageLister(arr) {
    var pages = "";
    for (var i = 0; i < arr.length; i++) {
        pages += arr[i];
        if (arr[i] == arr[i + 1] - 1) {
            while (arr[i]== arr[i + 1] - 1){
                i++;
            }
        pages += "-"+ arr[i];
        }
        if (i < arr.length-1){
            pages +=",";
        }
    }
return pages;
}

console.log(pageLister(num1))