SELECT * FROM OPCOES_TRAVAS
where status = 'A'
AND papel ='VALE3'
and pedido =6


ALTER TABLE OPCOES_TRAVAS
ADD strike_new float;

UPDATE OPCOES_TRAVAS
SET op_pr_new = 
    CASE 
        WHEN tr_type = 's' THEN -op_pr
        ELSE op_pr
    END,
    strike_new = 
    CASE 
        WHEN tr_type = 's' THEN -strike
        ELSE strike
    END

SELECT pedido, papel,op_type, sum(op_pr_new) as op_pr_new,sum(strike_new) as strike_new,(sum(op_pr_new)/sum(strike_new))*100 as diff  FROM OPCOES_TRAVAS
where status = 'A'
AND papel ='VALE3'
and pedido =6
group by pedido, papel,op_type

SELECT pedido, papel, sum(op_pr_new) as op_pr_new  FROM OPCOES_TRAVAS
where status = 'A'
--AND papel ='VALE3'
--and pedido =6
group by pedido, papel


SELECT pedido, papel,op_type, sum(op_pr_new) as op_pr_new,sum(strike_new) as strike_new,(sum(op_pr_new)/sum(strike_new))*100 as diff  FROM OPCOES_TRAVAS
where status = 'A'
AND papel ='JBSS3'
---and pedido =6
group by pedido, papel,op_type

