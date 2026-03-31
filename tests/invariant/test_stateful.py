from hypothesis import settings
from hypothesis.stateful import RuleBasedStateMachine, rule
from contracts.invariant import stateful_fuzz_solvable
from boa.test.strategies import strategy


class StatefulFuzzer(RuleBasedStateMachine):
    def __init__(self):
        super().__init__()
        self.contract = stateful_fuzz_solvable.deploy()
        print(f"Deployed contract at address: {self.contract.address}")

    # Rules -> Actions, and have properties / invariants
    # Invariants -> Properties that should always hold true
    @rule(new_number=strategy("uint256"))
    def change_number(self, new_number):
        self.contract.change_number(new_number)
        print(f"Changed number to: {new_number}")

    @rule(input=strategy("uint256"))
    def input_number_returns_itself(self, input):
        response = self.contract.always_returns_input_number(input)
        print(f"Input: {input}, Response: {response}")
        assert response == input, f"Expected {input}, but got {response}"


TestStatefulFuzzing = StatefulFuzzer.TestCase
TestStatefulFuzzing.settings = settings(max_examples=10000)
