select DATE(date) as 'date', sum(price) as 'cash'
FROM tikets JOIN session ON id_session=session_id
WHERE YEAR(date) = '$year' AND month(date) = '$month'
GROUP BY DATE(date)