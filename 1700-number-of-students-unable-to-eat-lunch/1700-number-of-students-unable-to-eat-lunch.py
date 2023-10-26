class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_passed = 0
        while students and num_passed <= len(students):
            student = students[0]
            sandwich = sandwiches[0]
            if student == sandwich:
                students.pop(0)
                sandwiches.pop(0)
                num_passed = 0
            else:
                students.pop(0)
                students.append(student)
                num_passed += 1
        return len(students)