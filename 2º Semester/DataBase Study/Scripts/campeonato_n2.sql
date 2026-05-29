CREATE DATABASE campeonato_n2;

USE campeonato_n2;

-- =========================================
-- TABELA: Estadios
-- =========================================
CREATE TABLE Estadios (
    codigo INT PRIMARY KEY,
    local VARCHAR(255),
    nome VARCHAR(150),
    capacidade INT,
    cidade VARCHAR(80),
    estado CHAR(2)
);

-- =========================================
-- TABELA: Equipes
-- =========================================
CREATE TABLE Equipes (
    codigo INT PRIMARY KEY,
    nome VARCHAR(100),
    tecnico VARCHAR(80),
    pais VARCHAR(50)
);

-- =========================================
-- TABELA: Juiz
-- =========================================
CREATE TABLE Juiz (
    registro VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(80),
    nacionalidade VARCHAR(80)
);

-- =========================================
-- TABELA: Jogadores
-- =========================================
CREATE TABLE Jogadores (
    documento VARCHAR(20) PRIMARY KEY,
    nome VARCHAR(130),
    status INT,
    codigo_equipe INT,
    numero INT,

    CONSTRAINT fk_jogadores_equipes
        FOREIGN KEY (codigo_equipe)
        REFERENCES Equipes(codigo)
);

-- =========================================
-- TABELA: Uniformes
-- =========================================
CREATE TABLE Uniformes (
    codigo_uniformes INT PRIMARY KEY,
    versao INT,
    cor_camisa VARCHAR(40),
    cor_calcao VARCHAR(40),
    cor_meias VARCHAR(40),
    codigo_equipes INT,

    CONSTRAINT fk_uniformes_equipes
        FOREIGN KEY (codigo_equipes)
        REFERENCES Equipes(codigo)
);

-- =========================================
-- TABELA: Partidas
-- =========================================
CREATE TABLE Partidas (
    codigo_partida INT PRIMARY KEY,
    data_hora DATETIME,
    codigo_mandate INT,
    codigo_visitante INT,
    placar VARCHAR(7),
    codigo_estadio INT,
    codigo_juiz VARCHAR(20),

    CONSTRAINT fk_partidas_mandante
        FOREIGN KEY (codigo_mandate)
        REFERENCES Equipes(codigo),

    CONSTRAINT fk_partidas_visitante
        FOREIGN KEY (codigo_visitante)
        REFERENCES Equipes(codigo),

    CONSTRAINT fk_partidas_estadio
        FOREIGN KEY (codigo_estadio)
        REFERENCES Estadios(codigo),

    CONSTRAINT fk_partidas_juiz
        FOREIGN KEY (codigo_juiz)
        REFERENCES Juiz(registro)
);

-- =========================================
-- INSERTS - Estadios
-- =========================================
INSERT INTO Estadios (codigo, local, nome, capacidade, cidade, estado)
VALUES
(1, 'Barra Funda', 'Allianz Parque', 43713, 'Sao Paulo', 'SP'),
(2, 'Itaquera', 'Neo Quimica Arena', 49205, 'Sao Paulo', 'SP'),
(3, 'Morumbi', 'MorumBIS', 66795, 'Sao Paulo', 'SP'),
(4, 'Maracana', 'Estadio do Maracana', 78838, 'Rio de Janeiro', 'RJ');

-- =========================================
-- INSERTS - Equipes
-- =========================================
INSERT INTO Equipes (codigo, nome, tecnico, pais)
VALUES
(1, 'Palmeiras', 'Abel Ferreira', 'Brasil'),
(2, 'Corinthians', 'Antonio Oliveira', 'Brasil'),
(3, 'Sao Paulo', 'Luis Zubeldia', 'Brasil'),
(4, 'Flamengo', 'Tite', 'Brasil');

-- =========================================
-- INSERTS - Juiz
-- =========================================
INSERT INTO Juiz (registro, nome, nacionalidade)
VALUES
('J001', 'Wilton Pereira Sampaio', 'Brasileiro'),
('J002', 'Raphael Claus', 'Brasileiro'),
('J003', 'Anderson Daronco', 'Brasileiro'),
('J004', 'Bruno Arleu', 'Brasileiro');

-- =========================================
-- INSERTS - Jogadores
-- =========================================
INSERT INTO Jogadores (documento, nome, status, codigo_equipe, numero)
VALUES
('DOC001', 'Flaco', 1, 1, 21),
('DOC002', 'Yuri Alberto', 1, 2, 9),
('DOC003', 'Lucas Moura', 1, 3, 7),
('DOC004', 'Gabriel Barbosa', 1, 4, 10);

-- =========================================
-- INSERTS - Uniformes
-- =========================================
INSERT INTO Uniformes (
    codigo_uniformes,
    versao,
    cor_camisa,
    cor_calcao,
    cor_meias,
    codigo_equipes
)
VALUES
(1, 1, 'Verde', 'Branco', 'Verde', 1),
(2, 1, 'Branco', 'Preto', 'Branco', 2),
(3, 1, 'Branco', 'Preto', 'Branco', 3),
(4, 1, 'Rubro-Negro', 'Preto', 'Vermelho', 4);

-- =========================================
-- INSERTS - Partidas
-- =========================================
INSERT INTO Partidas (
    codigo_partida,
    data_hora,
    codigo_mandate,
    codigo_visitante,
    placar,
    codigo_estadio,
    codigo_juiz
)
VALUES
(1, '2025-06-10 16:00:00', 1, 2, '2x1', 1, 'J001'),
(2, '2025-06-12 18:30:00', 3, 4, '1x1', 3, 'J002'),
(3, '2025-06-15 20:00:00', 2, 3, '0x2', 2, 'J003'),
(4, '2025-06-18 21:00:00', 4, 1, '3x2', 4, 'J004');


SELECT
    E.nome equipe,
    U.cor_camisa,
    U.cor_calcao,
    U.cor_meias
FROM
    uniformes U
INNER JOIN equipes E ON
    E.codigo = U.codigo_equipes
WHERE
    E.nome IN(
        "Palmeiras",
        "Corinthians",
        "São Paulo"
    );


SELECT
    P.codigo_partida,
    EM.nome AS mandante,
    EV.nome AS visitante,
    P.placar,
    ES.nome AS estadio,
    P.data_hora
FROM
    partidas AS P
INNER JOIN equipes AS EM
ON
    EM.codigo = P.codigo_mandate
INNER JOIN equipes AS EV
ON
    EV.codigo = P.codigo_visitante
INNER JOIN estadios AS ES
ON
    ES.codigo = P.codigo_estadio
ORDER BY
    P.data_hora;








































