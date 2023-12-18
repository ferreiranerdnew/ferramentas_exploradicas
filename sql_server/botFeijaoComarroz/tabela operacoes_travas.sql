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
)

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra) VALUES (
                              1,'PETR4','c',36.77,'s',0.76,'A','20240119','20231218')

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra) VALUES (
                            1,'PETR4','c',37.27,'b',0.60,'A','20240119','20231218')
                            
INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra) VALUES (
                            1,'PETR4','p',34.52,'s',0.51,'A','20240119','20231218')

INSERT INTO OPCOES_TRAVAS (pedido,papel,op_type,strike,tr_type,op_pr,status,data_necimento,data_compra) VALUES (
                            1,'PETR4','p',34.02,'b',0.41,'A','20240119','20231218')