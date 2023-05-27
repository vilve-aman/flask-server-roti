import json
import uuid


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Only for analysis Purpose
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class RunLogs:
    def __init__(self, routeId, logId, completeList):
        self.routeId = routeId
        self.runlogId = logId or str(uuid.uuid4())
        self.completeList = completeList or []

    def __repr__(self):
        return f'routeId : {self.routeId}   runLogId : {self.runlogId}    completeList : {self.completeList}'

    def get_obj(self):
        obj_dict = {"routeId": self.routeId, "completeList": self.completeList, "runlogId": self.runlogId}
        # print(obj_dict)
        return obj_dict

    def get_runlog_id(self):
        return self.runlogId

# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #   Setter Function
# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# #   Getter Function
# # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

