library(readr)
LMdata = read.csv("https://www.math.ntnu.no/emner/TMA4267/2026v/A6lmdataInfl.csv")
dim(LMdata); head(LMdata)

table(LMdata$group)
table(LMdata$group, LMdata$month)

plot(x = LMdata$month, y = LMdata$dep)

mod1 = lm(dep ~ predep + month*group, data = LMdata)
plot(mod1, 1)
plot(mod1, 2)
plot(mod1, 5)

LMdata_clean <- LMdata[-c(62, 63), ]
mod2 = lm(dep ~ predep + month*group, data = LMdata_clean)

plot(mod2, 1)
plot(mod2, 2)
plot(mod2, 5)
summary(mod2)


LMMdata <- read.csv("https://www.math.ntnu.no/emner/TMA4267/2026v/A6lmmdata.csv")
dim(LMMdata); head(LMMdata)
library(ggplot2)

ggplot(LMMdata, aes(x = month, y = dep, group = subject, color = factor(group))) +
geom_line() + geom_point()

avg_data <- aggregate(dep ~ month + group, data = LMMdata, FUN = mean)
ggplot(avg_data, aes(x = month, y = dep, group = group, color = factor(group))) +
geom_line() + geom_point()

library(lme4)
library(lmerTest)

mod3 = lmer(dep ~ predep + month*group + (1|subject), data = LMMdata)
summary(mod3)

predict(mod3, newdata = data.frame(predep = 20, month = 3, group = 0, subject = NA), re.form = NA)
