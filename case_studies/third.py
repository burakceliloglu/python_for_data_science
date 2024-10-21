import pandas as pd
df = pd.read_excel('case_studies/miuul_gezinomi.xlsx')
pd.set_option('display.max_columns', 500)

def dataframe_summary(dataframe):
    print("#################### First 5 data ####################")
    print(dataframe.head())
    print("######################## Shape #######################")
    print(dataframe.shape)
    print("##################### Data Types #####################")
    print(dataframe.dtypes)
    print("####################### Info #######################")
    print(dataframe.info())

dataframe_summary(df)

# Unique Değerler ve Freanksları
df["SaleCityName"].nunique()
df["SaleCityName"].value_counts()
df.groupby("SaleCityName").size()

# Unique Concept İsimleri ve Satış Adetleri
df["ConceptName"].nunique()
df.groupby("ConceptName").size()

# Şehirlere göre toplam satış
pd.options.display.float_format = '{:,.2f}'.format
df.groupby("SaleCityName").agg({"Price": "sum"})

# Concept'e göre ne kadar kazanılmış
df.groupby("ConceptName").agg({"Price": "sum"})

df.groupby("SaleCityName").agg({"Price": "mean"})

df.groupby("ConceptName").agg({"Price": "mean"})

df.groupby(["ConceptName", "SaleCityName"]).agg({"Price": "mean"})

#SaleCheckInDayDiff'i kategorik dğeişkene çevir
bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins=bins, labels=labels)

# Şehir-Concept-EB Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında
# ortalama ödenen ücret ve yapılan işlem sayısı cinsinden
# inceleyiniz ?
df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price": ["mean","count"]})
df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": ["mean","count"]})
df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price": ["mean","count"]})

agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending=False)
agg_df.head()

agg_df.reset_index(inplace=True)

agg_df["Sales_Level_Based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis=1)

agg_df["Segment"] = pd.qcut(agg_df["Price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("Segment").agg({"Price": ["mean", "max", "sum"]})

df.info()
