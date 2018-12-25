"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp_dict = {}
        for i in range(len(employees)):
            emp_dict[employees[i].id] = employees[i]
            
        def dfs(id, emp_dict):
            if not emp_dict[id].subordinates:
                return emp_dict[id].importance
            imp = emp_dict[id].importance
            for i in emp_dict[id].subordinates:
                imp += dfs(i, emp_dict)
            return imp
        
        return dfs(id, emp_dict)
            
            
            
            
            
            
            
            
            
            
