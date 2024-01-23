SECRET = "9ifewkjpmn0ij43t90j"

def multiplicate(x: float, times: float, print_result: bool = False) -> float:
    if not print_result:
        return
        # return float(x) * float(times)
    print(eval('{}*{}'.format(x, times)))


def main():
    """
    To exploit, run python app.py and pass python variable or cmd as parameter, for example: __import__('os').system('date')
    """
    x = input("Pass first number:")
    y = input("Pass second number:")
    multiplicate(x, y, print_result=True)

if __name__ == "__main__":
    main()


