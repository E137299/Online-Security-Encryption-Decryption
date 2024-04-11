from main import *

def test_caesar():
  assert caesar("FRIENDSROMANSCOUNTRYMENLENDMEYOUREAR", -20) == "LXOKTJYXUSGTYIUATZXESKTRKTJSKEUAXKGX"
  assert caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", -3) == "XYZABCDEFGHIJKLMNOPQRSTUVW"
  assert cesar_encrypt("LXOKTJYXUSGTYIUATZXESKTRKTJSKEUAXKGX", 20) == "FRIENDSROMANSCOUNTRYMENLENDMEYOUREAR"

def test_vigenere_encrypt():
  assert vigenere_encrypt("ATTACK AT DAWN", "LEMON") == "LXEOPVDMGMOEHA"
  assert vigenere_encrypt("THE EAGLE HAS LANDED.", "AMERICA") == "TTIOMCGLQBYIU LMRUMF"

def test_vignere_decrypt():
  assert vigenere_decrypt("LXEOPVDMGMOEHA", "LEMON") == "ATTACK AT DAWN"
  assert vigenere_decrypt("TTIQMCGLQDYIU LMRUMF", "america") == "THE EAGLE HAS LANDED"
  
