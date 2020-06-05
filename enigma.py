import numpy as np

# variabelen---------------
rotors = ("I","II","III","IV", "V")
plug = "AT BS DE FM IR KN LZ OW PV XY"
ringSet = "ABC"
ringPos = "DEF"

def crypt(text):
  global rotors, plug, ringSet, ringPos
  
  rotor1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  rotor2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  rotor3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  rotor4 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  rotor5 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  rotor1slag = 'D'
  rotor2slag = 'E'
  rotor3slag = 'X'
  rotor4slag = 'J'
  rotor5slag = 'Z'

  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
