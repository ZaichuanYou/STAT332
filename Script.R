options(scipen=999)
set.seed(42)



data_files <- list.files("C:/Users/21995/Desktop/Math/Stat332/Final project/STAT332/Data")
names <- c()
for (x in 1:length(data_files)) {
  name <- data_files[x]
  if (substring(name, nchar(name)-6, nchar(name)) != "adj.csv"){
    assign(substring(name, 0, nchar(name)-4),
         read.csv(paste0("C:/Users/21995/Desktop/Math/Stat332/Final project/STAT332/Data/", data_files[x])))
    names <- c(names, substring(name, 0, nchar(name)-4))
  }
}

vola <- c()
for (x in 1:length(names)){
  data <- get(names[[x]])
  result <- sum(data$high/7-data$low/7)
  format(result, scientific = F)
  vola <- c(vola, result)
}

print(vola)
plot(factor(names), vola)


