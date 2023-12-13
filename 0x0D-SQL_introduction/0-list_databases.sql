#!/usr/bin/env bash
--script that lists all MySQL databases
mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "SHOW DATABASES;"
