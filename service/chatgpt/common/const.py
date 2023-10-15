import requests
# bot_type
OPEN_AI = "openAI"
CHATGPT = "chatGPT"
BAIDU = "baidu"
XUNFEI = "xunfei"
CHATGPTONAZURE = "chatGPTOnAzure"
LINKAI = "linkai"

VERSION = "1.3.0"

CLAUDEAI = "claude"
MODEL_LIST = ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "wenxin", "xunfei","claude"]

URL = "10.221.38.232:8080"

FUNCTIONS=[{
        "name":"getProjectByName",
        "description":"根据项目名字查询信息",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名称，需要保留项目两个字"},
                },
        "required":["projectName"],
        },
        }, 
        {
        "name":"listUserPlan",
        "description":"填写项目工时",
        "parameters":{
        "type":"object",
        "properties":{
        # "headers":{"type":"string","description":"请求头信息"},
                },
        "required":[],
        },
        },
        {"name":"projectList",
        "description":"修改项目计划",
        "parameters":{
        "type":"object",
        "properties":{
        # "headers":{"type":"string","description":"请求头信息"},
                },
        "required":[],
        },},
        {"name":"riskListBytName",
        "description":"根据项目名字更新风险信息",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
        "type": {"type":"string","description":"风险种类"}
                },
        "required":["projectName", "type"],
        },},
        {"name":"projectListByName",
        "description":"根据项目名字获取项目列表详情",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
                },
        "required":["projectName"],
        },},
        {"name":"updateProjectRisk",
        "description":"根据项目名字修改项目的整体风险，风险等级低为0，风险等级中等为1，风险等级高为2",
        "parameters":{
        "type":"object",
        "properties":{
        "riskLevel":{"type":"number","description":"整体风险等级，用数字表示"},
                },
        "required":["riskLevel"],
        },},
        {"name":"projectListByRiskLevel",
        "description":"根据整体风险等级查询项目，风险等级低为0，风险等级中等为1，风险等级高为2",
        "parameters":{
        "type":"object",
        "properties":{
        "riskLevel":{"type":"string","description":"整体风险等级，用数字表示"},
                },
        "required":['riskLevel'],
        },},
        {"name":"addRiskByProjectName",
        "description":"根据名字增加风险明细",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"名字"},
                },
        "required":["projectName"],
        },},
        {"name":"deleteRiskByProjectName",
        "description":"根据名字删除风险明细",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"名字"},
        "type":{"type":"string","description":"要删除的风险明细名"},
                },
        "required":["projectName", 'type'],
        },},
        {"name":"deleteRiskByProjectName",
        "description":"根据名字删除风险明细",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"名字"},
        "type":{"type":"string","description":"要删除的风险明细名"},
                },
        "required":["projectName", 'type'],
        },},
        {"name":"queryListByName",
        "description":"根据名字查询项目交付清单",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"名字"},
                },
        "required":["projectName"],
        },},
        {"name":"deleteProductByProjectNam",
        "description":"根据项目名字删除项目下对应的产品明细",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
        "productName": {"type":"string","description":"产品名字"},
                },
        "required":["projectName", "productName"],
        },},
        {"name":"queryBudgetByProjectName",
        "description":"根据项目名字查询项目预算",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
                },
        "required":["projectName"],
        },},
        {"name":"editBudgetCostByProjectName",
        "description":"根据项目名字编辑预算成本",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
        "type": {"type":"string","description":"预算成本类型"},
        "ratio": {"type":"number","description":"成本增加或减少的百分比"}
                },
        "required":["projectName",'type','ratio'],
        },},
        {"name":"planListByProjectName",
        "description":"根据项目名字（或里程碑名字）查询项目计划下的任务列表",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
        "milestoneName": {"type":"string","description":"里程碑名字"},
                },
        "required":["projectName",'milestoneName'],
        },},
        {"name":"getCostAll",
        "description":"根据项目名字查询项目下的实际成本",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
                },
        "required":["projectName"],
        },},
        {"name":"addMilestone",
        "description":"根据项目名字添加里程碑",
        "parameters":{
        "type":"object",
        "properties":{
        "projectName":{"type":"string","description":"项目名字"},
                },
        "required":["projectName"],
        },},
        ]

# def getProjectByName(projectName: str):
#     res = requests.get(f'http://{URL}/api/v1/project/getByName', params={'projectName': projectName})
#     if res.json()['code'] != 0:
#         res = requests.get('http://{URL}/api/v1/project/getByName', params={'projectName': f"{projectName}项目"})
#     return res.text

# def listUserPlan(headers):
#     res = requests.get('http://{URL}/api/v1/project/getByName', headers=headers)
#     return res.text
