var prev1;
var prev2 = 1;
var curr = 1;
var sum = 0;

while (curr <= 4000000) {

  if (curr % 2 === 0) {
    sum = sum + curr;
  }

  prev1 = prev2;
  prev2 = curr;
  curr = prev1 + prev2;
}

console.log(sum);
