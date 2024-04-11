from main import *

def test_caesar():
  assert caesar("FRIENDS ROMANS COUNTRYMEN LEND ME YOUR EAR", -20) == "MYPLUKZGYVTHUZGJVAU YETLUGSLUKGTLGEVAYGLHY"
  assert caesar("A quick brown fox jumps over the lazy dog",-23) == "EDUYMGODFVS RDJSADNYQTWDSZIVDXLIDPECBDHSK"
  assert caesar("myplukzgyvthuzgjvau yetlugslukgtlgevayglhy", 20) == "FRIENDS ROMANS COUNTRYMEN LEND ME YOUR EAR"
  assert caesar("EDUYMGODFVS RDJSADNYQTWDSZIVDXLIDPECBDHSK",23) == "A QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

def test_vigenere_encrypt():
  assert vigenere_encrypt("ATTACK AT DAWN", "LEMON") == "LXEOPVDMGMOEHA"
  assert vigenere_encrypt("THE EAGLE HAS LANDED", "AMERICA") == "TTIQMCGLQDYIU LMRUMF"

def test_vignere_decrypt():
  assert vigenere_decrypt("LXEOPVDMGMOEHA", "LEMON") == "ATTACK AT DAWN"
  assert vigenere_decrypt("TTIQMCGLQDYIU LMRUMF", "AMERICA") == "THE EAGLE HAS LANDED"
