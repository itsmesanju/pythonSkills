class Solution:


def rotatedDigits(self, N):
	count = 0
	for i in range(1, N + 1):
		if self.rotate(str(i)):
                    count += 1
                return count
def rotate(self, n):
            if '4' in n or '7' in n or '3' in n:
                return False
            elif '2' in n or '5' in n or '6' in n or '9' in n:
                return True
            else:
                return None
