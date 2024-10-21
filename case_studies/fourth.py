import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:,.2f}'.format

# persona.csv dosyasını okutunuz ve veri seti ile
# ilgili genel bilgileri gösteriniz.
df = pd.read_csv('case_studies/persona.csv')
df.info()

# Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Kaç unique PRICE vardır?
df["PRICE"].nunique()

# Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Hangi ülkeden kaçar tane satış olmuş?
df.groupby("COUNTRY").agg({"PRICE": "count"})

# Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# SOURCE türlerine göre satış sayıları nedir?
df.groupby("SOURCE").agg({"PRICE": "count"})

# Ülkelere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE": "mean"})

# COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

# COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# Çıktıyı PRICE’a göre sıralayınız.
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

# Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df = agg_df.reset_index()

# Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
agg_df["AGE"].describe()

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
labels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]

agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=labels)

# Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df["Customers_Level_Based"] = [row[2].upper() + "_" + row[3].upper() + "_" + row[4].upper() + "_" + row[7].upper() for row in agg_df.values]
agg_df.info()

agg_df = agg_df[["Customers_Level_Based", "PRICE"]]
agg_df.head()

agg_df = agg_df.groupby("Customers_Level_Based").agg({"PRICE" : "mean"})
agg_df = agg_df.reset_index()

agg_df["SEGMENT"] = pd.cut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
