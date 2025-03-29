import sys

counter = 0

if len(sys.argv)>1:
    source = sys.argv[1]
    if source == "-f":
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            source = f.read()
    for i in source:
        if i == "P":
            print("안녕 난 뽀로로야!", end=" ")
        elif i == "Q":
            print(source, end="")
        elif i == "9":
            for j in range(99, 0, -1):
                if j == 1:
                    print(f"1 friend of Pororo in playground, 1 friend of Pororo.\nA friend went to bed, no more firends of Pororo in playground.\n\nNo more friends of Pororo in playground, no more friends of Pororo.\nWent to bed and slept until morning, 99 friends in playground.")
                    break
                print(f"{j} friends of Pororo in playground, {j} friends of Pororo.\nOne of the friends went to bed, {j-1} friends of Pororo in playground.")
        elif i == "+":
            counter+=1
else:
    print("Please enter the source code")