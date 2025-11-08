# library(raster)
# library(rgdal)
# library(rgeos)
# library(ggplot2)
# library(dplyr)
#
# ### Q1: Assam only
#
# ### Get data
# india &lt;- getData("GADM", country = "India", level = 1)
#
# ### Choose Assam
# assam &lt;- subset(india, NAME_1 == "Assam")
#
# ### SPDF to DF
# map &lt;- fortify(assam)
#
# ### Draw a map
#
# ggplot() +
# geom_map(data = map, map = map, aes(x = long, y = lat, map_id = id, group = group))
#
#
# ### Q2: State with their names
#
# map &lt;- fortify(india)
# map$id &lt;- as.integer(map$id)
#
# dat &lt;- data.frame(id = 1:(length(india@data$NAME_1)), state = india@data$NAME_1)
# map_df &lt;- inner_join(map, dat, by = "id")
#
# centers &lt;- data.frame(gCentroid(india, byid = TRUE))
# centers$state &lt;- dat$state
#
#
# ### This is hrbrmstr's own function
# theme_map &lt;- function (base_size = 12, base_family = "") {
# theme_gray(base_size = base_size, base_family = base_family) %+replace%
# theme(
# axis.line=element_blank(),
# axis.text.x=element_blank(),
# axis.text.y=element_blank(),
# axis.ticks=element_blank(),
# axis.ticks.length=unit(0.3, "lines"),
# axis.ticks.margin=unit(0.5, "lines"),
# axis.title.x=element_blank(),
# axis.title.y=element_blank(),
# legend.background=element_rect(fill="white", colour=NA),
# legend.key=element_rect(colour="white"),
# legend.key.size=unit(1.5, "lines"),
# legend.position="right",
# legend.text=element_text(size=rel(1.2)),
# legend.title=element_text(size=rel(1.4), face="bold", hjust=0),
# panel.background=element_blank(),
# panel.border=element_blank(),
# panel.grid.major=element_blank(),
# panel.grid.minor=element_blank(),
# panel.margin=unit(0, "lines"),
# plot.background=element_blank(),
# plot.margin=unit(c(1, 1, 0.5, 0.5), "lines"),
# plot.title=element_text(size=rel(1.8), face="bold", hjust=0.5),
# strip.background=element_rect(fill="grey90", colour="grey50"),
# strip.text.x=element_text(size=rel(0.8)),
# strip.text.y=element_text(size=rel(0.8), angle=-90)
# )
# }
#
# ggplot() +
# geom_map(data = map_df, map = map_df,
#          aes(map_id = id, x = long, y = lat, group = group),
#          color = "#ffffff", fill = "#bbbbbb", size = 0.25) +
# geom_text(data = centers, aes(label = state, x = x, y = y), size = 2) +
# coord_map() +
# labs(x = "", y = "", title = "India State") +
# theme_map()
#
#
# ### Q3: Add color to one state
#
# ### Create a column for color. Assam will have a different color.
# map_df2 &lt;- transform(map_df, hue = ifelse(state == "Assam", "a", NA))
#
#
# ggplot() +
# geom_map(data = map_df2, map = map_df2,
#          aes(map_id = id, x = long, y = lat, group = group, fill = hue),
#          color = "#ffffff", size = 0.25) +
# geom_text(data = centers, aes(label = state, x = x, y = y), size = 2) +
# coord_map() +
# labs(x = "", y = "", title = "India State") +
# theme_map() +
# theme(legend.position = "none")
#
#


# import urllib.request, json
# resp = urllib.request.urlopen('https://query2.finance.yahoo.com/v10/finance/quoteSummary/tsla?modules=price')
# data = json.loads(resp.read())
# price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
# print(price)

mylist = [1, 2, 3]
for item in mylist:
    print(item)


mydict = {1: 'one', 2: 'two', 3: 'three'}
for key in mydict:
    print(key, mydict[key])


for i, item in enumerate(mylist):
    mylist[i] = item ** 2
    print(mylist[i])