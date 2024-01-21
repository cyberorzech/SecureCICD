
def multiplicate(x: float, times: float, print_result: bool = False) -> float:
    if not print_result:
        return x * times
    print(eval('x * times'))
    

def main():
    res = multiplicate(1.5, times=4)
    print(f"Safe func run: {res}")
    print("Unsafe func run: ", end="")
    multiplicate(1.5, times=4, print_result=True)

if __name__ == "__main__":
    main()