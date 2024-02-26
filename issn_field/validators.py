from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from six import string_types
from stdnum import issn


def ISSNValidator(raw_issn):
    """ Check string is a valid ISSN number"""
    issn_to_check = raw_issn.replace('-', '').replace(' ', '')

    if not isinstance(issn_to_check, string_types):
        raise ValidationError(_(u'Invalid ISSN: Not a string'))

    if len(issn_to_check) != 8:
        raise ValidationError(_(u'Invalid ISSN: Wrong length'))
    
    if not issn.is_valid(issn_to_check):
        raise ValidationError(_(u'Invalid ISSN: Failed checksum'))

    if issn_to_check != issn_to_check.upper():
        raise ValidationError(_(u'Invalid ISSN: Only upper case allowed'))

    return True
