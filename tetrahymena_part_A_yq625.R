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
  ggplot(.,aes(x=log(`mean(diameter)`),y=log(`mean(conc)`)))+
  geom_point(aes(color=glucose))+
  geom_abline()
plot
