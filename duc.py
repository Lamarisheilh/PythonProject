import duckdb

result = duckdb.sql("SELECT 42 AS answer").fetchall()
print(result)
