--INSERT INTO user(username, password) VALUES('newman', 'qwerty123');
--SELECT * FROM user; 
--SELECT username as nick, password FROM user;

/*SELECT username as nick, password
FROM user
WHERE username = 'smith';*/

--SELECT username as nick, password
--FROM user
--WHERE username = 'smith' OR id = 1;

--SELECT username as nick, password
--FROM user
--WHERE username = 'smith' AND id = 3;


/*SELECT username as nick, password
FROM user
WHERE id > 1 AND id < 4;*/


/*UPDATE user
SET username = 'rorshah'
WHERE username = 'freeman';*/


--UPDATE user
--SET password = 'new_password'
--WHERE id > 1;

/*DELETE FROM user
WHERE username = 'rorshah';*/


/*SELECT * FROM user
ORDER BY username DESC;*/

/*SELECT user.username, role.name, role.description
FROM user, role
WHERE user.role_id = role.id*/


/*SELECT user.username, role.name as role, role.description
FROM user
JOIN role
ON user.role_id = role.id
WHERE role.name = 'user';*/

/*SELECT user.username, role.name as role, role.description, profile.info
FROM user
JOIN role
ON user.role_id = role.id
JOIN profile
ON user.profile_id = profile.id
WHERE role.name = 'user';*/

SELECT user.username, city.name as city, country.name
FROM user_city
JOIN user
ON user.id = user_city.user_id
JOIN city
ON city.id = user_city.city_id
JOIN country
ON city.country_id = country.id
WHERE country.code = 'US' AND user.username = 'smith'
ORDER BY city;
