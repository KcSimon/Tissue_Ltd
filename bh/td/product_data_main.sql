CREATE TABLE "products" (
	"sku"	VARCHAR(32) NOT NULL,
	"product"	VARCHAR(256) NOT NULL,
	"cost"	REAL NOT NULL,
	"productionDate"	DATE NOT NULL,
	PRIMARY KEY("sku","productionDate")
);
CREATE TABLE IF NOT EXISTS "sales" (
	"sku"	VARCHAR(32) NOT NULL,
	"amount"	INTEGER NOT NULL,
	"price"	REAL NOT NULL,
	FOREIGN KEY("sku") REFERENCES "products"("sku") ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY("sku","price")
);
INSERT INTO "products" ("sku","product","cost","productionDate") VALUES ('PS12','bath tissue',20.14,'11/02/2020');
INSERT INTO "products" ("sku","product","cost","productionDate") VALUES ('SAZX','bath tissue',35.12,'03/03/2020');
INSERT INTO "products" ("sku","product","cost","productionDate") VALUES ('UW89','napkin',24.13,'04/08/2020');
INSERT INTO "products" ("sku","product","cost","productionDate") VALUES ('ZB5J','bath tissue',2.22,'11/11/2020');
INSERT INTO "products" ("sku","product","cost","productionDate") VALUES ('SCFH','hand towel',6.64,'16/12/2020');
INSERT INTO "products" ("sku","product","cost","productionDate") VALUES ('ANK3','tissue',32.88,'03/02/2020');
INSERT INTO "sales" ("sku","amount","price") VALUES ('UW89',303,59.23);
INSERT INTO "sales" ("sku","amount","price") VALUES ('ZB5J',204,99.05);
INSERT INTO "sales" ("sku","amount","price") VALUES ('SCFH',203,42.1);
INSERT INTO "sales" ("sku","amount","price") VALUES ('PS12',706,37.61);
INSERT INTO "sales" ("sku","amount","price") VALUES ('ANK3',560,75.12);
INSERT INTO "sales" ("sku","amount","price") VALUES ('SAZX',110,84.63);