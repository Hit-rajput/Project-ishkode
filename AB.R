# Load required libraries
library(ggplot2)

# Generate random data
set.seed(123)  # for reproducibility
x <- rnorm(50, mean = 10, sd = 2)
y <- 2 * x + rnorm(50, mean = 0, sd = 1)

# Calculate basic statistics
mean_x <- mean(x)
mean_y <- mean(y)
correlation <- cor(x, y)

# Print statistics
cat("Mean of x:", mean_x, "\n")
cat("Mean of y:", mean_y, "\n")
cat("Correlation between x and y:", correlation, "\n")

# Create a scatter plot using ggplot2
data <- data.frame(x = x, y = y)
scatter_plot <- ggplot(data, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Scatter Plot of x and y", x = "x-axis", y = "y-axis")

print(scatter_plot)
