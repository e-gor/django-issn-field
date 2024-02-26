from .validators import ISSNValidator
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from django.core.validators import EMPTY_VALUES

class ISSNField(CharField):

    description = _("ISSN")

    def __init__(self, clean_issn=True, *args, **kwargs):
        self.clean_issn = clean_issn
        kwargs['max_length'] = kwargs['max_length'] if 'max_length' in kwargs else 18
        kwargs['verbose_name'] = kwargs['verbose_name'] if 'verbose_name' in kwargs else u'ISSN'
        kwargs['validators'] = [ISSNValidator]
        super(ISSNField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'min_length': 8,
            'validators': [ISSNValidator],
        }
        defaults.update(kwargs)
        return super(ISSNField, self).formfield(**defaults)

    def deconstruct(self):
        name, path, args, kwargs = super(ISSNField, self).deconstruct()
        # Only include clean_issn in kwarg if it's not the default value
        if not self.clean_issn:
            kwargs['clean_issn'] = self.clean_issn
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        """Remove dashes, spaces, and convert issn to uppercase before saving
        when clean_issn is enabled"""
        value = getattr(model_instance, self.attname)
        if self.clean_issn and value not in EMPTY_VALUES:
            cleaned_issn = value.replace(' ', '').replace('-', '').upper()
            setattr(model_instance, self.attname, cleaned_issn)
        return super(ISSNField, self).pre_save(model_instance, add)

    def __unicode__(self):
        return self.value
