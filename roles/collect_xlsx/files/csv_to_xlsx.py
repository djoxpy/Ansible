import pandas as pd
import sys


try:
    assert str(sys.argv[-2]).endswith(".csv")
    assert str(sys.argv[-1]).endswith(".xlsx")
    assert len(sys.argv) == 3

except AssertionError:
    print("Wrong args")
    sys.exit()

read_file_product = pd.read_csv(sys.argv[-2], sep=';')
read_file_product.to_excel(sys.argv[-1], index=None, header=True)

print("Success!")
