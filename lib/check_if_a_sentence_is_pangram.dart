class Solution {
  bool checkIfPangram(String sentence) {
    final alphabet = <String>{};
    for (var i = 0; i < sentence.length; i++) {
      alphabet.add(sentence[i]);
    }

    return alphabet.length == 26;
  }
}
