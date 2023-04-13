from flask import jsonify

RESULT_SUCCESS = "Success"
RESULT_ERROR = "Error"


class WebResult(object):
    def __init__(self, code, message, data):
        self.message = message
        self.code = code
        self.data = data

    def to_dict(self):
        d = {'code': self.code, "data": self.data}
        if self.message:
            d["message"] = self.message
        return d

    def model_2_json(self):
        d = {'code': self.code, "data": self.data}
        if self.message:
            d["message"] = self.message
        return d

    @staticmethod
    def success(data):
        return jsonify(WebResult(RESULT_SUCCESS, None, data).to_dict())

    @staticmethod
    def list(total, data_list, remark_dict=None):
        return jsonify(WebResult(RESULT_SUCCESS, None, {
            "total": total, "list": data_list, 'remark_dict': remark_dict
        }).to_dict())

    @staticmethod
    def error(message, data=None):
        return jsonify(WebResult(RESULT_ERROR, message, data).to_dict())
