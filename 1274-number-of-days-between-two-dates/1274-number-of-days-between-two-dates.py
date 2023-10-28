class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def calc_Days(date):
            days = 0
            year, month, day = map(int,date.split('-'))
            for y in range(1900, year):
                days +=  365
                if ( y%4 == 0):
                    if y%100 != 0 or (y%100==0 and y%400==0):
                        days +=1
            for m in range(1, month):
                if m in [1,3,5,7,8,10,12]:
                    days += 31
                elif m == 2:
                    days += 28 
                    if (year%4 ==0 ):
                        if year%100 != 0 or ( year%100==0 and year%400==0):
                            days +=1
                else: #m in [4,6,9,11]
                    days +=30
            return days +day
        return abs(calc_Days(date1)-calc_Days(date2))

