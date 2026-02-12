library(readr)
library(ggplot2)
library(GGally)

groceries = read_csv("https://www.math.ntnu.no/emner/TMA4267/2026v/assignments/groceries.csv")

head(groceries)
ggpairs(groceries[,1:3])

ggplot(groceries, aes(y = turnover, x = as.factor(central))) + geom_boxplot()

groceries$log_distance = log(groceries$distance)
model1 = lm(turnover ~ population + log_distance, data = groceries)
summary(model1)
model2 = lm(turnover ~ population + log_distance + central*mall, data = groceries)

