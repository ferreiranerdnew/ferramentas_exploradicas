select DATA_INICIO,	PAPEL,	QUANTIDADE,	VALOR_MEDIO,	TOTAL_GASTO	,TOTAL_RETORNO,	Preco_Atual
 from OPEHIST
where PAPEL ='BRAP4F'
ORDER BY VALOR_MEDIO

--61,74

select PAPEL ,SUM(TOTAL_GASTO) AS TOTAL_GASTO, SUM(TOTAL_RETORNO) TOTAL_RETORNO, SUM(QUANTIDADE) AS QUANTIDADE  from OPEHIST
--where PAPEL ='CSNA3F'
GROUP BY PAPEL
ORDER BY VALOR_MEDIO