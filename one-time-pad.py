#!/usr/bin/python3.5
import random
import sys


def encrypt(byte):
  byte = ord(byte)

  keys = []
  keys.append(random.randint(0, 255))
  keys.append(byte ^ keys[0])

  return keys


def decrypt(byte0,byte1):
  keys = []
  keys.append(ord(byte0))
  keys.append(ord(byte1))

  aux = keys[0] ^ keys[1]

  return aux


def encryptFile(input1, output1, output2):
  key1File = open(output1, 'wb')
  key2File = open(output2, 'wb')

  with open(input1, "rb") as f:
    byte = f.read(1)
    while byte:
      aux = encrypt(byte)
      key1File.write(aux[0].to_bytes(1,byteorder="big",signed=False))
      key2File.write(aux[1].to_bytes(1,byteorder="big",signed=False))
      byte = f.read(1)


def decryptFile(input1, input2, output1):
  output1 = open(output1, 'wb')

  with open(input1, "rb") as f1:
    with open(input2, "rb") as f2:
      byte1 = f1.read(1)
      byte2 = f2.read(1)
      while byte1:
        output1.write(decrypt(byte1, byte2).to_bytes(1,byteorder="big",signed=False))
        byte1 = f1.read(1)
        byte2 = f2.read(1)


print("Starting script...")

if len(sys.argv) == 2:
  encryptFile(sys.argv[1], sys.argv[1] + ".0", sys.argv[1] + ".1")
elif len(sys.argv) == 3:
  decryptFile(sys.argv[1], sys.argv[2], sys.argv[1][:-2])
else:
  print("Argument parsing error.")

print("Script finished.")
