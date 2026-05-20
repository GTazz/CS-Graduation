CREATE DATABASE aula_n2_teste;

USE aula_n2_teste;

CREATE TABLE proprietario (
	id_proprietario int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    cpf varchar(11) NOT NULL,
    data_nascimento date NOT NULL,
    renda decimal(10,2) NOT NULL,
    ativo boolean
);

CREATE TABLE carro (
	id_carro int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    modelo varchar(100) NOT NULL,
    marca varchar(50) NOT NULL,
    ano int,
    preco decimal(10,2),
    placa char(7) NOT NULL,
    disponivel boolean,
    id_proprietario int,
    FOREIGN KEY (id_proprietario) REFERENCES proprietario(id_proprietario)
);

CREATE TABLE manutencao (
	id_manutencao int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    descreicao varchar(200) NOT NULL,
    data_manutencao date NOT NULL,
    valor decimal(10,2),
    id_carro int NOT NULL,
    FOREIGN KEY (id_carro) REFERENCES carro(id_carro)
);

ALTER TABLE carro ADD COLUMN cor varchar(30);

ALTER TABLE proprietario MODIFY nome varchar(150);

ALTER TABLE carro DROP COLUMN cor;

DROP TABLE manutencao;
DROP TABLE carro;
DROP TABLE proprietario;
