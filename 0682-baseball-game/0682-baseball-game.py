class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for o in operations:
            tail = len(record) - 1
            if o == 'C':
                record.pop()
            elif o == 'D':
                record.append(record[tail] * 2)
            elif o == '+':
                record.append(record[tail] + record[tail - 1])
            else:
                record.append(int(o))
        return sum(record)