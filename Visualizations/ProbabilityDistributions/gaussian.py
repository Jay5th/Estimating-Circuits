from math import pi, exp, sqrt


def gaussian_pdf(mean: int or float, std_deviation: int or float, x: int or float) -> int or float:
    mu, sigma = mean, std_deviation
    return (1 / (sigma * sqrt(2*pi))) * exp(-0.5 * ((x - mu) / sigma) ** 2)
