import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("NetflixOriginals.csv",encoding="utf-8",encoding_errors="ignore",index_col=False)




#check if there is nan value
#print(df.isnull().sum())

#fill nan values
df[["Premiere","Language"]]=df[["Premiere","Language"]].fillna(value="Unknown")

df[["Score","Runtime"]]=df[["Score","Runtime"]].fillna(value=df["Score"].median())

#Change date format 
df["Premiere"]=pd.to_datetime(df["Premiere"],errors="coerce")

#Calculations

AverageRuntime=round(df["Runtime"].mean(),2)
MedianRuntime=round(df["Runtime"].median(),2)
AverageScore=round(df["Score"].mean(),2)
MedianScore=round(df["Score"].median(),2)

#Movie with max runtime
maxruntime=round(df["Runtime"].max())
maxruntimemovie=df[df["Runtime"]==maxruntime]["Title"].tolist()[0]
print("Movie with max runtime:",maxruntimemovie,"-->",maxruntime)


#Movie with min runtime
minruntime=round(df["Runtime"].min())
minruntimemovie=df[df["Runtime"]==minruntime]["Title"].tolist()[0]
print("Movie with min runtime:",minruntimemovie,"-->",minruntime)

#Longest title
Longesttitle=""
for title in df["Title"].tolist():
    if len(title)>len(Longesttitle):
        Longesttitle=title
print("Longest movie name is:",Longesttitle)


#Oldest movie
oldest=df["Premiere"].min()
oldestmovie=df[df["Premiere"]==oldest]["Title"].tolist()[0]

print("Oldest movie is:",str(oldest.strftime("%Y-%m-%d")),oldestmovie)


#How many Indıan movies

Indians=len(df[df["Language"]=="Hindi"])
print(Indians,"Indian movies")

#Most used genre


MostGenrevalue=df["Genre"].mode()[0]
MostGenre=df["Genre"].value_counts()[MostGenrevalue]
print("Most used genre is:",MostGenrevalue,MostGenre)


###Labeling some values
#If 0<Score<4 Bad, 4<Score<7 Nice, 7<Score<10 Perfect. New column.

df["Evaluate"]=pd.cut(df["Score"],
            bins=[0,4,7,10],
            labels=["Bad","Nice","Perfect"])
# print(df.head())



#Creating new column df["Year"]

df["Year"]=df["Premiere"].dt.strftime("%Y")
print(df.head())


# Visualization
fig,axes=plt.subplots(1,2,figsize=(16,6))


x1=df["Genre"].value_counts().head().index
y1=df["Genre"].value_counts().head().values

axes[0].bar(x1,y1,color="red")
axes[0].set_xlabel("Genres",color="blue",size=25)
axes[0].set_ylabel("Frequency",color="blue",size=25)
axes[0].set_title("Top 5 Genres",color="blue",size=25)



x2=df["Year"].value_counts().head().index
y2=df["Year"].value_counts().head().values
axes[1].bar(x2,y2,color="red")
axes[1].set_xlabel("Years",color="blue",size=25)
axes[1].set_ylabel("Frequency",color="blue",size=25)
axes[1].set_title("Top 5 Years",color="blue",size=25)
plt.show()















