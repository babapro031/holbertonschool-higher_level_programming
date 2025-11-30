-- İstifadəçi yaradılır (əgər artıq mövcud deyilsə)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- İstifadəçiyə bütün privileges verilir
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Dəyişiklikləri tətbiq etmək üçün
FLUSH PRIVILEGES;
