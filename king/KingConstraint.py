from CSP.Constraint import Constraint


class PotionNotSameConstraint(Constraint):
    def __init__(self, variables):
        super().__init__(variables)

    def is_satisfied(self) -> bool:
        list_of_values = [x.value for x in self.variables if x.value is not None]
        print(list_of_values)
        if len(list_of_values) == 2:
            if list_of_values[0][0] == list_of_values[1][0] or list_of_values[0][1] == list_of_values[1][1]:
                return False
        return True

        # return len(list_of_values) == len(set(list_of_values))
        # return len(set(values)) == len(values)
