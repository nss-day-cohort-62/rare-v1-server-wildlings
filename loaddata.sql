CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);



CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "content" varchar,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);


INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Tags VALUES (2, 'Coffee');
INSERT INTO Tags VALUES (3, 'Toast');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

DROP TABLE Users;
DROP TABLE Categories;
DROP TABLE Posts;

INSERT INTO Users VALUES (null, "Googly", "Moogly", "googly@moogly.com", 
"no", "googly", "password", null, "2023-04-21", 1);
INSERT INTO Users VALUES (null, "Eric", "Frey", "ericlfrey@elf.com", 
"just a coder", "elfrey", "elfrey", "NULL", "2023-04-21", 1);
INSERT INTO Users VALUES (null, "Sarah", "Smith", "sarah.smith@example.com", 
"Loves to travel and take photos.", "sarahsmith", "password123", null, "2023-04-22", 1);
INSERT INTO Users VALUES (null, "John", "Doe", "johndoe@example.com", 
"Tech enthusiast and amateur photographer.", "johndoe", "secret", null, "2023-04-23", 1);
INSERT INTO Users VALUES (null, "Alice", "Lee", "alicelee@example.com", 
"Bookworm, coffee addict, and occasional writer.", "alicelee", "mypassword", null, "2023-04-24", 1);

INSERT INTO Categories VALUES (null, 'General');
INSERT INTO Categories VALUES (null, 'Travel');
INSERT INTO Categories VALUES (null, 'Lifestyle');


INSERT INTO Posts VALUES (null, 1, 2, 'The Best Places to Visit in Europe', '04/23/2023', 'Europe is full of beautiful destinations that are waiting to be explored. In this post, we will discuss some of the best places to visit in Europe, including Paris, Rome, and Barcelona.');
INSERT INTO Posts VALUES (null, 2, 3, 'My Morning Routine', '04/22/2023', 'I wake up early every morning and start my day with a cup of coffee and a quick workout. Then, I spend some time meditating and journaling before starting work. Here is a more detailed breakdown of my morning routine.');
INSERT INTO Posts VALUES (null, 3, 1, 'How to Stay Productive When Working from Home', '04/21/2023', 'Working from home can be challenging, especially if you have trouble staying focused. In this post, we will share some tips and tricks for staying productive when working from home, including setting up a dedicated workspace and using time-blocking techniques.');
INSERT INTO Posts VALUES (null, 2, 2, 'Summer Vacation Ideas', '5/1/2023', 'Looking for some great ideas for your summer vacation? Check out these top destinations!');
INSERT INTO Posts VALUES (null, 3, 1, 'New Product Launch', '3/15/2023', 'Introducing our latest product, now available for purchase!');
INSERT INTO Posts VALUES (null, 2, 3, 'Healthy Eating Tips', '2/5/2023', 'Learn how to make simple changes to your diet that can have a big impact on your health.');
INSERT INTO Posts VALUES (null, 4, 2, 'Home Improvement Projects', '4/20/2023', 'Ready to tackle some DIY projects around the house? Here are some ideas to get you started.');
INSERT INTO Posts VALUES (null, 3, 1, 'Company News', '1/1/2023', 'We are excited to announce our latest company milestone!');
INSERT INTO Posts VALUES (null, 4, 3, 'Travel Hacks', '6/1/2023', 'Save money and travel smarter with these top travel hacks.');
INSERT INTO Posts VALUES (null, 5, 2, 'Gardening Tips', '5/15/2023', 'Get your garden ready for summer with these expert tips.');
INSERT INTO Posts VALUES (null, 2, 1, 'Job Openings', '4/1/2023', 'We are hiring! Check out our latest job openings and apply today.');

SELECT 
  p.id,
  p.title,
  p.publication_date,
  p.content,
  c.label,
  u.first_name,
  u.last_name
FROM Posts p 
JOIN Categories c 
  ON c.id = p.category_id
JOIN Users u 
  ON u.id = p.user_id
ORDER BY p.publication_date DESC


DROP TABLE Users;
DROP TABLE Categories;
DROP TABLE Posts;

INSERT INTO Posts VALUES (null, 1, 2, 'The Best Places to Visit in Europe', '04/23/2023', 'Europe is full of beautiful destinations that are waiting to be explored. In this post, we will discuss some of the best places to visit in Europe, including Paris, Rome, and Barcelona.');
INSERT INTO Posts VALUES (null, 2, 3, 'My Morning Routine', '04/22/2023', 'I wake up early every morning and start my day with a cup of coffee and a quick workout. Then, I spend some time meditating and journaling before starting work. Here is a more detailed breakdown of my morning routine.');
INSERT INTO Posts VALUES (null, 3, 1, 'How to Stay Productive When Working from Home', '04/21/2023', 'Working from home can be challenging, especially if you have trouble staying focused. In this post, we will share some tips and tricks for staying productive when working from home, including setting up a dedicated workspace and using time-blocking techniques.');
INSERT INTO Posts VALUES (null, 2, 2, 'Summer Vacation Ideas', '5/1/2023', 'Looking for some great ideas for your summer vacation? Check out these top destinations!');
INSERT INTO Posts VALUES (null, 3, 1, 'New Product Launch', '3/15/2023', 'Introducing our latest product, now available for purchase!');
INSERT INTO Posts VALUES (null, 2, 3, 'Healthy Eating Tips', '2/5/2023', 'Learn how to make simple changes to your diet that can have a big impact on your health.');
INSERT INTO Posts VALUES (null, 4, 2, 'Home Improvement Projects', '4/20/2023', 'Ready to tackle some DIY projects around the house? Here are some ideas to get you started.');
INSERT INTO Posts VALUES (null, 3, 1, 'Company News', '1/1/2023', 'We are excited to announce our latest company milestone!');
INSERT INTO Posts VALUES (null, 4, 3, 'Travel Hacks', '6/1/2023', 'Save money and travel smarter with these top travel hacks.');
INSERT INTO Posts VALUES (null, 5, 2, 'Gardening Tips', '5/15/2023', 'Get your garden ready for summer with these expert tips.');
INSERT INTO Posts VALUES (null, 2, 1, 'Job Openings', '4/1/2023', 'We are hiring! Check out our latest job openings and apply today.');

INSERT INTO Users VALUES (null, "Googly", "Moogly", "googly@moogly.com", 
"no", "googly", "password", null, "2023-04-21", 1);
INSERT INTO Users VALUES (null, "Eric", "Frey", "ericlfrey@elf.com", 
"just a coder", "elfrey", "elfrey", "NULL", "2023-04-21", 1);
INSERT INTO Users VALUES (null, "Sarah", "Smith", "sarah.smith@example.com", 
"Loves to travel and take photos.", "sarahsmith", "password123", null, "2023-04-22", 1);
INSERT INTO Users VALUES (null, "John", "Doe", "johndoe@example.com", 
"Tech enthusiast and amateur photographer.", "johndoe", "secret", null, "2023-04-23", 1);
INSERT INTO Users VALUES (null, "Alice", "Lee", "alicelee@example.com", 
"Bookworm, coffee addict, and occasional writer.", "alicelee", "mypassword", null, "2023-04-24", 1);

INSERT INTO Categories VALUES (null, 'General');
INSERT INTO Categories VALUES (null, 'Travel');
INSERT INTO Categories VALUES (null, 'Lifestyle');

INSERT INTO Tags ('label') VALUES ('CSS');
INSERT INTO Tags ('label') VALUES ('React');
INSERT INTO Tags ('label') VALUES ('Python');
INSERT INTO Tags ('label') VALUES ('IceCream');

INSERT INTO PostTags VALUES (null, 1, 2);
INSERT INTO PostTags VALUES (null, 1, 3);
INSERT INTO PostTags VALUES (null, 1, 1);

SELECT * FROM PostTags;

SELECT DISTINCT
  p.id,
  p.title,
  p.publication_date,
  p.content,
  c.id category_id,
  c.label,
  u.id user_id,
  u.first_name,
  u.last_name,
  u.email,
  u.bio,
  u.username,
  u.password,
  u.profile_image_url,
  u.created_on,
  u.active,
  (SELECT GROUP_CONCAT(t.id)
    FROM PostTags pt
    JOIN Tags t on pt.tag_id = t.id
    WHERE pt.post_id = p.id) as tags
  FROM Posts p 
  JOIN Categories c 
      ON c.id = p.category_id
  JOIN Users u 
      ON u.id = p.user_id
  JOIN PostTags pt 
      ON p.id = pt.post_id
  JOIN Tags t 
      ON pt.tag_id = t.id
  ORDER BY p.publication_date DESC 
        
DELETE FROM PostTags
    WHERE post_id = post_id;
INSERT INTO PostTags (post_id, tag_id) VALUES (12,1);

DELETE FROM PostTags
    WHERE post_id = id;
INSERT INTO PostTags (id, post_id, tag_id) VALUES (1,1,3)