library(LDlinkR)
snps <- readLines("rsIDs.txt")
LDproxy_batch(
  snps,
  pop = list("CEU", "TSI", "FIN", "GBR", "ASW", "CHB", "JPT", "CHS", "MXL", "PUR", "PEL", "CLM"),
  r2d = "r2", 
  token = Sys.getenv("LDLINK_TOKEN"),
  append = TRUE,
  genome_build = "grch37",
)