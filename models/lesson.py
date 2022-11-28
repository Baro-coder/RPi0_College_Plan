from enum import Enum

# *** Lesson ***
class LessonType(Enum):
    LECTURE = 'w'
    EXCERCISES = 'ć'
    LABORATORY = 'L'
    PROJECT = 'P'
    OTHER = 'I'
    EMPTY = '-'
    
class Lesson:
    def __init__(self, block_id = int, subject = str, type = LessonType, place = str, info = str):
        self.block_id = block_id
        self.subject = subject
        self.type = type
        self.place = place
        self.info = info

    def __str__(self) -> str:
        return f'Blok {self.block_id} : {self.subject} ({self.type.value}) {self.place}'
