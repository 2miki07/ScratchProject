import matplotlib.pyplot as plt
import numpy as np
from datetime import date


def func(x):
    return x**2 * np.sin(x)


def main():
    today = date.today()

    print('This is a test for a repository')
    print("Today's date is", today)

    x = np.linspace(-20, 20, 200)
    y = func(x)

    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
