import import_tool
import os
import pandas as pd

file_pick = import_tool.csv_file
columns  = (file_pick.columns)

# printing the column names of the file
print(columns)

# selecting specific columns to display (for netflix_titles.csv, columns are country, release_year, and rating)
netflix_select_578 = (file_pick[[columns[5],columns[7],columns[8]]])
netflix_select_578.to_csv('subsets/netflix_select_578.csv', index = True, header  = True)

# subsetting all rows that have the 'country' column set to 'United States'
netflix_subset_US = (file_pick[file_pick['country'] == 'United States'])
netflix_subset_US.to_csv('subsets/netflix_subset_US.csv', index = True, header  = True)

# subsetting all rows for mulitple conditions: country, release_year, and rating
year = 2015
rating = 'R'
country = 'United States'

is_year = file_pick['release_year'] == year
is_rating = file_pick['rating'] == rating
is_country = file_pick['country'] == country
netflix_subset_US_2015_R_ = (file_pick[is_year & is_rating & is_country])
netflix_subset_US_2015_R_.to_csv('subsets/netflix_subset_US_2015_R_.csv', index = True, header  = True)


# subsetting all rows for multiple conditions using the isin() method: type, rating
rating = ['TV-MA','TV-PG','R']
typed = 'TV Show'

is_type = file_pick['type'] == typed
is_rating = file_pick['rating'].isin(rating)

netflix_subset_MAandPGandR_or_tv = (file_pick[is_type | is_rating])
netflix_subset_MAandPGandR_or_tv.to_csv('subsets/netflix_subset_MAandPGandR_or_tv.csv', index = True, header  = True)



