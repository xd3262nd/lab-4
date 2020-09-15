import camelcase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelcase.camelcase('Hello World'))

    def test_camelcase_with_new_line_and_tab(self):
        self.assertEqual('aNewLineComingUp', camelcase.camelcase('a neW LinE cOming \n uP'))
        self.assertEqual('tabHereTest', camelcase.camelcase('\t\t tab \t heRe teSt'))

    def test_camelcase_with_extra_space(self):
        self.assertEqual('thisIsAString', camelcase.camelcase('     this   iS    a StrING   '))

    def test_camelcase_with_empty_string(self):
        self.assertEqual('', camelcase.camelcase('       '))
        self.assertEqual('', camelcase.camelcase(''))

    def test_camcelcase_with_numbers(self):
        self.assertEqual('numbers1234Five', camelcase.camelcase('numbers 1234 fiVe'))

    def test_camelcase_with_symbols(self):
        self.assertEqual('here*Is^^^TheSymbol!', camelcase.camelcase('here   *  Is ^^^ The SYmbol!'))

    def test_camelcase_with_caps(self):
        self.assertEqual('capsIsAwesome', camelcase.camelcase('CAPS IS   AWESOME'))
