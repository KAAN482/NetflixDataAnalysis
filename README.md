This project is conducted to analyze the Netflix Originals dataset. The analysis includes data cleaning, basic statistical calculations, categorical data labeling, and visualization. The dataset contains information about Netflix original titles, genres, languages, ratings, runtimes, and premiere dates.

Project Content
1. Data Cleaning:
Missing (NaN) values have been filled.
The "Premiere" column has been converted into a datetime format.
Missing values in the "Language" column were filled with "Unknown".
2. Statistical Calculations:
Mean and median runtime and ratings have been calculated.
The movie with the maximum and minimum runtime has been identified.
The longest title and the oldest movie have been found.
3. Categorical Data Labeling:
A new column ("Evaluate") has been created based on movie ratings:
0-4: Bad
4-7: Nice
7-10: Perfect
4. Visualization:
The top 5 genres and the distribution of movies by year have been visualized.
Bar charts were used to show the most popular genres and years.
Libraries Used
Pandas: Used for data analysis and manipulation.
Matplotlib: Used for data visualization.

Dataset
The dataset contains information about Netflix Originals. The following columns are included in the dataset:

Title: Movie or series title.
Premiere: Release date.
Genre: Genre.
Language: Language.
Score: Rating (on a scale from 1 to 10).
Runtime: Duration (in minutes).
Usage
Requirements:
Python 3.x
Pandas
Matplotlib


