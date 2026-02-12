# Sample R code
install.packages("rlang")
install.packages(c("ggplot2", "readr", "GGally"))
library(readr)
library(ggplot2)
library(GGally)
groceries = read_csv("https://www.math.ntnu.no/emner/TMA4267/2026v/assignments/groceries.csv")
head(groceries)
ggpairs(groceries[,1:3])
