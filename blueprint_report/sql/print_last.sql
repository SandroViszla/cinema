select order_year, order_month, product_id, quantity, cost from rk6_sinema.report
where order_year = $date_start and order_month = $date_end