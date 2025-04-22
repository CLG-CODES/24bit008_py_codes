def tester():
    inp=input("Pls give the value:");
    try:
        int(inp);
    except:
        print("Only Integer Values Are Allowed.");
        tester();
tester();