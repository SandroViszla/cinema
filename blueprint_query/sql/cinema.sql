-- создать отчет о сеансах на дату ХХХ по форме: название зала, время начала сеанса, общая стоймость всех прожанных билетов
SELECT name, date_format(date, '%H:%i:%s') AS 'dayjust', sum(price)
FROM rk6_sinema.hall
JOIN rk6_sinema.session ON hall_id = idhall
JOIN rk6_sinema.tikets ON id_session = session_id
WHERE DATE(date) = '$formatted_date'
GROUP BY name, date;
