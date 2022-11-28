from models.lesson import Lesson, LessonType

# *** Date ***
class Date:
    def __init__(self, day : int, month : int, year : int, lessons = []):
        self.day = day
        self.month = month
        self.year = year
        self.lessons = lessons
    
    def __eq__(self, obj) -> bool:
        if isinstance(obj, Date):
            return (self.year == obj.year) and (self.month == obj.month) and (self.day == obj.day)
        
        return False
    
    def __str__(self) -> str:
        res = f'{self.year}-{self.month}-{self.day}:\n'
        for lesson in self.lessons:
            res += '\t' + str(lesson) + '\n'
        
        return res
    
    def standardize(self):
        for i in range(7):
            lesson_exists = False
            for lesson in self.lessons:
                if lesson.block_id == i+1:
                    lesson_exists = True
                    break
            if lesson_exists:
                continue
            
            self.lessons.insert(i, Lesson(i+1, '-', LessonType.EMPTY, '-', '-'))
