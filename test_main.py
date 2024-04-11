from main import *

def test_caesar():
  assert caesar("FRIENDS ROMANS COUNTRYMEN LEND ME YOUR EAR", -20) == "myplukzgyvthuzgjvau yetlugslukgtlgevayglhy"
  assert caesar("A quick brown fox jumps over the lazy dog",-23) == "eduymgodfvs rdjsadnyqtwdszivdxlidpecbdhsk"
  assert caesar("myplukzgyvthuzgjvau yetlugslukgtlgevayglhy", 20) == "friends romans countrymen lend me your ear"
  assert caesar("eduymgodfvs rdjsadnyqtwdszivdxlidpecbdhsk",23) == "a quick brown fox jumps over the lazy dog"

def test_vigenere_encrypt():
  assert vigenere_encrypt("ATTACK AT DAWN", "LEMON") == "LXEOPVDMGMOEHA"
  assert vigenere_encrypt("THE EAGLE HAS LANDED", "AMERICA") == "TTIQMCGLQDYIU LMRUMF"

def test_vignere_decrypt():
  assert vigenere_decrypt("LXEOPVDMGMOEHA", "LEMON") == "ATTACK AT DAWN"
  assert vigenere_decrypt("TTIQMCGLQDYIU LMRUMF", "AMERICA") == "THE EAGLE HAS LANDED"
  
