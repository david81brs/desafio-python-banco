-- Consulta quantas contas
-- 2016-12-18
SELECT c.cliente_nome, c.email, c.criado_em, k.numero_conta FROM clientes AS c JOIN contas AS k ON c.id = clientes_id;

