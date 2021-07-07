while(True):
    try:
        brightness = input("Please input brightness\n")
        if (brightness=="quit"):
            break
        brightness= int(brightness)

        with open("./brightness.txt","w") as file:
            file.write("manual," + str(brightness))
        file.close()
    except:
        print("invalid input")
        
