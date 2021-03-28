from config.public_data import *
#from utils.ParseExcel import ParseExcel

class WriteTestResult(object):
    def __init__(self):
        pass
    @classmethod
    def write(self,wbObject,sheetObject,responseData,errorKey,rowNum):
        try:
            #写响应body
            wbObject.writeCell(sheet=sheetObject, content="%s" %responseData,
        rowNo = rowNum, colsNo = CASE_status)

            #写校验结果状态及错误信息列
            if errorKey:
                wbObject.writeCell(sheet=sheetObject, content="failed",rowNo=rowNum, colsNo=CASE_status)
                wbObject.writeCell(sheet=sheetObject, content="%s" %errorKey,rowNo=rowNum, colsNo=CASE_errorInfo)
            else:
                wbObject.writeCell(sheet=sheetObject, content="pass", rowNo=rowNum, colsNo=CASE_status)
                wbObject.writeCell(sheet=sheetObject, content="", rowNo=rowNum, colsNo=CASE_errorInfo)

        except Exception as err:
            raise err