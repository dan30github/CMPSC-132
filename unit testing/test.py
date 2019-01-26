import unittest
from LAB4 import *

class encrypt_decryptTestCase(unittest.TestCase):
    """Tests for 'lab4.py'"""
    def test_encrypt_normal_frase1(self):
    	"""Is case1 correct?"""
    	correct = 'Nz obnf jt Ebojfm, boe J bn b dpnqvufs fohjoffsjoh tuvefou bu Qfoo Tubuf Vojwfstjuz'
    	self.assertEqual(encrypt('My name is Daniel, and I am a computer engineering student at Penn State University', 1), correct)

    def test_encrypt_normal_frase2(self):
    	"""Is case2 correct?"""
    	correct = 'Oa pcog ku Fcpkgn, cpf K co c eqorwvgt gpikpggtkpi uvwfgpv cv Rgpp Uvcvg Wpkxgtukva'
    	self.assertEqual(encrypt('My name is Daniel, and I am a computer engineering student at Penn State University', 2), correct)

    def test_encrypt_normal_frase3(self):
    	"""Is case3 correct?"""
    	correct = 'Pb qdph lv Gdqlho, dqg L dp d frpsxwhu hqjlqhhulqj vwxghqw dw Shqq Vwdwh Xqlyhuvlwb'
    	self.assertEqual(encrypt('My name is Daniel, and I am a computer engineering student at Penn State University', 3), correct)

    def test_for_extreme_encrypt(self):
    	"""Is it working when using the last letters in the alphabet?"""
    	correct = 'JJJ kkk LLL'
    	self.assertEqual(encrypt('XXX yyy ZZZ', 12), correct)

    def test_encrypt_punctuation_numbers(self):
        """ Does it work with punctuation and numbers?"""
        correct = 'Alza mvy wbujabhapvu huk ubtilyz: 123,.!?'
        self.assertEqual(encrypt('Test for punctuation and numbers: 123,.!?', 7), correct)

    def test_encrypt_for_same_key(self):
        """Does encrypt and decrypt return same message if key is the same?"""
        correct = 'Yjxy ktw xfrj pjd = 5.'
        self.assertEqual(encrypt('Test for same key = 5.', 5), correct)


    def test_decrypt_normal_frase1(self):
    	"""Is case1 correct?"""
    	correct = 'My name is Daniel, and I am a computer engineering student at Penn State University'
    	self.assertEqual(decrypt('Yk zmyq ue Pmzuqx, mzp U my m oaybgfqd qzsuzqqduzs efgpqzf mf Bqzz Efmfq Gzuhqdeufk', 12), correct)

    def test_decrypt_normal_frase2(self):
        """Is case2 correct?"""
        correct = 'My name is Daniel, and I am a computer engineering student at Penn State University'
        self.assertEqual(decrypt('Zl anzr vf Qnavry, naq V nz n pbzchgre ratvarrevat fghqrag ng Craa Fgngr Havirefvgl', 13), correct)

    def test_decrypt_normal_frase3(self):
        """Is case2 correct?"""
        correct = 'My name is Daniel, and I am a computer engineering student at Penn State University'
        self.assertEqual(decrypt('Am boas wg Robwsz, obr W oa o qcadihsf sbuwbssfwbu ghirsbh oh Dsbb Ghohs Ibwjsfgwhm', 14), correct)

    def test_for_extreme_decrypt(self):
        """Is it working when using the firsr letters in the alphabet?"""
        correct = 'OOO ppp QQQ'
        self.assertEqual(decrypt('AAA bbb CCC', 12), correct)

    def test_decrypt_punctuation_numbers(self):
        """ Does it work with punctuation and numbers?"""
        correct = 'Test for punctuation and numbers: 123,.!?'
        self.assertEqual(decrypt('Alza mvy wbujabhapvu huk ubtilyz: 123,.!?', 7), correct)

    def test_decrypt_for_same_key(self):
        """Does encrypt and decrypt return same message if key is the same?"""
        correct = 'Test for same key = 5.'
        self.assertEqual(decrypt('Yjxy ktw xfrj pjd = 5.', 5), correct)


if __name__ == '__main__':
    unittest.main(exit=False)