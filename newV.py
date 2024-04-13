import pickle

while True:
    print("")
    print("1.read the matrix")
    print("2.delete a matrix")
    print("3.delete all matrix")
    print("4.insert new matrix")
    print("5.exit")
    print("")
    y = int(input("input:"))
    print("")
    if y == 1:
        n = 0
        with open("mybinary.dat","rb") as file:
            while True: 
                try:
                    n+=1
                    inp = pickle.load(file)
                    print("MATRIX"+str(n)+":")
                    i = [print(i) for i in inp]
                    print("")

                except:
                    break
    elif y == 1:
        num = int(input("enter the matrix to delete:"))

        #reading
        out = []
        with open("mybinary.dat","rb") as file:
            while True: 
                try:
                    inp = pickle.load(file)
                    out.append(inp)
                except:
                    break

        #writing
        with open("mybinary.dat","wb") as file:
            for i in range(len(output)):
                if i+1 != num:
                    pickle.dump(output[i])

    elif y == 3:
        if input("are you sure(Y/N)") == "Y":
            with open("mybinary.dat","wb") as file:
                pass

    elif y == 4:
        mat = []
        for i in range(int(input("number of rows:"))):
            row = eval(input("enter the row:"))
            mat.append(row)

        with open("mybinary.dat","ab") as file:
            pickle.dump(mat,file)

    elif y == 5:
        break
    else:
        print("invalid input")
