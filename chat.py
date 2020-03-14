
def read_file(filename):
	records = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			records.append(line.strip())
	return records

def convert(records):
	new = []
	person = None #如果對話紀錄開始第一行不是人名，程式會crash，所以先做變數宣告
	for line in records:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:#檢查person變數都不是Allen或Tom，就使用預設值None
			new.append(person + ':' + line)
	return new

def write_file(filename, converted):
	with open(filename, 'w') as f:
		for line in converted:
			f.write(line + '\n')

def main():
	records = read_file('input.txt')
	converted = convert(records)
	write_file('output.txt', converted)

main()