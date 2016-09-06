var words = [
  'ptolemaic', //0
  'retrograde',
  'supplant',
  'undulate',
  'xenoepist', // 4
  'zzzz',
  'zzzzzzz',
  'zzzzzzzzzz',
  'asymptote', // <-- rotates here!
  'babka', // 8
  'banoffee',
  'engender',
  'karpatka',
  'othellolagkage', //12
];

function findRotationPoint(array) {
  var rotationIdx = startIdx = 0; // Point of lowest found value
  var endIdx = array.length - 1;
  while (endIdx - startIdx > 0) {
    var midIdx = startIdx + Math.floor((endIdx - startIdx) / 2);
    if (array[rotationIdx] > array[midIdx]) {
      rotationIdx = endIdx = midIdx;
    } else {
      startIdx = midIdx + 1;
    }
  }
  return rotationIdx;
}

console.log(findRotationPoint(words));
