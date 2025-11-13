# Databricks notebook source
!pip install -r requirements.txt

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import utils; utils.db_setup('rel-amazon', 'amazon/amazon.db')

# COMMAND ----------

!ls -lrta /home/spark-d9e9a93b-2269-4670-89c6-7b/.cache/relbench/rel-amazon/

