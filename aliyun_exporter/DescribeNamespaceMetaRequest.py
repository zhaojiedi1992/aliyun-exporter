from aliyunsdkcms.request.v20190101.DescribeProjectMetaRequest import DescribeProjectMetaRequest as AliyunDescribeProjectMetaRequest

class DescribeNamespaceMetaRequest(AliyunDescribeProjectMetaRequest):
    def get_Namespace(self):
        return self.get_query_params().get('Namespace')

    def set_Namespace(self):
        return self.get_query_params().set('Namespace')