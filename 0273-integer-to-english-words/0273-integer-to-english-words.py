class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        billion = num//1000000000 #9 0's
        million = (num - billion*1000000000)//1000000 #6 0's
        thousand= (num - billion*1000000000 - million*1000000)//1000
        hundred = (num - billion*1000000000 - million*1000000 - thousand*1000)
        result = ""
        def three(x):
            hundreds = x//100
            tens = (x - hundreds*100)//10
            units = (x- hundreds*100 - tens*10)
            res = ""
            if hundreds != 0:
                res += num_dictionary[hundreds] + " Hundred "
            if tens > 1 :# !=0 AND not one as its eleven, tweleve
                res += ten_dictionary[tens] + " "
            elif tens == 1:
                teen = (x - hundreds*100) 
                res += teen_dictionary[teen] + " "
            if units !=0 and tens != 1 :
                res += num_dictionary[units] + " "
            return res
        num_dictionary = { 
            1 :"One", 2:"Two", 3:"Three", 4:"Four",5:"Five",
            6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"
            }
        ten_dictionary = {
            2: "Twenty", 3:"Thirty", 4: "Forty",5:"Fifty", 
            6:"Sixty", 7:"Seventy",8:"Eighty",9:"Ninety" 
        }
        teen_dictionary =  {
            10: "Ten",11:"Eleven" ,12: "Twelve",13: "Thirteen" ,14:"Fourteen",
            15: "Fifteen",16:"Sixteen",17:"Seventeen", 18:"Eighteen",19:"Nineteen"
        }
        
        if billion != 0:
            result += three(billion) + "Billion "
        if million != 0:
            result += three(million) + "Million "
        if thousand != 0:
            result += three(thousand) + "Thousand "
        if hundred != 0:
            result += three(hundred) 
        
        return result.strip()