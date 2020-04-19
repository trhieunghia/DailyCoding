# Given 3 int values, a b c, return their sum.
# However, if any of the values is a teen
# -- in the range 13..19 inclusive --
# then that value counts as 0,
# except 15 and 16 do not count as a teens
#
#  For example:
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3


class Exercise00NoTeenSum:

    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def no_teen_sum(self):
        summary = 0
        summary += self.fix_value(self.a)
        summary += self.fix_value(self.b)
        summary += self.fix_value(self.c)
        return summary

    @staticmethod
    def fix_value(value):
        teen = [13, 14, 17, 18, 19]
        if teen.__contains__(value):
            return 0
        return value
