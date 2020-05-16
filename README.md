# Хранилища и базы данных

## Подготовка

### Docker

https://docs.docker.com/engine/install/ubuntu/

### Oracle DB 

1. Скачать докер-образ https://yadi.sk/d/9nOqNSKgoRV5bA
1. Распаковать `unzip oracle_with_olaptrain.zip`
1. `docker load -i oracle_with_olaptrain.tar`
1. `docker run --name oracle -d -p 0.0.0.0:1521:1521 oracle_with_olaptrain`
1. `docker exec -ti -u oracle oracle bash`
1. В шелле делаем `sqlplus sys as sysdba@PDB1;`, пароль пустой. Затем выполняем последовательность команд:
```
shutdown;
startup;
ALTER PLUGGABLE DATABASE ALL OPEN;

alter session set container=pdb1;
create user lab_oracle_user identified by lab_oracle_user_password;
GRANT CONNECT,RESOURCE,DBA TO lab_oracle_user;
GRANT CREATE SESSION, GRANT ANY PRIVILEGE TO lab_oracle_user;
GRANT UNLIMITED TABLESPACE TO lab_oracle_user;

exit;
```
1. Выходим из шелла, Oracle DB готов и доступен на порту 1521.

### MySQL

1. `docker pull mysql`
1. `docker run --name mysql -e MYSQL_ROOT_PASSWORD=superstr0ngpassword -e MYSQL_USER=lab_mysql_user -e MYSQL_PASSWORD=lab_mysql_user_password -d mysql`
