f = open("demofile.txt", "a")
f.write("we are developing as programmers. \n this is the first file we are creating. totally impressive")
f.close
f = open("demofile.txt", "r")
print(f.read())