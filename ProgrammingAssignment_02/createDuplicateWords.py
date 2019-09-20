def main():
	f= open("duplicateWords.txt","w+")
	for i in range(80000000):
	     f.write("BigData")
	f.close()

main()