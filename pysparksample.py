from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Crie uma SparkSession
spark = SparkSession.builder \
    .appName("Simple PySpark Example") \
    .getOrCreate()

# Leia o arquivo CSV
df = spark.read.csv("example.csv", header=True, inferSchema=True)

# Mostre o DataFrame original
print("DataFrame Original:")
df.show()

# Selecione colunas específicas
df_selected = df.select("name", "age")

# Filtre linhas onde a idade é maior que 30
df_filtered = df_selected.filter(col("age") > 30)

# Mostre o DataFrame transformado
print("DataFrame Transformado:")
df_filtered.show()

# Pare a SparkSession
spark.stop()
