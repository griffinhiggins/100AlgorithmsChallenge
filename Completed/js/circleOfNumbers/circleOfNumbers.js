function circleOfNumbers(n, firstNumber) {
  let op = n / 2 + firstNumber;
  return op > n ? op - n : op;
}

// "n must also be even" needs to be added under *Guaranteed constraints:* for the problem to be staisfied
console.log(circleOfNumbers(10, 2));
console.log(circleOfNumbers(10, 7));
console.log(circleOfNumbers(10, 0));
