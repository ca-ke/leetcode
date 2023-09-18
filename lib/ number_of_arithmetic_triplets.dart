class Solution {
  int arithmeticTriplets(List<int> nums, int diff) {
    int answer = 0;
    final lenght = nums.length;
    for (var i = 0; i < lenght; i++) {
      for (var j = i + 1; j < lenght; j++) {
        for (var k = j + 1; k < lenght; k++) {
          if (nums[j] - nums[i] == diff && nums[k] - nums[j] == diff) {
            answer++;
          }
        }
      }
    }

    return answer;
  }
}
