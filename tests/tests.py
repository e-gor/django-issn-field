from django.core.exceptions import ValidationError
from issn_field.validators import ISSNValidator
from issn_field import ISSNField

from django.test import TestCase

from .models import CleanISSNModel, DirtyISSNModel, BlankISSNModel, BlankNullISSNModel

class ISSNValidatorTest(TestCase):

    def test_ISSN_too_short(self):
        with self.assertRaises(ValidationError):
            ISSNValidator('111')

        with self.assertRaises(ValidationError):
            ISSNValidator('')

    def test_ISSN_too_long(self):
        with self.assertRaises(ValidationError):
            ISSNValidator('123456789')

    def test_ISSN_with_illegal_structure(self):
        with self.assertRaises(ValidationError):
            ISSNValidator('2530-2486')

    def test_invalid_lower_case_x_ISSN(self):
        with self.assertRaises(ValidationError):
            ISSNValidator('2530-248x')

    def test_dashes_as_valid_separators(self):
        assert(ISSNValidator('2530-2485'))
        assert(ISSNValidator('2-5-3-0-2-4-8-5'))

    def test_spaces_as_valid_separators(self):
        assert(ISSNValidator('2530 2485'))
        assert(ISSNValidator('2 5 3 0 2 4 8 5'))

    def test_space_and_dash_as_valid_separators(self):
        assert(ISSNValidator('2 530-248 5'))
        assert(ISSNValidator('2 5 3 0-2 4 8 5'))

    def test_valid_ISSNs(self):
        assert(ISSNValidator('25302485'))


class ISSNFieldTest(TestCase):

    def test_issn_field_clean(self):
        
        issns = [
            ('25302485', '2-530-248-5'),
            ('25302485', '2 530 248 5'),
            ('25302485', '2-530 248-5'),
            ('25302485', '2530-2485')]
        
        for clean, original in issns:
            m = CleanISSNModel.objects.create(issn=original)
            self.assertEqual(m.issn, clean)

            m = DirtyISSNModel.objects.create(issn=original)
            self.assertEqual(m.issn, original)

    def test_issn_field_blank(self):
        """Test empty values are accepted when blank=True"""
        m = BlankISSNModel.objects.create(issn="")
        self.assertEqual(m.issn, "")

    def test_issn_field_null(self):
        """Test null values are accepted when blank=True null=True"""
        m = BlankNullISSNModel.objects.create(issn=None)
        self.assertEqual(m.issn, None)

