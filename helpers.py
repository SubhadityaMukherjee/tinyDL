def pbar(iterable, length=50,listofextra = [], prefix='', suffix='', decimals=1, fill='█', printEnd="\r"):
    total = len(iterable)
    listofextra = " ".join(listofextra)

    def printPbar(iteration):
        percent = ("{0:." + str(decimals)+"f}").format(100 *
                                                       (iteration/float(total)))
        filledLength = int(length*iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% | {listofextra} {suffix}', end=printEnd)

    printPbar(0)
    for i, item in enumerate(iterable):
        yield item
        printPbar(i+1)

    print()

def pretty(arch):
    print(f"Number of layers -> ", len(arch))
    temp = ""
    for j,i in enumerate(arch):
        temp += f"{j}) {i['name']} : {i['input_dim']} -> {i['output_dim']} , {i['activation']}\n"
    print(temp)
    return temp
