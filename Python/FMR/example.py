```python
import functional


def CheckEven(no):
    return no % 2 == 0


def Increment(no):
    return no + 1


def Addition(no1, no2):
    return no1 + no2


def main():
    Data = [1, 2, 3, 4, 5, 6]

    Ret = functional.filterX(CheckEven, Data)
    print("Filter :", Ret)

    Ret = functional.mapX(Increment, Data)
    print("Map    :", Ret)

    Ret = functional.reduceX(Addition, Data)
    print("Reduce :", Ret)


if __name__ == "__main__":
    main()
```
