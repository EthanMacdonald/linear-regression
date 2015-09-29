

functionCSV <-  function(fileNameJSON){
  library(jsonlite)
  jsonData3<- fromJSON(fileNameJSON, flatten = TRUE)
  jsonData5 <- jsonData3$data$children
  jsonData5 <- jsonData5[,lapply(jsonData5,class)!= "list"]
  lengthTrainingM <- dim(jsonData5)[1]
  jsonData5 <- jsonData5[,lapply(jsonData5,length) == lengthTrainingM]
 
 
  csvName <- sub(".json",".csv",fileNameJSON)
  write.csv(jsonData5,csvName)
  

  
  
  
}
