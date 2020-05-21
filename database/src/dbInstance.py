class Room :
    def __init__(self, rNo, rIdx_x, rIdx_y) :
        self.roomNo = rNo
        self.roomIdx_x = rIdx_x
        self.roomIdx_y = rIdx_y
    

class Robot :
    def __init__(self, rNo, rState, rIdx_x, rIdx_y, rPower) :
        self.robotNo = rNo
        self.robotState = rState
        self.robotIdx_x = rIdx_x
        self.robotIdx_y = rIdx_y
        self.robotPower = rPower


class Goods :
    def __init__(self, gNo, gName, gIdx_x, gIdx_y) :
        self.goodsNo = gNo
        self.goodsName = gName
        self.goodsIdx_x = gIdx_x
        self.goodsIdx_y = gIdx_y

class Instruction :
    def __init__(self, iNo, iType, iRoomNo, iGoodsNo) :
        self.insNo = iNo
        self.insType = iType
        self.insRoomNo = iRoomNo
        self.insGoodsNo = iGoodsNo
    

class Utils :
    dbName = 'ROSDATABASE.db'

    insertSql = '''
        INSERT INTO _TABLE
        (_ATTRS)
        VALUES
        (_VALUES)
    '''

    querySql = '''
        SELECT *
        FROM _TABLE
        WHERE
        _CONDITION
    '''

    deleteSql = '''
        DELETE
        FROM _TABLE
        WHERE
        _CONDITION
    '''

    updateSql = '''
        UPDATE _TABLE
        SET _UPDATESTM
        WHERE
        _CONDITION
    '''

    @classmethod
    def toStr(cls, rstr) :
        return '\'' + str(rstr) + '\''
    
    @classmethod
    def toUdeStm(cls, attr, value) :
        return str(attr)+ '=' + str(value)
