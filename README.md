# Информацинонная система "Кинотеатр"
___

## Общее описание 
Данный проект представляет собой информационную систему для кинотеатра.
Система включает в себя работу с базой данных MySQL, работу с хранимыми процедурами и запросами, а так же авторизацию пользователей. 

## Функциональные возможности
+ **Авторизация пользователей**: система поддерживает аутентификацию пользователей, обеспечивая разграничение доступа к различным функциям в зависимости от роли пользователя.
+ **Корзина для покупки билетов**: пользователи могут добавлять билеты в корзину и оформлять покупку. Данные о билетах хранятся в таблице билетов в базе данных.
+ **Работа с отчетами**: система предоставляет возможность генерации отчетов по данным из базы данных с использованием хранимых процедур. Это позволяет выполнять сложные запросы и агрегацию данных на стороне сервера.
+ **Запросы к базе данных**: реализована поддержка различных запросов к базе данных для вывода информации о фильмах, сеансах, залах и других сущностях, связанных с работой кинотеатра.

## Технологии 
+ **Backend**: для разработки бэкенда был использован фреймворк для создания веб-приложений **Flask** и язык порграммирования Python. Так же была выбрана реляционная база данных **MySQL**.
+ **Frontend**: интерфейс пользователей был реализован с помощью **HTML** и **CSS**. 
+ **База данных**: MySQL. Использование хранимых процедур для генерации отчетов и обработки запросов на стороне сервера.

## Использование
Пользователи могут авторизоваться в системе и соверщать покупку билетов(выбрать нужный фильм и место).
Администраторы системы могут создавать и просматривать отчеты и работать с запросами. 