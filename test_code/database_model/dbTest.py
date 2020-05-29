import sqlite3
from dbInstance import *
from dbOperation import *

if __name__ == "__main__":
    insertRobot(Robot('R001', 1, 0.0, 0.0, 100))
    insertRoom(Room('F001', 5, 5))
    insertGoods(Goods('G001', 'cola', 88, 99))
    insertIns(Instruction('I001', 1, 'F001', 'G001'))
    
    r = queryRobot('R001')
    print("insert robot succeed",r.robotNo, r.robotState)
    r = queryRoom('F001')
    print("insert room, succeed",r.roomNo, r.roomIdx_x)
    r = queryGoods('G001')
    print("insert goods succeed", r.goodsNo, r.goodsName)
    r = queryIns('I001')
    print("insert instruction succeed",r.insNo, r.insType)
    
    updateRobot(Robot('R001', 2, 1.0, -9.0, 99))
    updateRoom(Room('F001', 1, 1))
    updateGoods(Goods('G001', '7xi', 99, 88))
    updateIns(Instruction('I001', 2, 'F001','G001'))
    
    r = queryRobot('R001')
    print("update robot succeed",r.robotNo, r.robotState)
    r = queryRoom('F001')
    print("update room, succeed",r.roomNo, r.roomIdx_x)
    r = queryGoods('G001')
    print("update goods succeed", r.goodsNo, r.goodsName)
    r = queryIns('I001')
    print("update instruction succeed",r.insNo, r.insType)
    

    deleteRobot('R001')
    deleteRoom('F001')
    deleteGoods('G001')
    deleteIns('I001')

