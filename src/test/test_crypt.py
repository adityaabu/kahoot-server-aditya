import unittest
from ..utils.crypt import encrypt

class TestCryptMethods(unittest.TestCase):
    
    def testEncrypBenar(self):
        self.assertEqual(encrypt("a",4),"e")
        self.assertEqual(encrypt("b",4),"f")

    # def testEncrypGagal(self):
    #     self.assertEqual(encrypt("a",4),"e")
    #     self.assertEqual(encrypt("b",4),"h")

    if __name__ == '__main__':
        unittest.main()

#kalau fungsi berfungsi
# to test : (Kahoot) C:\Users\adity\OneDrive\Documents\Bootcamp Makers Institute\Kahoot\projects\kahoot-server-aditya>python -m unittest src/test/test_crypt.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
# kalau fungsi tidak berfungsi
# (Kahoot) C:\Users\adity\OneDrive\Documents\Bootcamp Makers Institute\Kahoot\projects\kahoot-server-aditya>python -m unittest src/test/test_crypt.py
# F
# ======================================================================
# FAIL: testEncryp (src.test.test_crypt.TestCryptMethods)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\adity\OneDrive\Documents\Bootcamp Makers Institute\Kahoot\projects\kahoot-server-aditya\src\test\test_crypt.py", line 8, in testEncryp
#     self.assertEqual(encrypt("b",4),"j")
# AssertionError: 'f' != 'j'
# - f
# + j


# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (failures=1)