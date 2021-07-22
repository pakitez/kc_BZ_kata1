import unittest
from romanos import a_numero

class RomanosTests(unittest.TestCase):
    def test_digitos_romanos(self):
        self.assertEqual(a_numero("I"), 1)
        self.assertEqual(a_numero("V"), 5)

    def test_numeros_completos(self):
        self.assertEqual(a_numero("XXV"), 25)
        self.assertEqual(a_numero("CDXXIV"), 424)

    def test_no_se_resta_V_L_D(self):    
        with self.assertRaises(ValueError):
            a_numero("VC")

    def test_no_se_resta_mas_de_un_salto(self):
        self.assertEqual(a_numero("IV"), 4)
        self.assertEqual(a_numero("IX"), 9)
        self.assertEqual(a_numero("XL"), 40)
        self.assertEqual(a_numero("XC"), 90)
        self.assertEqual(a_numero("CD"), 400)
        self.assertEqual(a_numero("CM"), 900)
        with self.assertRaises(ValueError):
            a_numero("IL")
        with self.assertRaises(ValueError):
            a_numero("IC")
        with self.assertRaises(ValueError):
            a_numero("IM")
        with self.assertRaises(ValueError):
            a_numero("XM")
        with self.assertRaises(ValueError):
            a_numero("XD")
            
    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(a_numero("III"),3)
        with self.assertRaises(ValueError):
            a_numero("IIII")

    def test_no_restas_dos_iguales(self):
        with self.assertRaises(ValueError):
            a_numero("XXL")
        with self.assertRaises(ValueError):
            a_numero("CCM")
        with self.assertRaises(ValueError):
            a_numero("IIX")
        with self.assertRaises(ValueError):
            a_numero("CCCM")

    def test_no_multiplos_de_cinco_seguidos(self):
        with self.assertRaises(ValueError):
            a_numero("VV")
        with self.assertRaises(ValueError):
            a_numero("LL")
        with self.assertRaises(ValueError):
            a_numero("DD")

    def test_no_restas_consecutivas(self):
        with self.assertRaises(ValueError):
            a_numero("IXC")
            
    def test_no_mayor_de_15_caracteres(self):
        with self.assertRaises(ValueError):
            a_numero("MMMDCCCLXXXVIIII")
            

