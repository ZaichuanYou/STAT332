data_files <- list.files("C:/Users/21995/Desktop/Math/Stat332/Final project/STAT332/Data")
names <-list()
for (x in 1:length(data_files)) {
  name <- data_files[x]
  if (substring(name, nchar(name)-6, nchar(name)) != "adj.csv"){
    assign(substring(name, 0, nchar(name)-4),
         read.csv(paste0("C:/Users/21995/Desktop/Math/Stat332/Final project/STAT332/Data/", data_files[x])))
    names <- append(names, substring(name, 0, nchar(name)-4))
  }
}

for (x in 1:length(names)){
  data <- get(names[x])
  result <- sum(data$high-data$low)
  print(result)
}


