# SQLParser+

SQLParser+ is a Python script that will take as input a txt or sql file. It will extract the queries inside file to create a hierarchical JSON from it.

From this JSON you can:
- Create an UML diagram of your DB
- Export a Data Catalog creation script
- Create the Data Lineage of your DB

Don't worry about the formatting of your queries thanks to the Auto Format feature you can simply put your script and let the magic happen !


## Installation

Install python 3.12

```bash

```

## Correct Format

Here is the format required for the script so SQLParser+ can correctly parse everything and output accurate data. (“Managed by Auto Format” means you can have peace of mind SQLParser+ takes care of making this modification to the query for you)
- (Managed By Auto Format) Each column's line for CREATE TABLE must end with a space
- (Managed By Auto Format) DECIMAL must not have spaces between their decimal point -> DECIMAL(10,2)
- (Managed By Auto Format) ENUM must not have spaces between their possible values -> ENUM('user','admin)
  
## Authors

- [@Dolotboy](https://www.github.com/dolotboy)

