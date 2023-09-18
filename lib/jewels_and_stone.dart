class Solution {
  int numJewelsInStones(String jewels, String stones) {
    final jewelsMap = <String, int>{};
    for (var i = 0; i < jewels.length; i++) {
      jewelsMap[jewels[i]] = 0;
    }

    for (var i = 0; i < stones.length; i++) {
      if (jewelsMap.containsKey(stones[i])) {
        jewelsMap[stones[i]] = jewelsMap[stones[i]]! + 1;
      }
    }

    return jewelsMap.values.reduce((a, b) => a + b);
  }
}
