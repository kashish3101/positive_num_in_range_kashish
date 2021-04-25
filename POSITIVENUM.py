#PYTHON PG TO PRINT POSITIVE NUM IN A GIVEN RANGE
start = int(input(" ENTER THE START OF THE NUMBERS IN YOUR RANGE"))
end = int(input(" ENTER THE END OF THE NUMBERS IN YOUR RANGE"))
#using for loop iteration
for num in range (start,end + 1):
    if num >= 0:
        print (num , end=" ")
