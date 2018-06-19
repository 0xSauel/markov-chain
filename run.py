from fetch_data import print_data

while True:
    option = raw_input("Generate story? (y/n) ").lower()
    if option == "y":
        print "Generating story..."
        try:
            print_data()
        except:
            try:
                print_data()
            except:
                try:
                    print_data()
                except:
                    print "Error. Try again."
    elif option == "n":
        print "Exiting..."
        break
    else:
        break