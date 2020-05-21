# -*- coding: utf-8 -*-
import sqlite3
from dbInstance import *

'''
this is the first version, add exception handle like query null and so on later
'''

'''################################
                room
##################################'''
def insertRoom(room) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'roomMessage'
    attrs = 'roomNo, roomIdx_x, roomIdx_y'
    values = (Utils.toStr(str(room.roomNo)) + ',' + str(room.roomIdx_x) + ',' + str(room.roomIdx_y))
    cursor.execute(Utils.insertSql.replace('_TABLE',table).replace('_ATTRS',attrs).replace('_VALUES',values))
    connect.commit()
    connect.close()

def queryRoom(roomNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'roomMessage'
    condition = ('roomNo = ' + Utils.toStr(roomNo))
    cursor.execute(Utils.querySql.replace('_TABLE',table).replace('_CONDITION',condition))
    room = cursor.fetchone()
    connect.close()
    return Room(room[0], room[1], room[2])

def updateRoom(room) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'roomMessage'
    # primary key cannot update
    updateStm = Utils.toUdeStm('roomIdx_x', room.roomIdx_x) + ',' + Utils.toUdeStm('roomIdx_y' , room.roomIdx_y) 
    condition = ('roomNo = ' + Utils.toStr(room.roomNo))
    cursor.execute(Utils.updateSql.replace('_TABLE',table).replace('_UPDATESTM', updateStm).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

def deleteRoom(roomNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'roomMessage'
    condition = ('roomNo = ' + Utils.toStr(roomNo))
    cursor.execute(Utils.deleteSql.replace('_TABLE',table).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

'''################################
                robot
##################################'''
def insertRobot(robot) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'robotMessage'
    attrs = 'robotNo, robotState, robotIdx_x, robotIdx_y, robotPower'
    values = (Utils.toStr(str(robot.robotNo)) + ',' + str(robot.robotState) +',' +str(robot.robotIdx_x) + ',' + str(robot.robotIdx_y)) + ',' + str(robot.robotPower)
    cursor.execute(Utils.insertSql.replace('_TABLE',table).replace('_ATTRS',attrs).replace('_VALUES',values))
    connect.commit()
    connect.close()

def queryRobot(robotNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'robotMessage'
    condition = ('robotNo = ' + Utils.toStr(robotNo))
    cursor.execute(Utils.querySql.replace('_TABLE',table).replace('_CONDITION',condition))
    robot = cursor.fetchone()
    connect.close()
    return Robot(robot[0], robot[1], robot[2], robot[3], robot[4])

def updateRobot(robot) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'robotMessage'
    # primary key cannot update
    updateStm = Utils.toUdeStm('robotState', robot.robotState) + ',' + Utils.toUdeStm('robotIdx_x', robot.robotIdx_x) + ',' + Utils.toUdeStm('robotIdx_y', robot.robotIdx_y) + ','+ Utils.toUdeStm('robotPower', robot.robotPower)
    condition = ('robotNo = ' + Utils.toStr(robot.robotNo))
    cursor.execute(Utils.updateSql.replace('_TABLE',table).replace('_UPDATESTM', updateStm).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

def deleteRobot(robotNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'robotMessage'
    condition = ('robotNo = ' + Utils.toStr(robotNo))
    cursor.execute(Utils.deleteSql.replace('_TABLE',table).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

'''################################
                goods
##################################'''
def insertGoods(goods) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'goodsMessage'
    attrs = 'goodsNo, goodsName, goodsIdx_x, goodsIdx_y'
    values = (Utils.toStr(str(goods.goodsNo)) + ',' + Utils.toStr(str(goods.goodsName)) +',' +str(goods.goodsIdx_x) + ',' + str(goods.goodsIdx_y))
    cursor.execute(Utils.insertSql.replace('_TABLE',table).replace('_ATTRS',attrs).replace('_VALUES',values))
    connect.commit()
    connect.close()

def queryGoods(goodsNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'goodsMessage'
    condition = ('goodsNo = ' + Utils.toStr(goodsNo))
    cursor.execute(Utils.querySql.replace('_TABLE',table).replace('_CONDITION',condition))
    goods = cursor.fetchone()
    connect.close()
    return Goods(goods[0], goods[1], goods[2], goods[3])

def updateGoods(goods) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'goodsMessage'
    # primary key cannot update
    updateStm = Utils.toUdeStm('goodsName', Utils.toStr(goods.goodsName)) + ',' + Utils.toUdeStm('goodsIdx_x', goods.goodsIdx_x) + ',' + Utils.toUdeStm('goodsIdx_y', goods.goodsIdx_y)
    condition = ('goodsNo = ' + Utils.toStr(goods.goodsNo))
    cursor.execute(Utils.updateSql.replace('_TABLE',table).replace('_UPDATESTM', updateStm).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

def deleteGoods(goodsNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'goodsMessage'
    condition = ('goodsNo = ' + Utils.toStr(goodsNo))
    cursor.execute(Utils.deleteSql.replace('_TABLE',table).replace('_CONDITION',condition))
    connect.commit()
    connect.close()


'''################################
                instruction
##################################'''
def insertIns(ins) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'insMessage'
    attrs = 'insNo, insType, insRoomNo, insGoodsNo'
    values = (Utils.toStr(str(ins.insNo)) + ',' + str(ins.insType) +',' + Utils.toStr(str(ins.insRoomNo)) + ',' + Utils.toStr(str(ins.insGoodsNo)))
    cursor.execute(Utils.insertSql.replace('_TABLE',table).replace('_ATTRS',attrs).replace('_VALUES',values))
    connect.commit()
    connect.close()

def queryIns(insNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'insMessage'
    condition = ('insNo = ' + Utils.toStr(insNo))
    cursor.execute(Utils.querySql.replace('_TABLE',table).replace('_CONDITION',condition))
    ins = cursor.fetchone()
    connect.close()
    return Instruction(ins[0], ins[1], ins[2], ins[3])

def updateIns(ins) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'insMessage'
    # primary key cannot update
    updateStm = Utils.toUdeStm('insType', ins.insType) + ',' + Utils.toUdeStm('insRoomNo', Utils.toStr(ins.insRoomNo)) + ',' + Utils.toUdeStm('insGoodsNo', Utils.toStr(ins.insGoodsNo))
    condition = ('insNo = ' + Utils.toStr(ins.insNo))
    cursor.execute(Utils.updateSql.replace('_TABLE',table).replace('_UPDATESTM', updateStm).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

def deleteIns(insNo) :
    connect = sqlite3.connect(Utils.dbName)
    cursor = connect.cursor()
    table = 'insMessage'
    condition = ('insNo = ' + Utils.toStr(insNo))
    cursor.execute(Utils.deleteSql.replace('_TABLE',table).replace('_CONDITION',condition))
    connect.commit()
    connect.close()

