CREATE TABLE IF NOT EXISTS produto (
    produto_id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT NOT NULL,
    preco FLOAT NOT NULL
);

INSERT INTO produto (nome, descricao, preco) VALUES 
('Produto Teste', 'Descrição do produto teste.', 100.0);
