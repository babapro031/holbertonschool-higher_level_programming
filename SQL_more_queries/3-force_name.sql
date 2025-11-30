-- Table yaradılır (əgər artıq mövcuddursa, xətaya düşmür)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
