from typing import Protocol, runtime_checkable

@runtime_checkable
class NaturalPersonInterface(Protocol):

    @property
    def id(self): pass

    @property
    def monthly_income(self): pass

    @property
    def age(self): pass

    @property
    def full_name(self): pass

    @property
    def mobile(self): pass

    @property
    def email(self): pass

    @property
    def category(self): pass

    @property
    def balance(self): pass
