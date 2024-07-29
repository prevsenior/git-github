# %%
from pyspark.sql import SparkSession

# Inicializa a sessão Spark com configurações básicas
spark = SparkSession.builder \
    .appName("ExemploPySpark") \
    .config("spark.master", "local[*]") \
    .getOrCreate()

# Imprime uma mensagem
print("Hello")

# Cria um DataFrame simples
data = [("Alice", 30), ("Bob", 25), ("Cathy", 29)]
columns = ["Nome", "Idade"]

df = spark.createDataFrame(data, columns)

# Mostra o DataFrame
df.show()

# Para encerrar a sessão Spark
spark.stop()


# %%
