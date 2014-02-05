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
gspcTail=as.ts(tail(r.xd,1000))
gspcArma=armaFit(gspcTail~arma(5,1),data=gspcTail)

armaSearch=function(
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
		fit=tryCatch(armaFit(formula,data=series),error=function(err) FALSE, warning=function(warn) FALSE)
		if(!is.logical(fit))
		{
			fitAic=fit@fit$aic
			if(fitAic<bestAic)
			{
				bestAic=fitAic
				bestFit=fit
				bestModel=c(p,q)
			}
			if(trace)
			{
				message=paste(sep="","(",p,",",q,"): AIC= ", fitAic)
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

gspcArma=armaFit(gspcTail~arma(Coef),data=gspcTail)

#Logit
dat<-read.csv("Candidate_Integrate.csv",header=FALSE)
summary(dat)
#conver numerci cols here or Excel..
dat<-cbind(dat[,1:2],as.numeric(dat[,3]))



