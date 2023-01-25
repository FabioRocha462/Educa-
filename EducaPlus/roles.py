from rolepermissions.roles import AbstractUserRole

class Secretary(AbstractUserRole):

    available_permissions = {'food_list':True, 'cleaning_list':True,'request_food':True,'request_food_list':True,'request_food_detail':True,'request_food_table':True,'request_cleaning':True,'request_cleaning_list':True,'request_cleaning_detail':True,'request_cleaning_table':True}

class ASG(AbstractUserRole):

    available_permissions = {'food_list':True, 'cleaning_list':True,'request_food':True,'request_food_list':True,'request_food_detail':True,'request_food_table':True,'request_cleaning':True,'request_cleaning_list':True,'request_cleaning_detail':True,'request_cleaning_table':True}