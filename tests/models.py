from django.db import models
from issn_field import ISSNField

class CleanISSNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    issn = ISSNField() # clean_issn=True (default)


class DirtyISSNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    issn = ISSNField(clean_issn=False)


class BlankISSNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    issn = ISSNField(clean_issn=True, blank=True)

class BlankNullISSNModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    issn = ISSNField(clean_issn=True, blank=True, null=True)
