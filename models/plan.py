from models.date import Date

# *** Plan ***
class Plan:
    dates : list = []
    
    @staticmethod
    def show():
        if len(Plan.dates) > 0:
            for date in Plan.dates:
                print(date)
                
        else:
            print('Plan is empty')
            
    @staticmethod
    def get_plan_by_date(year : int, month : int, day : int):
        d = Date(day, month, year)
        
        for date in Plan.dates:
            if d.__eq__(date):
                return date
        
        return None