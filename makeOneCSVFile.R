#This function takes as input a list "csvlist" which represents a list of data frames, corresponding to csv data, and indexes "indexA" 
#and "indexB" are indexes of the list "csvlist". The function outputs a merged data frame "csv" containing all the data from "indexA" to "indexB"
#in the csvlist.
makeOneCSVFile <- function(csvlist, indexA, indexB){
  csv <- csvlist[[indexA]]
  for (i in ((indexA + 1): indexB)){
    csv <- merge(csv, csvlist[[i]], all = TRUE)
  }
  return (csv)
}
