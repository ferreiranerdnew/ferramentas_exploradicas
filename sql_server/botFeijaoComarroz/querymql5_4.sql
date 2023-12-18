SELECT * FROM OPERACOES
where DEAL ='2682853264'


SELECT * FROM OPERACOES
                    WHERE DEAL_VENDA IS NULL
                    AND STATUS_COMPRA ='S'
                    AND STATUS_VENDA ='S'
                    and PAPEL ='CMIG4F'
                    order by DEAL
                    
                    
UPDATE OPERACOES
                                            SET STATUS_COMPRA = 'F',
                                            DEAL_VENDA ='123456',
                                            Preco_Atual=13.32,
                                            STATUS_VENDA ='N',
                                            DATA_FIM = CONVERT(VARCHAR(8), GETDATE(), 112)
                                        WHERE PAPEL ='CMIG4F'
                                        AND DEAL ='2682753748' 
                                        
SELECT * FROM OPERACOES
                                WHERE PAPEL = 'QUAL3F'
                                --AND STATUS_COMPRA ='N'
                                AND DEAL_VENDA IS NULL
                                --AND DEAL ='2686818106'
                                --AND VALOR_MEDIO =7.48
                                GROUP BY PAPEL,STATUS_COMPRA
                                
                                
UPDATE OPERACOES
                                        SET STATUS_COMPRA = 'S'
                                WHERE PAPEL = 'DXCO3F'
                                AND STATUS_COMPRA ='N'
                                AND DEAL_VENDA IS NULL
                                AND DEAL ='2686818106'