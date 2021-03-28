from config.public_data import REQUEST_DATA,RESPONSE_DATA

class RelyDataStore(object):
    def __init__(self):
        pass

    @classmethod
    def do(self,storePoint,apiName, caseId,request_source,responce_source):
        type_map = {"request":REQUEST_DATA,"response":RESPONSE_DATA}
        source_map = {"request":request_source,"response":responce_source}
        for key,value in storePoint.items():
                #说明应该存入公共变量REQUEST_DATA中
            for i in value:
                #说明此处默认传入的数据源都是一层dict类型
                temp = source_map[key].get(i,"")
                #print("***************temp:",temp)
                if temp:
                    if apiName not in type_map[key]:
                        #说明存储数据的结构还未生成，需要指明数据存储结构
                        type_map[key][apiName] = {str(caseId):{i:temp}}
                    else:
                        #说明存储数据结构中最外层结构式完整的
                        if str(caseId) in type_map[key][apiName]:
                            type_map[key][apiName][str(caseId)][i]= temp
                        else:
                            type_map[key][apiName][str(caseId)] = {i:temp}
                else:
                    print("&&请求参数中不存在字段%s" %(key))
"""
    @classmethod
    def do(self,storePoint,apiName, caseId,request_source,responce_source):
        for key,value in storePoint.items():
            if key == "request":
                #说明应该存入公共变量REQUEST_DATA中
                for i in value:
                    #说明此处默认传入的数据源都是一层dict类型
                    temp = request_source.get(i,"")
                    print("***************temp:",temp)
                    if temp:
                        if apiName not in REQUEST_DATA:
                            #说明存储数据的结构还未生成，需要指明数据存储结构
                            REQUEST_DATA[apiName] = {str(caseId):{i:temp}}
                        else:
                            #说明存储数据结构中最外层结构式完整的
                            if str(caseId) in REQUEST_DATA[apiName]:
                                REQUEST_DATA[apiName][str(caseId)][i]= temp
                            else:
                                REQUEST_DATA[apiName][str(caseId)] = {i:temp}
                    else:
                        print("&&请求参数中不存在字段:",i)

            elif key == "response":
                #说明应该存入公共变量RESPONSE_DATA中
                for j in value:
                    # 说明此处默认传入的数据源都是一层dict类型
                    r_temp = response_source.get(j, "")

                    if r_temp:
                        if apiName not in RESPONSE_DATA:
                            # 说明存储数据的结构还未生成，需要指明数据存储结构
                            RESPONSE_DATA[apiName] = {str(caseId): {j: r_temp}}
                        else:
                            # 说明存储数据结构中最外层结构式完整的
                            if str(caseId) in RESPONSE_DATA[apiName]:
                                RESPONSE_DATA[apiName][str(caseId)][j] = r_temp
                            else:
                                RESPONSE_DATA[apiName][str(caseId)] = {j: r_temp}
                    else:
                        print("**请求参数中不存在字段:", j)
"""



if __name__ == "__main__":
    storePoint = {"request":["username","password"],"response":["code"]}
    apiName = "register"
    caseId = 1
    request_source = {"username":"lisi1231","password":"wcx123wac1","email":"wcx@qq.com"}
    response_source = {'username': 'zhwu1231', 'code': '01'}
    RelyDataStore.do(storePoint, apiName, caseId, request_source, response_source)
    print(REQUEST_DATA)
    print(RESPONSE_DATA)