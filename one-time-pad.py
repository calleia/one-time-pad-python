#!/usr/bin/python3.5
import random
import sys


def getByte(bits):
  return int(bits, 2)


def xor(x, y):
  return bool(x) ^ bool(y)


# Function definition is here
def getBits(byte):
  bits = '{0:08b}'.format(ord(byte))
  return bits


def encrypt(byte):
  bits = getBits(byte)

  key1 = []
  key2 = []
  for bit in bits:
    aux = random.randint(0, 1)
    key1.append(str(aux))
    key2.append(str(int(xor(int(bit),aux))))

  keys = []
  keys.append(chr(getByte("".join(key1))))
  keys.append(chr(getByte("".join(key2))))

  return keys;


def decrypt(key1,key2):
  key1Bits = getBits(key1)
  key2Bits = getBits(key2)

  key = []
  for i in range(0, 8):
    key.append(str(int(xor(int(key1Bits[i]),int(key2Bits[i])))))

  return getByte("".join(key))


def encryptFile(input1, output1, output2):
  key1File = open(output1, 'wb')
  key2File = open(output2, 'wb')

  with open(input1, "rb") as f:
    byte = f.read(1)
    while byte:
      aux = encrypt(byte)
      key1File.write(ord(aux[0]).to_bytes(1,byteorder="big",signed=False))
      key2File.write(ord(aux[1]).to_bytes(1,byteorder="big",signed=False))
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


