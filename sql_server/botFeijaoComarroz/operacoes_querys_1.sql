SELECT * FROM OPCOES_TRAVAS
where status = 'A'
AND papel ='VALE3'
and pedido =6


ALTER TABLE OPCOES_TRAVAS
ADD op_pr_new float;

UPDATE OPCOES_TRAVAS
SET op_pr_new = 
    CASE 
        WHEN tr_type = 's' THEN -op_pr
        ELSE op_pr
    END
WHERE status = 'A'
AND papel = 'VALE3';


SELECT pedido, papel,op_type, sum(op_pr_new) as op_pr_new FROM OPCOES_TRAVAS
where status = 'A'
AND papel ='VALE3'
and pedido =6
group by pedido, papel,op_type



