var divisor = 13194;
var prime = 0;

while (prime == 0) {
  if (13195 % divisor == 0) {
    var num = 2;
    var isPrime = true;
    while (num < divisor && isPrime == true) {
      if (divisor % num == 0) {
        isPrime = false;
      }
      num++;
    }
    if (isPrime == true) {
      prime = divisor;
    }
  }
  divisor--;
}

console.log(prime);
