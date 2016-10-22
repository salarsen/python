SELECT countries.name as country, languages.language as language, languages.percentage as percentage
FROM countries
JOIN languages ON languages.country_id = countries.id
WHERE languages.language LIKE '%Slovene%'
ORDER BY percentage DESC;

SELECT countries.name as country, (SELECT COUNT(cities.name) FROM cities WHERE cities.country_id = countries.id) as total_cities
FROM countries
ORDER by total_cities DESC;

SELECT countries.name AS country, count(*) AS cities
FROM cities
LEFT JOIN countries ON cities.country_id = countries.id
GROUP BY country
ORDER BY cities DESC;

SELECT cities.name AS name, cities.population AS population
FROM cities
LEFT JOIN countries ON cities.country_id = countries.id
WHERE countries.name LIKE '%Mexico%' AND cities.population > 500000
ORDER BY population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM languages
LEFT JOIN countries ON languages.country_id = countries.id
WHERE percentage > 89
ORDER BY percentage DESC;

SELECT name, surface_area, population
FROM countries 
WHERE surface_area < 501 AND population > 100000;

SELECT name, government_form, capital, life_expectancy
FROM countries
WHERE capital > 200 AND life_expectancy > 75 AND government_form LIKE 'Constitutional Monarchy';

SELECT countries.name, cities.name, cities.district, cities.population
FROM cities
LEFT JOIN countries ON countries.id = cities.country_id
WHERE district LIKE 'Buenos Aires' AND cities.population > 500000;

SELECT region, count(*) As countries
FROM countries
GROUP BY region
ORDER BY countries DESC;