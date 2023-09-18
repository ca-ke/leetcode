class Solution {
  String decodeMessage(String key, String message) {
    final alphabet = 'abcdefghijklmnopqrstuvwxyz'.split('');
    final keyWithoutSpace = key.split(' ').join();
    final mappedKey = <String, String>{};
    final stringBuffer = StringBuffer();

    var alphabetCounter = 0;
    for (var i = 0; i < keyWithoutSpace.length; i++) {
      if (!mappedKey.containsKey(keyWithoutSpace[i])) {
        mappedKey[keyWithoutSpace[i]] = alphabet[alphabetCounter];
        alphabetCounter++;
      }
    }

    for (var i = 0; i < message.length; i++) {
      if (mappedKey.containsKey(message[i])) {
        stringBuffer.write(mappedKey[message[i]]);
      } else {
        stringBuffer.write(' ');
      }
    }

    return stringBuffer.toString();
  }
}
