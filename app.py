from fastapi import FastAPI

SECRET = "9ifewkjpmn0ij43t90j"

app = FastAPI()


def multiplicate(x: float, times: float, print_result: bool = False) -> float:
    if not print_result:
        return float(x) * float(times)
    print(eval("{}*{}".format(x, times)))


@app.get("/get-result")
async def get_result(x: float, times: float):
    return multiplicate(x, times)


def main():
    """
    To exploit, run python app.py and pass python variable or cmd as parameter, for example: __import__('os').system('date')

    Example usage:
    x = input("Pass first number:")
    y = input("Pass second number:")
    multiplicate(x, y, print_result=True)
    """
    raise NotImplementedError(
        "Use API with uvicorn: python -m uvicorn app:app --port 8000"
    )


if __name__ == "__main__":
    main()
