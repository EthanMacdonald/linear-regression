makeOneCSVFile <- function(csvList, indexA, indexB) {


    mergedCSV1 <- csvList[[indexA]]
    for(i in (indexA+1):indexB){
      mergedCSV1 <- merge(mergedCSV1, csvList[[i]], all = TRUE)
    }
    return(mergedCSV1)
}