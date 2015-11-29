setwd('/home/sumitkhanna/applift')
getwd()

## the script to basically partition the 1GB data, acc. to 
## arguments like 'traffictype - app / site" | appsiteid | appsitecategory | campaignid

# data_1gb <- read.csv('dataset_1gb.csv',header=F)
# colnames(data_1gb) <- c("bidid","traffictype","publisherid","appsiteid","appsitecategory","position","bidfloor","timestamp","age","gender","os","osvrsn","model","manufacturer","carrier","devicetype","deviceid","deviceip","country","lat","long","zipcode","geotype","campaignid","creativeid","Creativetype","creativecategory","exchangebid","outcome")

vec_t <- unique(data_1gb$traffictype)
vec_app <- unique(data_1gb$appsiteid)
vec_pub <- unique(data_1gb$publisherid)
vec_appcat <- unique(data_1gb$appsitecategory)
vec_camp <- unique(data_1gb$campaignid)

splitfunc <- function(data,varstring,varvec)
{
 for(i in varvec) 
 {
   str <- as.character(i)
   print(str)
   if(varstring=="traffictype"){
   loc_data <- subset(data,as.character(traffictype)==str)
   }
   else if(varstring=="appsiteid"){
     loc_data <- subset(data,as.character(appsiteid)==str)
   }
   else if(varstring=="appsitecategory")
   {
     loc_data <- subset(data,as.character(appsitecategory)==str)
   }
   else if(varstring=="campaignid")
   {
     loc_data <- subset(data,as.character(campaignid)==str)
   }
   else if(varstring=="publisherid")
   {
     loc_data <- subset(data,as.character(publisherid)==str)
   }
   write.csv(loc_data,paste0(getwd(),"/",varstring,"/",str,".csv"),row.names=F)
 }
}

# splitfunc(data_1gb,"traffictype",vec_t)
splitfunc(data_1gb,"appsiteid",vec_app)
splitfunc(data_1gb,"appsitecategory",vec_appcat)
splitfunc(data_1gb,"campaignid",vec_camp)
splitfunc(data_1gb,"publisherid",vec_pub)
