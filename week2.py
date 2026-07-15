import pandas as pd
import matplotlib.pyplot as plt

# FIXED: Added safe encoding to handle mixed character text in global descriptions
try:
    df = pd.read_csv("netflix_titles.csv", encoding='utf-8')
    print("Loaded with UTF-8 encoding.")
except UnicodeDecodeError:
    df = pd.read_csv("netflix_titles.csv", encoding='latin1')
    print("Loaded with Latin-1 encoding fallback.")

print("First 5 Records")
print(df.head())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInformation")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

df = df.drop_duplicates()

df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["rating"] = df["rating"].fillna("Not Rated")

# FIXED: Strip hidden spaces from date strings so pd.to_datetime works cleanly
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors='coerce')

print("\nSummary Statistics")
print(df.describe(include="all"))

print("\nMovies and TV Shows")
print(df["type"].value_counts())

movies = df[df["type"] == "Movie"]
tvshows = df[df["type"] == "TV Show"]

print("\nNumber of Movies :", len(movies))
print("Number of TV Shows :", len(tvshows))

print("\nTop 10 Countries")
print(df["country"].value_counts().head(10))

print("\nTop 10 Ratings")
print(df["rating"].value_counts().head(10))

print("\nTop 10 Release Years")
print(df["release_year"].value_counts().head(10))

print("\nTop Directors")
print(df["director"].value_counts().head(10))

print("\nOldest Movies")
print(df.sort_values("release_year").head(10)[["title","release_year"]])

print("\nLatest Movies")
print(df.sort_values("release_year",ascending=False).head(10)[["title","release_year"]])

recent = df[df["release_year"] >= 2020]

print("\nReleased after 2020")
print(len(recent))

india = df[df["country"].str.contains("India",case=False,na=False)]

print("\nContent from India")
print(len(india))

usa = df[df["country"].str.contains("United States",case=False,na=False)]

print("\nContent from USA")
print(len(usa))

family = df[df["listed_in"].str.contains("Children|Family",case=False,na=False)]

print("\nFamily Content")
print(len(family))

action = df[df["listed_in"].str.contains("Action",case=False,na=False)]

print("\nAction Content")
print(len(action))

rating_count = df["rating"].value_counts()

plt.figure(figsize=(8,5))
rating_count.plot(kind="bar")
plt.title("Content Rating")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

type_count = df["type"].value_counts()

plt.figure(figsize=(5,5))
type_count.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Movies vs TV Shows")
plt.tight_layout()
plt.show()

country = df["country"].value_counts().head(10)

plt.figure(figsize=(10,5))
country.plot(kind="bar")
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

years = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
years.plot()
plt.title("Content Released by Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# IMPROVED: Exclude 'Unknown' from the visualization so actual top directors are shown
actual_directors = df[df["director"] != "Unknown"]["director"].value_counts().head(10)

plt.figure(figsize=(10,5))
actual_directors.plot(kind="bar")
plt.title("Top 10 Actual Directors")
plt.xlabel("Director")
plt.ylabel("Titles")
plt.tight_layout()
plt.show()

movies_per_year = movies.groupby("release_year").size()

plt.figure(figsize=(10,5))
movies_per_year.plot()
plt.title("Movies Released Every Year")
plt.xlabel("Year")
plt.ylabel("Movies")
plt.tight_layout()
plt.show()

tv_per_year = tvshows.groupby("release_year").size()

plt.figure(figsize=(10,5))
tv_per_year.plot(color="red")
plt.title("TV Shows Released Every Year")
plt.xlabel("Year")
plt.ylabel("TV Shows")
plt.tight_layout()
plt.show()

genre = df["listed_in"].str.split(",").explode().str.strip()
top_genre = genre.value_counts().head(10)

print("\nTop Genres")
print(top_genre)

plt.figure(figsize=(10,5))
top_genre.plot(kind="bar")
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Titles")
plt.tight_layout()
plt.show()

summary = pd.DataFrame({
    "Total Records":[len(df)],
    "Movies":[len(movies)],
    "TV Shows":[len(tvshows)],
    "Countries":[df["country"].nunique()],
    "Directors":[df["director"].nunique()]
})

summary.to_csv("netflix_summary.csv",index=False)
df.to_csv("cleaned_netflix.csv",index=False)

print("\nSummary")
print(summary)

print("\nProject Completed Successfully")
