speed = int(input("enter the speed"))
for speed in range(0, 200):
    if speed < 70:
        print("ok")
        for speed in range(70,200,5):
            if 70 < speed <= 75:
                points = "1"
                print("points", points)
            elif 75 < speed <=80:
                points = "2"
                print("points", points)
                if points > 12:
                    print("license suspended")
            
                
        
            
            
    
