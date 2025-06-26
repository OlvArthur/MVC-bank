from typing import Protocol, runtime_checkable

@runtime_checkable
class JuridicalPersonInterface(Protocol):
    @property
    def id(self): pass

    @property
    def revenue(self): pass

    @property
    def age(self): pass

    @property
    def trade_name(self): pass

    @property
    def mobile(self): pass

    @property
    def corporate_email(self): pass

    @property
    def category(self): pass

    @property
    def balance(self): pass
