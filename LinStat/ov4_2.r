X = matrix(c(1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1), nrow=8, ncol=3)
b = c(225, -30, 45)
Y = X %*% b + rnorm(8, 0, 10)
model = lm(Y ~ X[, 2:3])
summary(model)

b0 = c()
b1 = c()
b2 = c()
s2 = c()
for (i in 1:1000){
    Y = X %*% b + rnorm(8, 0, 10)
    m_ = lm(Y ~ X[, 2:3])
    s2[i] = (summary(m_)$sigma)^2
    b0[i] = m_$coefficients[1]
    b1[i] = m_$coefficients[2]
    b2[i] = m_$coefficients[3]
}

hist(b0)
