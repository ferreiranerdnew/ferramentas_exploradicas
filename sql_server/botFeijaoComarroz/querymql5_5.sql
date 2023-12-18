select * from EMPVINICIAL
where EMPRESAS IN('CMIN3F')

delete from EMPVINICIAL
where EMPRESAS IN('CMIN3F')

SELECT * FROM OPERACOES
where PAPEL  IN('CMIN3F')

delete from OPERACOES
where PAPEL  = 'BMGB4F'

select * from EMPVINICIAL
order by VALOR_INI