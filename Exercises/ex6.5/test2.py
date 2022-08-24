print ("pick a number, 1 or 2")
for retry in range(5):
    a = int(input("> "))
    if a==1:
        print ("this")
        break
    if a == 2:
        print ("that")
        break
    print ("you have made an invalid choice, try again.")
else:
    print ("you keep making invalid choices, exiting.")
    sys.exit(1)
