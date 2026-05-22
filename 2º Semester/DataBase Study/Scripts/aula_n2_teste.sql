CREATE DATABASE aula_n2_teste;

USE aula_n2_teste;

CREATE TABLE proprietario (
    id_proprietario int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    cpf varchar(11) NOT NULL,
    data_nascimento date NOT NULL,
    renda decimal(10, 2) NOT NULL,
    ativo boolean
);

CREATE TABLE carro (
    id_carro int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    modelo varchar(100) NOT NULL,
    marca varchar(50) NOT NULL,
    ano int,
    preco decimal(10, 2),
    placa char(7) NOT NULL,
    disponivel boolean,
    id_proprietario int,
    FOREIGN KEY (id_proprietario) REFERENCES proprietario (id_proprietario)
);

CREATE TABLE manutencao (
    id_manutencao int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descricao varchar(200) NOT NULL,
    data_manutencao date NOT NULL,
    valor decimal(10, 2),
    id_carro int NOT NULL,
    FOREIGN KEY (id_carro) REFERENCES carro (id_carro)
);

-- ALTER TABLE carro ADD COLUMN cor varchar(30);
-- ALTER TABLE proprietario MODIFY nome varchar(150);
-- ALTER TABLE carro DROP COLUMN cor;
-- DROP TABLE manutencao;
-- DROP TABLE carro;
-- DROP TABLE proprietario;
INSERT INTO
    proprietario (
        id_proprietario,
        nome,
        cpf,
        data_nascimento,
        renda,
        ativo
    )
VALUES
    (
        1,
        'João Silva',
        '12345678901',
        '1980-05-15',
        5000.00,
        true
    ),
    (
        2,
        'Maria Souza',
        '98765432100',
        '1990-08-20',
        6000.00,
        true
    );

INSERT INTO
    proprietario
VALUES
    (
        3,
        'Carlos Pereira',
        '11122233344',
        '1975-12-10',
        4500.00,
        false
    );

INSERT INTO
    proprietario (
        nome,
        cpf,
        data_nascimento,
        renda,
        ativo
    )
VALUES
    (
        'Pablo Escobar',
        '15555555555',
        '2002-01-01',
        9500.00,
        false
    );

INSERT into
    carro (
        modelo,
        marca,
        ano,
        preco,
        placa,
        disponivel,
        id_proprietario
    )
VALUES
    (
        'Civic',
        'Honda',
        2020,
        95000.00,
        'ABC1234',
        TRUE,
        1
    ),
    (
        'Corolla',
        'Toyota',
        2022,
        120000.00,
        'XYZ9876',
        FALSE,
        2
    ),
    (
        'Gol',
        'Volkswagen',
        2018,
        45000.00,
        'BRA4567',
        TRUE,
        1
    );

INSERT INTO
    manutencao (descricao, data_manutencao, valor, id_carro)
VALUES
    ('Troca de óleo', '2026-05-01', 250.00, 1),
    ('Alinhamento', '2026-05-03', 180.00, 2),
    ('Troca de pneus', '2026-05-05', 1200.00, 2);

-------------------------------------------------------

SELECT nome, renda FROM proprietario;

SELECT * FROM carro
WHERE preco > 50000;

SELECT * FROM carro
ORDER BY preco DESC;

SELECT * FROM proprietario
WHERE nome LIKE 'A%';

SELECT * FROM carro
WHERE ano BETWEEN 2016 AND 2023;

SELECT * FROM carro
WHERE marca IN ('Honda', 'Toyota');

SELECT * FROM carro
WHERE marca = 'Honda' OR marca = 'Toyota';

SELECT COUNT(*) AS "total de carros"
FROM carro;

-------------------------------------------------------

UPDATE carro
SET preco = 98000.00
WHERE id_carro = 1;

UPDATE proprietario
SET renda = 8000.00,
    ativo = FALSE
WHERE id_proprietario = 2;

UPDATE carro
SET disponivel = FALSE
WHERE preco > 100000;

DELETE FROM manutencao
WHERE id_manutencao = 3;

DELETE FROM carro
WHERE ano < 2019;

DELETE FROM proprietario
WHERE ativo = FALSE;