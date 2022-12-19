import os
import pandas as pd
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../keys/credentials.json'
project_id = 'mpg-wildlife-tracking'

client = bigquery.Client(project=project_id)

sql_query = """
  SELECT *
  FROM `mpg-wildlife-tracking.coyotes.main`
"""

df = pd.read_gbq(sql_query, project_id=project_id)

df.head()