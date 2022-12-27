def valueCheckedInput(dtype, inputMessage="", cLimit=1000):
    dtypeList = [str, int, float, bool]
    count = 0
    while count < cLimit:
        if dtype in dtypeList:
            try:
                x = dtype(input(f"{inputMessage}"))
                return x
            except:
                count+=1
                continue
        else:
            return 0

x = valueCheckedInput(int, "input: ", 3)
print(x)
print(type(x))