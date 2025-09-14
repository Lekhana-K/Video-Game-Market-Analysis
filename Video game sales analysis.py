import pandas as pd
df=pd.read_csv("C:\\Users\\Lekhana K\\Desktop\\practice\\CAPSTONE PROJECT\\vgsales.csv");

#What kind of games (genres) are most popular in terms of units sold
# Group by genre
genre_sales = df.groupby("Genre")
grouped=genre_sales["Global_Sales"].sum().sort_values(ascending=False)

print("Most popular genres (by Global Sales):")
#to check all-print(grouped)
#Top 5 games
print(grouped.head(5))


#What are the most commonly used gaming platforms (PS4, Xbox, PC, etc.)?
# Group by genre
genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)

print("Most popular genres (by Global Sales):")
print(genre_sales)

# top 5 genres
print(genre_sales.head(5))

#Are the number of buyers increasing in the long run?
yearly_sales = df.groupby("Year")["Global_Sales"].sum()

print("Global sales trend over the years:")
print(yearly_sales)

#Which publishers dominate the market?
publisher_sales = df.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False)

print("Top 5 publishers by Global Sales:")
print(publisher_sales.head(5))

