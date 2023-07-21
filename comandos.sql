show databases;
use nfse;
show tables;
select * from teste;
describe teste;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(10, 2),
    estoque INT
);

INSERT INTO produtos (nome, descricao, preco, estoque)
VALUES ('Produto A', 'Descrição do Produto A', 49.99, 100);
INSERT INTO produtos (nome, descricao, preco, estoque)
VALUES ('Produto B', 'Descrição do Produto B', 39.99, 50);
INSERT INTO produtos (nome, descricao, preco, estoque)
VALUES ('Produto C', 'Descrição do Produto C', 29.99, 200);
INSERT INTO produtos (nome, descricao, preco, estoque)
VALUES ('Produto D', 'Descrição do Produto D', 19.99, 75);

select * from produtos;

