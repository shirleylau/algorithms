console.log(findSumOfMultiples(1000, [3, 5]));

var sum = 0;
for (var i = 1; i < 1000; i++) {
  if ( i % 3 === 0 || i % 5 === 0) {
    sum = sum + i;
  }
}

console.log(sum);





































function findSumOfMultiples(maxNum, multiplesArr) {
  var multiples = multiplesArr.map(function(multiplier) {
    return findMultiples(multiplier, maxNum);
  });

  multiples = [].concat.apply([], multiples);

  multiples.sort();

  var sum = 0;
  var prev = 0;

  for (var i = 0; i < multiples.length; i++) {
    if (multiples[i] !== prev) {
      sum = multiples[i] + sum;
    }

    prev = multiples[i];
  }
   return sum;
}

function findMultiples(multiplier, max) {
  var maxMultiple = max / multiplier;
  var remainder = max % multiplier;
  var multiples = [];

  if (remainder === 0) {
    maxMultiple--;
  } else {
    maxMultiple = Math.floor(maxMultiple);
  }

  var x = 1;
  while (x <= maxMultiple) {
    var multiple = x * multiplier;
    multiples.push(multiple);
    x++;
  }

  return multiples;
}
