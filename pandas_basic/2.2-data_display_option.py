import pandas as pd

# in jupyter notebook, you can use the following command to display all columns of a DataFrame
display_max_columns = "display.max_columns"
print(display_max_columns)
print(pd.get_option(display_max_columns))
pd.set_option(display_max_columns, None)
print(pd.get_option(display_max_columns))
pd.set_option(display_max_columns, 60)
print(pd.get_option(display_max_columns))

display_width = "display.width"
print(display_width)
print(pd.get_option(display_width))
pd.set_option(display_width, 100)
print(pd.get_option(display_width))

# display.max_columns
# 0
# None
# 60
# display.width
# 80
# 100
