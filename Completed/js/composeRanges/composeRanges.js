function composeRanges(nums) {
  if (nums.length == 0) {
    return nums;
  } else if (nums.length == 1) {
    return [`${nums[0]}`];
  } else {
    let ret_a = [],
      i = 0,
      j = 0,
      k = 1;
    while (k < nums.length) {
      if (nums[j] == nums[k] - 1) {
        j++;
      } else {
        ret_a.push(
          nums[i] != nums[j] ? `${nums[i]}->${nums[j]}` : `${nums[j]}`,
        );
        i = k;
        j = k;
      }
      k++;
    }
    ret_a.push(i != j ? `${nums[i]}->${nums[j]}` : `${nums[j]}`);
    return ret_a;
  }
}
console.log(composeRanges([]));
console.log(composeRanges([1]));
console.log(composeRanges([1, 2, 3, 4, 5, 6]));
console.log(composeRanges([-1, 5, 10, 14, 15, 21, 22]));
console.log(composeRanges([-1, 0, 1, 2, 6, 7, 9]));
