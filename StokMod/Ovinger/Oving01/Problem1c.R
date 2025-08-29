set.seed(42)
N <- 1e6

# Helper: make flips given which trials use the biased coin
flip_once <- function(is_biased) {
  # biased -> always heads; fair -> heads with prob 0.5
  ifelse(is_biased, TRUE, runif(length(is_biased)) < 0.5)
}

# --- 1a: one flip ---
is_biased_1 <- runif(N) < 0.5                # pick coin at random
H1 <- flip_once(is_biased_1)                 # one flip outcome
p_biased_given_H <- sum(is_biased_1 & H1) / sum(H1)

# --- 1b: two flips ---
is_biased_2 <- runif(N) < 0.5
H2a <- flip_once(is_biased_2)
H2b <- flip_once(is_biased_2)
both_H <- H2a & H2b
p_biased_given_HH <- sum(is_biased_2 & both_H) / sum(both_H)

cat(sprintf("P(biased | H)  ≈ %.5f  (theory: 2/3 = 0.66667)\n", p_biased_given_H))
cat(sprintf("P(biased | HH) ≈ %.5f  (theory: 0.8)\n",             p_biased_given_HH))
