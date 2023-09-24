class Solution {
  bool _attend({required bool condition}) {
    return condition;
  }

  int _min(List<int> values) {
    return 0;
  }

  int _max(List<int> values) {
    return values.length - 1;
  }

  int _binarySearch(List<int> values, int target) {
    int count = 0;
    int left = _min(values);
    int right = _max(values);

    while (left < right) {
      if (_attend(condition: values[left] + values[right] < target)) {
        count+= right - left;
        left++;
      } else {
        right--;
      }
    }
    return count;
  }

  int countPairs(List<int> nums, int target) {
    nums.sort();
    return _binarySearch(nums, target);
  }
}
