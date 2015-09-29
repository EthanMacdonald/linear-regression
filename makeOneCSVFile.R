makeOneCSVFile <- function(csvlist, indexA, indexB){
  csv <- csvlist[[indexA]]
  for (i in ((indexA + 1): indexB)){
    csv <- merge(csv, csvlist[[i]], all = TRUE)
  }
  return (csv)
}