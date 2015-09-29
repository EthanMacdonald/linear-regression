

#jsonData3<- fromJSON("t3_3l901y.json", flatten = TRUE)
#jsonData4 <- jsonData3$data$children
#jsonData4 <- jsonData4[,lapply(jsonData4,class)!= "list"]
#lengthTrainingM <- dim(jsonData4)[1]
#jsonData4 <- jsonData4[,lapply(jsonData4,length) == lengthTrainingM]

functionCSV <-  function(fileNameJSON){
  library(jsonlite)
  jsonData3<- fromJSON(fileNameJSON, flatten = TRUE)
  jsonData4 <- jsonData3$data$children
  jsonData4 <- jsonData4[,lapply(jsonData4,class)!= "list"]
  lengthTrainingM <- dim(jsonData4)[1]
  jsonData4 <- jsonData4[,lapply(jsonData4,length) == lengthTrainingM]
  csvName <- sub(".json",".csv",fileNameJSON)
  write.csv(jsonData4,csvName)
  print(dim(jsonData4[1]))
  print(dim(jsonData4[2]))
  
  
  
}
