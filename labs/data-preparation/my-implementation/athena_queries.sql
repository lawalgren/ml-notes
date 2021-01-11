/* Male/Female percentage */
select gender, count(*) * 100.0 / (select count(*) from streaming_data_test_123dasdf3) as percentage
from streaming_data_test_123dasdf3
group by gender;

/* 10 most common user ages */
select distinct age, count(*) as total from streaming_data_test_123dasdf3 group by age order by count(*) desc limit 10;

/* users sorted by decade */
select age / 10 as decade, count(*) as total from streaming_data_test_123dasdf3 group by age / 10 order by decade;
