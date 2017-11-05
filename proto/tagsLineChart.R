infile = "./../../data/output/tagsByTime.out"

# data is expected to be structured such that each row is a different time segment and 
# each column beyond the first is the count of the log tags counted in that time segment.
# 1   12    0   3
# 2   13    0   1
# ...
data <- read.table(infile, sep = "", header = F, nrows = 144, na.strings = "", stringsAsFactors = F)



# ======= Plot data[4] ===========

# data is read in as a list of lists
# we want to do some plots, so we need to get (x,y)-coordinates to plot
# this will take some coersion
x <- as.numeric(unlist(data[1]))
y <- as.numeric(unlist(data[4]))
z <- as.numeric(unlist(data[5]))


# same as plot(x,y) for our case, because of the values of x
plot(y)

# line plot comparing y and z plots
plot(y, type="o", col="blue")
lines(z, type="o", pch=22, col="red")
