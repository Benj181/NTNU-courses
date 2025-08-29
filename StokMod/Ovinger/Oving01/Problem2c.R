# Task (c): simulate and verify parts (a) and (b)

set.seed(1)

# Parameters
lambda <- 6
mu     <- -2
sigma  <- 1
B      <- 2e6   # years to simulate

# Analytic results from (a)
mu_c  <- exp(mu + 0.5 * sigma^2)
var_c <- exp(2*mu + sigma^2) * (exp(sigma^2) - 1)

# Analytic results from (b)
E_S   <- lambda * mu_c
Var_S <- lambda * (var_c + mu_c^2)

# ---- Verify (a) by direct simulation of claim sizes ----
M <- 5e6
Ci <- rlnorm(M, meanlog = mu, sdlog = sigma)
cat(sprintf("Ci mean: analytic=%.6f  empirical=%.6f rel diff=%.6f \n", mu_c,  mean(Ci), abs(mu_c-mean(Ci))/mu_c)) 
cat(sprintf("Ci var : analytic=%.6f  empirical=%.6f, rel diff=%.6f\n\n", var_c, var(Ci), abs(var_c-var(Ci))/var_c))

# ---- Simulate B years for (b) ----
N <- rpois(B, lambda)                        # number of claims per year
tot_claims <- sum(N)

S <- numeric(B)                              # total claim per year
if (tot_claims > 0) {
  claims <- rlnorm(tot_claims, mu, sigma)   # all claims across all years
  grp    <- rep.int(seq_len(B), N)           # year index for each claim
  rs     <- rowsum(claims, grp, reorder = FALSE)
  S[as.integer(rownames(rs))] <- rs[, 1]     # fill, zeros stay for years with N=0
}

# ---- Compare empirical to analytic ----
cat(sprintf("Total S mean: analytic=%.6f  empirical=%.6f\n", E_S, mean(S)))
cat(sprintf("Total S var : analytic=%.6f  empirical=%.6f\n", Var_S, var(S)))
