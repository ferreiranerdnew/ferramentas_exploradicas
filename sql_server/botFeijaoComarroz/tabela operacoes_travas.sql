SELECT * FROM OPCOES_TRAVAS

drop table OPCOES_TRAVAS

CREATE TABLE OPCOES_TRAVAS(
pedido int,
papel varchar (15),
op_type char (1),
strike float,
tr_type char(1),
op_pr float,
status char(1),
data_necimento varchar(8),
data_compra varchar(8),
price_montagem float
)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                              1,'PETR4','c',36.77,'s',0.76,'A','20240119','20231218',35.78)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            1,'PETR4','c',37.27,'b',0.60,'A','20240119','20231218',35.78)
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            1,'PETR4','p',34.52,'s',0.51,'A','20240119','20231218',35.78)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            1,'PETR4','p',34.02,'b',0.41,'A','20240119','20231218',35.78)
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                              2,'ABEV3','c',14.85,'s',0.19,'A','20240119','20231218',14.51)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            2,'ABEV3','c',14.60,'b',0.31,'A','20240119','20231218',14.51)                             
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            3,'BMGB4','p',2.70,'b',0.06,'A','20240119','20231218',3.33)     
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            4,'MGLU3','p',2.25,'b',0.28,'A','20240119','20231218',2.23)    
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            4,'MGLU3','c',2.25,'b',0.27,'A','20240119','20231218',2.23)
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                           5,'SUZB3','c',53.01,'s',1.26,'A','20240119','20231218',52.52)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            5,'SUZB3','c',54.01,'b',0.88,'A','20240119','20231218',52.52)
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            5,'SUZB3','p',50.51,'s',0.40,'A','20240119','20231218',52.52)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            5,'SUZB3','p',49.76,'b',0.33,'A','20240119','20231218',52.52)                            
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                           6,'VALE3','c',76.82,'s',1.01,'A','20240119','20231218',74.11)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            6,'VALE3','c',77.32,'b',0.89,'A','20240119','20231218',74.11)
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            6,'VALE3','p',71.82,'s',0.73,'A','20240119','20231218',74.11)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            6,'VALE3','p',71.32,'b',0.63,'A','20240119','20231218',74.11)                           
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            7,'VALE3','p',70.32,'b',0.44,'A','20240119','20231218',74.11)  
                           
                           
                           
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                           8,'BRKM5','c',19.25,'s',0.65,'A','20240119','20231219',18.63)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            8,'BRKM5','c',20.25,'b',0.38,'A','20240119','20231219',18.63)
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            8,'BRKM5','p',17.75,'s',0.46,'A','20240119','20231219',18.63)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra,price_montagem) VALUES (
                            8,'BRKM5','p',16.75,'b',0.28,'A','20240119','20231219',18.63)  
                            
                            
                            
SELECT pedido, papel FROM OPCOES_TRAVAS
where status = 'A'
group by pedido, papel


SELECT * FROM OPCOES_TRAVAS

DELETE FROM OPCOES_TRAVAS
