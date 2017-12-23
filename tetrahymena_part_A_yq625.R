library(dplyr)
library(ggplot2)
df = read.table("tetrahymena.tsv",header = T)
View(df)
df<-df %>%
  filter(diameter>19.2) 
df<-df %>% 
  group_by(culture,glucose) %>% summarise(mean(conc),mean(diameter))
df<-df %>%
  mutate(log(`mean(conc)`),log(`mean(diameter)`))
plot<-df %>%
  ggplot(.,aes(x=log(`mean(diameter)`),y=log(`mean(conc)`),shape=glucose))+
  geom_point(aes(color=glucose))
plot
colnames(df)[5]<-'log_conc'
colnames(df)[6]<-'log_dia'
fit1<-lm(log_conc~log_dia, data = df[1:32,])
fit2<-lm(log_conc~log_dia, data = df[33:51,])
plot+geom_abline(intercept = coef(fit1)[1],slope = coef(fit1)[2],color='blue')+
  geom_abline(intercept = coef(fit2)[1],slope = coef(fit2)[2],color='red')
