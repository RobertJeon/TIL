# MySQL 터미널 명령어 정리

* 접속을 위한 디렉토리 이동
    - `cd /usr/local/mysql/bin`

* MySQL 접속
    - `./mysql -u root -p`

* 로컬서버 접속
    - `mysql -u root -p`
    - `mysql -u root -p --host 127.0.0.1`

* 외부 접속
    ```bash
    // 예시
    // port : 3000
    // host : 10.10.10.20
    mysql -u root -p --port 3000 --host 10.10.10.20
    ```

* 모든 데이터베이스 보기
    - `SHOW DATABASES;`

* 데이터베이스 생성하기
    - `CREATE DATABASE 데이터베이스명;`

* 데이터베이스 사용하기
    - `USE 데이터베이스명;`

* 테이블 생성하기
    ```sql
    CREATE TABLE 테이븡명(
        필드명 자료형(크기), NOT NULL AUTO_INCREMENT,
        필드명 자료형(크기),
        필드명 자료형(크기),
        PRIMARY KEY(필드명)
    );
    ```

* 모든 데이블 보기
    - `SHOW TABLES;`

* 테이블 구조 보기
    - `DESC 테이블명;`
    - `DESCRIBE 테이블명;`
    - `EXPALIN 테이블명;`

* 테이블의 컬럼에 데이터 추가하기
    - `INSERT INTO 테이블명 VALUES(필드1에 해당하는 값, 필드2에 해당하는 값, 필드3에 해당하는 값,...);`
    - `INSERT INTO 테이블명(필드명1, 필드명2, 필드명3) VALUES(필드1에 해당하는 값, 필드2에 해당하는 값, 필드3에 해당하는 값,...);`

* 테이블에 있는 데이터 수정하기
    - `UPDATE 테이블명 SET 컬럼명="수정할 값";`
    - `UPDATE 테이블명 SET 컬럼명="수정할 값" WHERE 조건문;`

* 테이블에 있는 데이터 삭제하기
    - `DELETE FROM 테이블명 WHERE 조건문;`

* 데이터 전체 삭제하기
    - `DELETE FROM 테이블명;`