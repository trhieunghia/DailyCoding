# Return True
# if the given string contains an appearance of "xyz"
# where the xyz is not directly preceeded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
#
#
# xyz_there('abcxyz') → True
# xyz_there('abc.xyz') → False
# xyz_there('xyz.abc') → True


class Xyz:

    def __init__(self, s1=""):
        self.s1 = s1
        self.xyz = "xyz"

    def xyz_there(self):
        if len(self.s1) < len(self.xyz):
            return False

        for i in range(0, len(self.s1) - len(self.xyz) + 1):
            if self.s1[i-1] != "." \
                    and self.s1[i:i + len(self.xyz)] == self.xyz:
                return True
        return False
