import pandas as pd
from pandas import read_parquet
from datetime import datetime
from icecream import ic
ic.configureOutput(prefix=lambda: datetime.now().strftime('%y-%m-%d %H:%M:%S | '),
                   includeContext=False)

data = read_parquet("assets/metadata_0.parquet")
ic(data.count())
print(data.head())
