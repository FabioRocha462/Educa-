from rolepermissions.roles import AbstractUserRole

class Secretary(AbstractUserRole):

    available_permissions = {'food_list':True, 'cleaning_list':True,'request_food':True,'request_food_list':True,'request_food_detail':True,'request_food_table':True,'request_cleaning':True,'request_cleaning_list':True,'request_cleaning_detail':True,'request_cleaning_table':True,'create_event':True,'event_list':True,'event_detail':True,'event_update':True,'event_food':True,'event_delete':True,'requeriment_create':True,'requeriment_list':True,'requeriment_detail':True,'memorando_create':True,'memorando_list':True,'memorando_detail':True,'official_create':True,'official_list':True,'official_detail':True}

class ASG(AbstractUserRole):

    available_permissions = {'request_food':True,'request_food_list':True,'request_food_detail':True,'request_food_table':True,'request_cleaning':True,'request_cleaning_list':True,'request_cleaning_detail':True,'request_cleaning_table':True,'requeriment_create':True,'requeriment_list':True,'requeriment_detail':True}

class Coordinator(AbstractUserRole):

    available_permissions = {'create_event':True,'event_list':True,'event_detail':True,'event_update':True,'event_food':True,'event_delete':True,'requeriment_create':True,'requeriment_list':True,'requeriment_detail':True,'memorando_create':True,'memorando_list':True,'memorando_detail':True,'official_create':True,'official_list':True,'official_detail':True}

class Nutricionist(AbstractUserRole):

    available_permissions = {'food_list':True, 'cleaning_list':True,'create_event':True,'event_list':True,'event_detail':True,'event_update':True,'event_food':True,'event_delete':True,'requeriment_create':True,'requeriment_list':True,'requeriment_detail':True,'memorando_create':True,'memorando_list':True,'memorando_detail':True,'official_create':True,'official_list':True,'official_detail':True}

class Fooddivider(AbstractUserRole):

    available_permissions = {'food_list':True, 'cleaning_list':True,'food_form':True,'food_update':True,'food_delete':True,'cleaning_form':True,'cleaning_update':True,'cleaning_delete':True,'requeriment_create':True,'requeriment_list':True,'requeriment_detail':True,'memorando_create':True,'memorando_list':True,'memorando_detail':True,'official_create':True,'official_list':True,'official_detail':True}