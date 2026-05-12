import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

schools = pd.read_csv("datalab_export_2026-05-12 05_39_57.csv")

schools = schools.fillna(0, inplace=True)

#beginning of analysis
# to find which schools have the best math results;
best_math_schools = schools[schools["average_math"] > 640][["school_name", "average_math"]].sort_values("average_math", ascending=False).reset_index(drop=True)

#What are the top 10 performing schools based on the combined SAT scores?
schools["total_SAT"] = schools["average_math"] + schools["average_reading"] + schools["average_writing"]
top_10_schools = schools[["school_name", "total_SAT"]].sort_values("total_SAT", ascending=False).head(10).reset_index(drop=True)

#Which single borough has the largest standard deviation in the combined SAT score?
borough = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
largest_std_dev = borough[borough["std"] == borough["std"].max()]
largest_std_dev = largest_std_dev.rename(columns = {"count": "num_schools", "mean": "average_SAT", "std": "std_SAT" })
largest_std_dev.reset_index(inplace=True)

#view each results

print("\nSchools with the best math results:")
print(best_math_schools)
print("\nTop 10 performing schools based on combined SAT scores:")
print(top_10_schools)
print("\nBorough with the largest standard deviation in combined SAT scores:")
print(largest_std_dev)
