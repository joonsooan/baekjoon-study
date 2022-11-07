class Calculator:

    def __init__(self):
        self.result = 0


    def add(self, num):
        self.result += num
        return self.result


    def mul(self, num):
        self.result *= num
        return self.result


    def sub(self, num):
        self.result -= num
        return self.result


    def div(self, num):
        if num == 0:
            return 0
        else:
            self.result //= num
            return self.result
    

    def pow(self, num):
        answer = self.result ** num
        return answer