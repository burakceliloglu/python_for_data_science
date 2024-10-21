#1
import seaborn as sns
import pandas as pd
df = sns.load_dataset("car_crashes")
pd.set_option('display.max_columns', None)
["NUM_" + col.upper() if df[col].dtype!="O" else col.upper() for col in df.columns]

df.dtypes

#2
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

#3
og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
df_new = df[new_cols]
df_new.head()

#4
df_titanic = sns.load_dataset("titanic")
pd.set_option('display.max_columns', None)
df_titanic["sex"].value_counts()
df_titanic.nunique()
df_titanic["pclass"].nunique()
df_titanic[["pclass","parch"]].nunique()
df_titanic["embarked"] = df_titanic["embarked"].astype("category")
df_titanic[df_titanic["embarked"] == "C"].head()
df_titanic[df_titanic["embarked"] != "S"].head()
df_titanic.loc[(df_titanic["age"] < 30) & (df_titanic["sex"] == "female"), :].head()
df_titanic[(df_titanic["fare"] > 500) | (df_titanic["age"] > 70)].head()
df_titanic.isnull().sum()
df_titanic.drop("who", axis=1, inplace=True)
df_titanic["deck"].fillna(df_titanic["deck"].mode()[0], inplace=True)
# .mode() yapınca pandas series oluyor. bundan dolayı 0. indextekini alıyoruz.
df_titanic["age"].fillna(df_titanic["age"].median())
df_titanic.groupby(["pclass", "sex"]).agg({"survived" : ["sum", "count", "mean"]})
df_titanic["age_flag"] = df_titanic["age"].apply(lambda x: 1 if x > 30 else 0)
df_tips = sns.load_dataset("tips")
df_tips.groupby("time").agg({"total_bill": ["sum", "mean", "max", "mean"]})
df_tips.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})
(df_tips[(df_tips["sex"] == "Female") & (df_tips["time"] == "Lunch")]
 .groupby("day").agg({"total_bill" : ["sum", "mean", "max", "mean"],
           "tip" : ["sum", "mean", "max", "mean"]}))
df_tips.loc[(df_tips["size"] < 3) & (df_tips["total_bill"] > 10), "total_bill"].mean()
df_tips["total_bill_tip_sum"] = df_tips["total_bill"] + df_tips["tip"]
df_new = df_tips.sort_values("total_bill_tip_sum", ascending=False)[0:30]
df_new.head()