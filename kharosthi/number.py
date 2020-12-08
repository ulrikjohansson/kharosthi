import re

class KharosthiNumber():

    int_to_kharosthi = {
        1: "𐩀",
        2: "𐩁",
        3: "𐩂",
        4: "𐩃",
        10: "𐩄",
        20: "𐩅",
        100: "𐩆",
        1000: "𐩇"
    }
    valid_regex = re.compile(r'[^𐩀𐩁𐩂𐩃𐩄𐩅𐩆𐩇]')

    

    number: str

    def __init__(self, number:str) -> None:
        self.validate(number)
        self.number = number

    def validate(self, number:str):
        #check that the number is a string and only contains valid digits
        if not type(number) is str:
            raise ValueError("Invalid input: Not a string")
        
        # check that it only contains valid characters
        # solution found here: https://stackoverflow.com/a/1325265/306458
        if bool(self.valid_regex.search(number)):
            raise ValueError("Invalid input: Contains invalid characters")

    @classmethod
    def _int_to_kharosthi(cls, number:int) -> str:
        result = ""

        # TODO: Calculate!
        # Find the biggest kharosthi common divisor(?)
        while number > 0:
            if khar := cls.int_to_kharosthi.get(number):
                result += khar
                break

            gcd = 4 # start at 4, since all numbers 4 or below are directly representable with a kharosthi digit
            for key in cls.int_to_kharosthi.keys():
                if key < number:
                    gcd = key
                    continue
                break
            
            quotitient, remainder = divmod(number, gcd)
            if gcd >= 100 and quotitient > 1:
                result += cls._int_to_kharosthi(quotitient) + cls.int_to_kharosthi[gcd]
            else:
                result += cls.int_to_kharosthi[gcd]*quotitient
            number = remainder

        if result:
            return result

        # we can't convert this number
        raise ValueError("Input can't be converted to a Kharosthi number")

    def __str__(self) -> str:
        return self.number

    @classmethod
    def from_int(cls, int_number:int):
        return cls(cls._int_to_kharosthi(int_number))