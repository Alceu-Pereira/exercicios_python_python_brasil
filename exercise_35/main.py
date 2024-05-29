year = 0


population_country_a = 80000
annual_growth_rate_a = 0.03



population_country_b = 200000
annual_growth_rate_b = 0.015


while True:
    year += 1

    population_country_a += (annual_growth_rate_a * population_country_a)

    population_country_b += (annual_growth_rate_b * population_country_b)

    if population_country_a >= population_country_b:
        break

print(round(population_country_a))
print(round(population_country_b))
print(year)