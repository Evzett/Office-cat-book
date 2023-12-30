import time
import sys


def animate(k):
    for _ in range(k // 2):
        sys.stdout.write("\rВыполнение почасовой работы ⢿")
        time.sleep(0.1)
        sys.stdout.write("\rВыполнение почасовой работы ⣻")
        time.sleep(0.1)
        sys.stdout.write("\rВыполнение почасовой работы ⣽")
        time.sleep(0.1)
        sys.stdout.write("\rВыполнение почасовой работы ⣾")
        time.sleep(0.1)
