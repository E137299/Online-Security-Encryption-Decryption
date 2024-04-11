from main import *

def test_caesar():
  assert caesar("FRIENDSROMANSCOUNTRYMENLENDMEYOUREAR", -20) == "LXOKTJYXUSGTYIUATZXESKTRKTJSKEUAXKGX"
  assert caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -3) == "XYZABCDEFGHIJKLMNOPQRSTUVW"
  assert cesar_encrypt("LXOKTJYXUSGTYIUATZXESKTRKTJSKEUAXKGX", 20) == "FRIENDSROMANSCOUNTRYMENLENDMEYOUREAR"

def test_vigenere_encrypt():
  assert vigenere_encrypt("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
  assert vigenere_encrypt("THEEAGLEHASLANDED", "AMERICA") == "TTIVIILETEJTCNDQH"

def test_vignere_decrypt():
  assert vigenere_decrypt("LXFOPVEFRNHR", "LEMON") == "ATTACKATDAWN"
  assert vigenere_decrypt("TTIVIILETEJTCNDQH", "AMERICA") == "THEEAGLEHASLANDED"
  
