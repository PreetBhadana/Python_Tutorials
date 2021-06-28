class calculator:
	
    def add(self, x, y):
        self.x = x
        self.y = y
	return (self.x + self.y)
	
    def sub(self, x, y):
	return (x - y)
	
    def mul(self, x, y):
	return (x * y)

    def dev(self, x , y):
	return (x // y)

obj = calculator()
print(obj.add(2, 4))
print(obj.sub(4, 2))
print(obj.mul(2, 4))
print(obj.dev(4, 2))
