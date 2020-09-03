BEGIN TRANSACTION;
PRAGMA foreign_keys=ON;

DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS custom_attributes;

CREATE TABLE `teams` (
  `id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `name` varchar(255) NOT NULL DEFAULT 'My Team'
,  `created_at` timestamp NOT NULL DEFAULT current_timestamp
,  `updated_at` timestamp NOT NULL DEFAULT current_timestamp 
);
CREATE TABLE `contacts` (
  `id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `team_id` integer  NOT NULL
,  `name` varchar(255) DEFAULT NULL
,  `phone` varchar(255) NOT NULL
,  `email` varchar(255) DEFAULT NULL
,  `created_at` timestamp NOT NULL DEFAULT current_timestamp
,  `updated_at` timestamp NOT NULL DEFAULT current_timestamp 
,  UNIQUE (`phone`,`team_id`)
,  CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`team_id`) REFERENCES `teams` (`id`) ON DELETE CASCADE
);
CREATE TABLE `custom_attributes` (
  `id` integer  NOT NULL PRIMARY KEY AUTOINCREMENT
,  `contact_id` integer  NOT NULL
,  `key` varchar(255) NOT NULL
,  `value` varchar(255) NOT NULL
,  CONSTRAINT `custom_attributes_ibfk_1` FOREIGN KEY (`contact_id`) REFERENCES `contacts` (`id`) ON DELETE CASCADE
);
DELETE FROM sqlite_sequence;
CREATE INDEX "idx_custom_attributes_contact_id" ON "custom_attributes" (`contact_id`);
CREATE INDEX "idx_contacts_team_id" ON "contacts" (`team_id`);
COMMIT;
