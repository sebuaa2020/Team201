# -*- coding: utf-8 -*-
import sqlite3
from dbInstance import *

if __name__ == "__main__":
    connect = sqlite3.connect(Utils.dbName)

    c = connect.cursor()

    c.execute('''
        CREATE TABLE roomMessage(
            roomNo varchar(50) PRIMARY KEY,
            roomIdx_x DOUBLE,
            roomIdx_y DOUBLE
        )
    ''')

    c.execute('''
        CREATE TABLE robotMessage(
            robotNo varchar(50) PRIMARY KEY,
            robotState int,
            robotIdx_x DOUBLE,
            robotIdx_y DOUBLE,
            robotPower int
        )
    ''')
    # add constraint to rState and rPower

    c.execute('''
        CREATE TABLE goodsMessage(
            goodsNo varchar(50) PRIMARY KEY,
            goodsName varchar(50),
            goodsIdx_x DOUBLE,
            goodsIdx_y DOUBLE
        )
    ''')


    c.execute('''
        CREATE TABLE insMessage(
            insNo varchar(50) PRIMARY KEY,
            insType int,
            insRoomNo varchar(50),
            insGoodsNo varchar(50),
            FOREIGN KEY (insRoomNo) REFERENCES roomMessage (roomNo),
            FOREIGN KEY (insGoodsNo) REFERENCES goodsMessage (goodsNo)
        )
    ''')
    # add constraint to iType

    connect.commit()
    connect.close()

