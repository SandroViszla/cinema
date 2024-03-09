SELECT
    s.movie AS movie_name,
    t.idtikets,
    t.row,
    t.seat,
    t.price
FROM
    tikets t
JOIN
    session s ON t.session_id = s.id_session
WHERE
    t.is_sold = '0'
