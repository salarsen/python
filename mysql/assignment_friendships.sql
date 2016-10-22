SELECT * FROM users;
INSERT INTO friendships (user_id, friend_id) VALUES (1,4);
INSERT INTO friendships (user_id, friend_id) VALUES (1,3);
INSERT INTO friendships (user_id, friend_id) VALUES (1,2);
INSERT INTO friendships (user_id, friend_id) VALUES (2,1);
INSERT INTO friendships (user_id, friend_id) VALUES (3,1);
INSERT INTO friendships (user_id, friend_id) VALUES (4,1);

UPDATE friendships SET created_at = NOW(), updated_at = NOW() WHERE id > 0;

SELECT * FROM friendships;

SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS users2 ON friendships.friend_id = users2.id
ORDER BY friend_last_name;