CREATE TABLE `sow_lesson_plan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_of_delivery_id` int(11) NOT NULL DEFAULT 1,
  `learning_episode_id` int(11) NOT NULL,
  `title` varchar(20) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `duration_minutes` int DEFAULT 0,
  `task_icon` varchar(500) DEFAULT '',
  PRIMARY KEY (`id`),
  CONSTRAINT `sow_lesson_plan__has__learning_episode` FOREIGN KEY (`learning_episode_id`) REFERENCES `sow_learning_episode` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


ALTER TABLE `sow_lesson_plan` 
MODIFY COLUMN `title` varchar(40) NOT NULL;