WITH MinValues AS (
                        SELECT
                            PAPEL,
                            MIN(VALOR_MEDIO) AS MIN_VALOR_MEDIO
                        FROM OPERACOES  with(nolock)
                        WHERE STATUS_COMPRA <> 'F'
                            AND DEAL_VENDA IS NULL
                        GROUP BY PAPEL
                    )
                    SELECT
                        o.PAPEL,
                        o.VALOR_MEDIO,
                        mv.MIN_VALOR_MEDIO,
                        CONVERT(VARCHAR, CONVERT(DATE, STUFF(STUFF(o.DATA_INICIO, 5, 0, '-'), 8, 0, '-')), 103) AS DATA_VALOR_MINIMO
                    FROM OPERACOES o with(nolock)
                    INNER JOIN MinValues mv ON o.PAPEL = mv.PAPEL AND o.VALOR_MEDIO = mv.MIN_VALOR_MEDIO
                    WHERE o.STATUS_COMPRA <> 'F'
                        AND o.DEAL_VENDA IS NULL;
                        
                        
CREATE TABLE OPERACOES_OPCOES (
DATA_INICIO AS CONVERT(VARCHAR(8), GETDATE(), 112),
PAPEL VARCHAR(255),
QUANTIDADE INT,
VALOR_MEDIO FLOAT,
TOTAL_RETORNO FLOAT,
Preco_Atual FLOAT,
STATUS_VENDA CHAR(1),
STATUS_COMPRA CHAR(1),
DATA_VENCIMENTO [varchar](8)
);

SELECT * FROM OPERACOES