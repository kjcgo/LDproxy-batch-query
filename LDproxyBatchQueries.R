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
df <- read.table("combined_query_snp_list_grch37.txt", header=FALSE)
write.csv(df, "query_snp_list.csv", row.names=FALSE)
