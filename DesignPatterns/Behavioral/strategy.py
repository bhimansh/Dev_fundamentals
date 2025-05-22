"""
The Strategy Pattern allows you to define a family of algorithms,
encapsulate each one, and make them interchangeable.
It lets you choose an algorithm's behavior at runtime.

✅ Where to Use Strategy Pattern
Use Case	                                            |    Description
Multiple interchangeable behaviors	                    | payment methods, sorting strategies, compression algorithms
You want to follow Open/Closed Principle	            | Easily add new behavior without modifying the existing code
You want to reduce complex if-elif-else or switch logic	| Cleaner, more maintainable design

❌ Where NOT to Use Strategy Pattern
Use Case	                                            |     Why It’s Not Ideal
Behavior doesn't change or only one algorithm is needed | Adds unnecessary complexity
Few fixed behaviors unlikely to change	                | Simpler code (like basic if/match) is more readable
You need stateful logic tightly coupled to the object	| Strategy is stateless by nature; use State pattern instead
"""
from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(PaymentStrategy):
    def pay(self):
        print('Paying via Credit-Card')

class DebitCard(PaymentStrategy):
    def pay(self):
        print('Paying via Debit-Card')

class UPI(PaymentStrategy):
    def pay(self):
        print('Paying via UPI')

class Context:
    def __init__(self, payment_method=CreditCard()):
        self.payment_method = payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def execute(self):
        self.payment_method.pay()


if __name__ == '__main__':
    ctx = Context()
    ctx.execute()       # O/P:- Paying via Credit-Card

    ctx.set_payment_method(UPI())
    ctx.execute()       # O/P:- Paying via Credit-Card

