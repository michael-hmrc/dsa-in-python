
def factorial(n: int) -> int:
    def loop(i:int, acc: int) -> int:
        if i == 0: 
            return acc
        else: 
            return loop(i - 1, acc * i)
    return loop(n, 1)            



if __name__ == "__main__":
    print("Hello World")
    print(factorial(5))