class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        previous = 0
        for symbol in s:
            value = roman_numerals[symbol]
            # need to subtract the previous value twice because it was already added once
            if value > previous:
                result += value - 2 * previous
            else:
                result += value
            previous = value
        return result

