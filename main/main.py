class Course:
    def __init__(self, title, students_count, capacity):
        self.title = title
        self.students_count = students_count
        self.capacity = capacity

    def enroll(self):
        if self.students_count < self.capacity:
            self.students_count += 1
            print("Ro‘yxatdan o‘tdi")
        else:
            print("Joy yo‘q")
