#This R program creates a single csv file from a list of json files in the directory. This program selects the most relevant features
#and the features are labelled.
dir <- getwd()
dir <- paste(dir, "makeOneCSVFile.R",sep = "/")
source(dir)
dir <- getwd()
dir <- paste(dir, "functionCSV.R", sep = "/")
source(dir)
dir <- getwd()
dir <- paste(dir, "countWordInText.R", sep = "/")
source(dir)
jsonFilesNames <- list.files(getwd())
jsonFilesNames <- jsonFilesNames[grepl(".json",jsonFilesNames)]
lapply(jsonFilesNames, functionCSV)
csvFilesNames <- list.files(getwd())
csvFilesNames <- csvFilesNames[grepl(".csv",csvFilesNames)]
csvList <- sapply(csvFilesNames, read.csv, header = TRUE)
dataset <- makeOneCSVFile(csvList, 1, length(csvFileNames))
dataset <- dataset[, c("data.domain", "data.selftext_html","data.selftext","data.over_18","data.author", "data.score", "data.created_utc","data.title", "data.ups","data.num_comments", "data.subreddit","data.url", "data.permalink","data.thumbnail")]
title <- as.character.factor(dataset$data.title)
title <- tolower(title)
content <- as.character.factor(dataset$data.selftext)
content <- tolower(content)
domain <- as.character.factor(dataset$data.domain)
domain<- tolower(domain)
dataset$data.over_18 <- as.numeric(dataset$data.over_18)
lengthTitle <- lapply(title, nchar)
titleVar <- lengthTitle
dataset$titleLength <- unlist(titleVar)
lengthContent <- lapply(content, nchar)
contentVar <- lengthContent
dataset$contentLength <- unlist(contentVar)
names(dataset) <- gsub("data.", "", names(dataset))
write.csv(csvFile,"reddit_dataset.csv")