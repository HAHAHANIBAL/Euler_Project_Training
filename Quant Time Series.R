# Time Series

library("tseries")
library("zoo")
library("moments")
library("quantmod")
library("fArma")


start0<-"1995-10-01"

require("quantmod")

spc <-new.env()

setDefaults(getSymbols,src="yahoo")
getSymbols("^GSPC",env=spc,from=start0)
x.d<-as.zoo(spc$GSPC[,4])

#Useful Functions
#time(x.d)
#start(x.d)

#Calculating returns
r.xd=diff(log(x.d))
ts=as.numeric(r.xd)
hh<-c("Basic statistics:	","Nobs =", formatC(length(ts), width=9) )
print.noquote(hh)
hh<-c("Mean=",formatC(mean(ts),digits=5,width=8,format="fg"),
	"Stdev=",formatC(sd(ts),digits=5,width=8,format="fg"))
print.noquote(hh)
hh<-c("Skewness=",formatC(skewness(ts),digits=8,width=5,format="fg"),
	"Kurtosis=",formatC(kurtosis(ts),digits=8,width=5,format="fg"))
print.noquote(hh)
jarque.bera.test(ts)
p<-as.vector(log(x.d))
m<-22
M<-as.integer((length(p)-1)/m)
TT<-m*M
p<-p[1:(TT+1)]
r<-diff(p)
mu<-mean(r)
rm<-c(1:M)*0
dataTail=as.ts(tail(r.xd,1000))
#dataArma=armaFit(dataTail~arma(5,1),data=dataTail)

modelSearch=function(
	series,
	minOrder=c(0,0),
	maxOrder=c(5,5),
	trace=FALSE)
{
	#set a sufficiently large number first
	bestAic=1e9
	len=NROW(series)
	for(p in minOrder[1]:maxOrder[1])
		for(q in minOrder[2]:maxOrder[2])
	{
		if(p==0&&q==0)
		{
			next
		}
		formula=as.formula(paste(sep="","series~arma(",p,",",q,")"))
		arma=tryCatch(armaFit(formula,data=series),error=function(err) FALSE, warning=function(warn) FALSE)
		if(!is.logical(arma))
		{
			armaAic=arma@fit$aic
			if(armaAic<bestAic)
			{
				bestAic=armaAic
				bestFit=arma
				bestModel=c(p,q)
			}
			if(trace)
			{
				message=paste(sep="","(",p,",",q,"): AIC= ", armaAic)
				print(message)
			}
		}
		else
		{
			if(trace)
			{
				message=paste(sep="","(",p,",",q,"):None")
				print(message)
			}
		}
	}
	if(bestAic<1e9)
	{
		return(bestModel)
	}
	return(FALSE)

}

modelSearch(dataTail)
#dataArma=armaFit(dataTail~arma(Coef),data=dataTail)
as.numeric(predict(dataArma,n.ahead=1,doplot=F)$pred)

#Logit
dat<-read.csv("dat.csv",header=FALSE)
summary(dat)
dat$V4<-factor(dat$V4)
dat$V5<-factor(dat$V5)
dat$V10<-as.numeric(dat$V10)
logitmodel<-glm(V1~V4+V5+V6+V7+V8+V9+V10+V11+V12,data=dat,family="binomial")
confint.default(logitmodel)
dat2014<-read.csv("dat2014.csv",header=FALSE)
dat2014$V4<-factor(dat2014$V4)
dat2014$V5<-factor(dat2014$V5)
dat2014$V10<-as.numeric(dat2014$V10)
dat_new<-cbind(dat2014[,4:12])
dat2014$V1<-predict(logitmodel,newdata=dat_new,type="response")
sink("congress_results_output.csv")
cbind(dat2014[,1])
sink()



#conver numerci cols here or Excel..
dat<-cbind(dat[,1:2],as.numeric(dat[,3]))

library("e1071")

dat<-read.table("ds_test_final.txt",sep="\t",header=TRUE)
summary(dat)
#fix(dat)
dat<-dat[order(-dat$hicov),,drop=FALSE]
#nrow(dat)
train<-rbind(dat[1:272762,])
test<-rbind(dat[272763:nrow(dat),])

x<-cbind(train[,2:9],train[,11:31])
y<-as.factor(train[,10])
classifier<-naiveBayes(x,y)
pred_y<-predict(classifier,x)
table(pred_y, y, dnn=list('predicted','actual'))



11 3:10 12:32
