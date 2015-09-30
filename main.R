#This R program creates a single csv file from a list of json files in the directory. This program selects the most relevant features
#and the features are labelled.
dir <- getwd()
dir <- paste(dir, "makeOneCSVFile.R",sep = "/")
source(dir)
dir <- getwd()
dir <- paste(dir, "functionCSV.R", sep = "/")
source(dir)
jsonFilesNames <- list.files(getwd())
jsonFilesNames <- jsonFilesNames[grepl(".json",jsonFilesNames)]
lapply(jsonFilesNames, functionCSV)
csvFilesNames <- list.files(getwd())
csvFilesNames <- csvFilesNames[grepl(".csv",csvFilesNames)]
csvList <- sapply(csvFilesNames, read.csv, header = TRUE)
dataset <- makeOneCSVFile(csvList, 1, length(csvFileNames))

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
dataset$numWordsInTitle <- unlist(sapply(gregexpr("\\W+", dataset[,"title"]), length)+1)
dataset$self <- as.numeric(!is.na(dataset[,"selftext_html"]))

dataset$elapsedTime <- difftime(as.POSIXct(dataset$scrape_time_utc, tz = "UTC", origin = "1970-01-01"),as.POSIXct(dataset$created_utc, tz = "UTC", origin = "1970-01-01"), units = "secs")

write.csv(csvFile,"reddit_dataset.csv")

trainingandTestDataset <- final[, c("title", "over_18", "num_comments","self","titleLength","contentLength","numWordsInTitle","elapsedTime","score")]
