class Solution:
    def intToRoman(self, num: int) -> str:
        romanString = ""

        while(1):
            if (num >= 1000):
                num -= 1000
                romanString += 'M'
            elif (num >= 500):
                if (num >= 900):
                    romanString += 'CM'
                    num -= 900
                else:
                    romanString += 'D'    
                    num -= 500 

            elif (num >= 100):
                if (num >= 400):
                    romanString += 'CD'
                    num -= 400
                else:
                    romanString += 'C'    
                    num -= 100 

            elif (num >= 50):
                if (num >= 90):
                    romanString += 'XC'
                    num -= 90
                else:
                    romanString += 'L'    
                    num -= 50

            elif (num >= 10):
                if (num >= 40):
                    romanString += 'XL'
                    num -= 40
                else:
                    romanString += 'X'    
                    num -= 10

            elif (num >= 5):
                if (num >= 9):
                    romanString += 'IX'
                    num -= 9
                else:
                    romanString += 'V'    
                    num -= 5

            elif (num >= 1):
                if (num >= 4):
                    romanString += 'IV'
                    num -= 4
                else:
                    romanString += 'I'    
                    num -= 1

            else:
                return romanString;

