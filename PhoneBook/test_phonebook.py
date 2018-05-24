import unittest
from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_entry_by_name(self):
        self.phonebook.add('Ali', '12345')
        self.assertEqual('12345', self.phonebook.lookup('Ali'))

    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")

    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Ali", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_duplicate_entries_is_consistent(self):
        self.phonebook.add("Ali", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertTrue(self.phonebook.is_consistent())

    def test_phonebook_with_number_prefix_one_is_consistent(self):
        self.phonebook.add("Ali", "12345")
        self.phonebook.add("Mary", "123")
        self.assertTrue(self.phonebook.is_consistent())
    # For memory management and should be after all the test ran
    # teardown only runs if the setup is successful
    def tearDown(self):
        pass

