# 逆向最大匹配

class IMM():
	def __init__(self,dic_path):
		self.dictionary = set()
		self.maximum = 0
		# read word dict
		with open(dic_path,"r",encoding='utf-8') as f:
			for line in f:
				line = line.strip()
				if not line:
					continue
				self.dictionary.add(line)
				self.maxinum = len(line)

	def cut(self,text):
		result = []
		index = len(text)
		while index > 0:
			word = None
			for size in range(self.maximum,0,-1):
				if index - size < 0:
					continue
				piece = text[(index-size):index]
				if piece in self.dictionary:
					word = piece
					result.append(word)
					index -= size
					break
				if word is None:
					index -= 1

		return result[::-1]


def main():
	text = '南京市长江大桥'
	tokenizer = IMM("your word dictionary path,must utf-8 encode")
	print(tokenizer.cut(text))

# 可以根据IMM自己写出MM的算法和双向最大匹配算法