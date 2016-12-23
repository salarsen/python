SELECT CONCAT_WS(' ', MONTHNAME(charged_datetime), YEAR(charged_datetime)) as date, SUM(amount) as revenue
FROM billing
WHERE MONTHNAME(charged_datetime) LIKE 'March' AND YEAR(charged_datetime) = 2012;

SELECT CONCAT_WS(' ', clients.first_name, clients.last_name) AS client_name, clients.client_id, SUM(amount) AS revenue
FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

SELECT site_id, domain_name
FROM sites
WHERE client_id = 10;

SELECT client_id, COUNT(domain_name) As number_of_websites, MONTHNAME(created_datetime) AS month_created, YEAR(created_datetime) AS year_created
FROM sites
WHERE client_id = 1
GROUP BY CONCAT(month_created, year_created);

SELECT client_id, COUNT(domain_name) As number_of_websites, MONTHNAME(created_datetime) AS month_created, YEAR(created_datetime) AS year_created
FROM sites
WHERE client_id = 20
GROUP BY CONCAT(month_created, year_created);

SELECT COUNT(leads.leads_id) AS number_of_leads, DATE_FORMAT(leads.registered_datetime, '%M %e, %Y') as date_generated, sites.domain_name
FROM leads
LEFT JOIN sites ON sites.site_id = leads.site_id
WHERE CAST(leads.registered_datetime AS DATE) BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-02-11' AS DATE)
GROUP BY leads.site_id;

SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as total_leads
FROM clients
LEFT JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE CAST(leads.registered_datetime AS DATE) BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-12-31' AS DATE)
GROUP BY client_name
ORDER BY total_leads DESC;

SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as total_leads, MONTHNAME(leads.registered_datetime) as month_name
FROM clients
LEFT JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE (MONTH(leads.registered_datetime) BETWEEN 1 AND 6) AND YEAR(leads.registered_datetime) = 2011
GROUP BY client_name, month_name
ORDER BY MONTH(leads.registered_datetime);

SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as total_leads, sites.domain_name, DATE_FORMAT(leads.registered_datetime, '%M %e, %Y') as date_generated
FROM clients
LEFT JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
WHERE CAST(leads.registered_datetime AS DATE) BETWEEN CAST('2011-01-01' AS DATE) AND CAST('2011-12-31' AS DATE)
GROUP BY client_name, sites.domain_name
ORDER BY client_name;

SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, COUNT(leads.leads_id) as total_leads, sites.domain_name
FROM clients
LEFT JOIN sites ON sites.client_id = clients.client_id
LEFT JOIN leads ON leads.site_id = sites.site_id
GROUP BY client_name, sites.domain_name
ORDER BY client_name;

SELECT concat_ws(' ', clients.first_name, clients.last_name) AS client_name, SUM(billing.amount) as total_revenue, monthname(billing.charged_datetime) as month_charge, YEAR(billing.charged_datetime) as year_charge
FROM clients
LEFT JOIN billing ON clients.client_id = billing.client_id
GROUP BY client_name, month_charge, year_charge
ORDER BY client_name, year_charge, month(billing.charged_datetime) ASC;

SELECT concat_ws(' ', clients.first_name, clients.last_name) as client_name, GROUP_CONCAT(sites.domain_name SEPARATOR ' / ') AS sites
FROM clients
LEFT JOIN sites ON clients.client_id = sites.client_id
GROUP BY client_name;
