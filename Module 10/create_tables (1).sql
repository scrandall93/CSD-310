
DROP TABLE IF EXISTS Inventory;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Supplier;
DROP TABLE IF EXISTS Inbound_orders;
DROP TABLE IF EXISTS Outbound_orders;
DROP TABLE IF EXISTS Distribution;
DROP TABLE IF EXISTS Contract;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Payroll;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Management;
DROP TABLE IF EXISTS Work_Hours;



CREATE TABLE `Inventory` (
	`supply_no` INT NOT NULL AUTO_INCREMENT,
	`item_no` INT NOT NULL,
	`inventory_qty` INT NOT NULL,
	PRIMARY KEY (`supply_no`)
);

CREATE TABLE `Item` (
	`item_no` INT NOT NULL AUTO_INCREMENT,
	`item_name` VARCHAR(20) NOT NULL,
	`item_price` DECIMAL(6,2) NOT NULL,
	PRIMARY KEY (`item_no`)
);

CREATE TABLE `Supplier` (
	`supplier_id` INT NOT NULL AUTO_INCREMENT,
	`supplier_name` VARCHAR(20) NOT NULL,
	`contact_id` INT NOT NULL,
	`item_no` INT,
	PRIMARY KEY (`supplier_id`)
);

CREATE TABLE `Inbound_orders` (
	`inventory_order_id` INT NOT NULL AUTO_INCREMENT,
	`supplier_id` INT NOT NULL,
	`expected_delivery_dt` DATE,
	`actual_delivery_dt` DATE,
	`supply_no` INT NOT NULL,
	PRIMARY KEY (`inventory_order_id`)
);

CREATE TABLE `Outbound_orders` (
	`order_no` INT NOT NULL AUTO_INCREMENT,
	`item_count` INT NOT NULL,
	`total_cost` DECIMAL(6,2) NOT NULL,
	`item_no` INT NOT NULL,
	`distributor_id` INT NOT NULL,
	PRIMARY KEY (`order_no`)
);

CREATE TABLE `Distribution` (
	`distributor_id` INT NOT NULL AUTO_INCREMENT,
	`distributor_name` VARCHAR(20) NOT NULL,
	`item_no` DECIMAL(6) NOT NULL,
	`contact_id` INT NOT NULL,
	PRIMARY KEY (`distributor_id`)
);

CREATE TABLE `Contact` (
	`contact_id` INT NOT NULL AUTO_INCREMENT,
	`address` VARCHAR(50),
	`city` VARCHAR(20),
	`state` VARCHAR(20),
	`zip` VARCHAR(20),
	`phone` VARCHAR(20),
	`email` VARCHAR(20),
	PRIMARY KEY (`contact_id`)
);

CREATE TABLE `Department` (
	`dept_id` INT NOT NULL AUTO_INCREMENT,
	`dept_name` VARCHAR(20),
	`NumOfEmployees` INT,
	PRIMARY KEY (`dept_id`)
);

CREATE TABLE `Payroll` (
	`check_no` INT NOT NULL AUTO_INCREMENT,
	`pay_amount` DECIMAL(6,2) NOT NULL,
	`pay_date` DATE NOT NULL,
	`employee_id` INT NOT NULL,
	`dept_id` INT NOT NULL,
	PRIMARY KEY (`check_no`)
);

CREATE TABLE `Employee` (
	`employee_id` INT NOT NULL AUTO_INCREMENT,
	`first_name` VARCHAR(20) NOT NULL,
	`last_name` VARCHAR(20) NOT NULL,
	`contact_id` INT NOT NULL,
	`dept_id` INT NOT NULL,
	`check_no` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

CREATE TABLE `Management` (
	`mngmt_id` INT NOT NULL AUTO_INCREMENT,
	`employee_id` INT NOT NULL,
	`dept_id` INT NOT NULL,
	`start_date` DATE,
	`end_date` DATE,
	PRIMARY KEY (`mngmt_id`)
);

CREATE TABLE `Work_hours` (
	`hours_YTD` DECIMAL(9) NOT NULL,
	`current_week` INT NOT NULL,
	`employee_id` INT NOT NULL,
	PRIMARY KEY (`employee_id`)
);

