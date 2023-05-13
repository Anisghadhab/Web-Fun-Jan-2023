var sum = 0;

function betterThanAverage(arr) {
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    var count = 0
    avg = sum / arr.length + 1;
    for (j = 0; j < arr.length; j++) {
        if (arr[j] < avg) {
            count += 1;
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);
