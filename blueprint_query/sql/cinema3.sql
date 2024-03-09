SELECT session.id_session as 'id', movie, CAST(session.date AS DATE) as 'Date'
FROM session
LEFT JOIN tikets ON session_id=id_session
WHERE session_id IS NULL AND YEAR(session.date) = '$year';
