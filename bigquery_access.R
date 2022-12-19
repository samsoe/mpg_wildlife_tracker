library(DBI)
library(dplyr)

con <- dbConnect(
  bigrquery::bigquery(),
  project = "mpg-wildlife-tracking",
  dataset = "coyotes",
  billing = "mpg-wildlife-tracking"
)

df <- tbl(con, "main")

df %>% head(n = 4)