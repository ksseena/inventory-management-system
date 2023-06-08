from django.contrib import admin
from django.urls import path, include
from . import views
from .import adminViews, UserViews, ToolView


urlpatterns = [
    path('', views.loginPage, name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),

    path('admin_home/', adminViews.admin_home, name="admin_home"),

    path('add_user/', adminViews.add_user, name="add_user"),
    path('add_user_save/', adminViews.add_user_save, name="add_user_save"),
    path('manage_users/', adminViews.manage_user, name="manage_user"),
    path('edit_user/<staff_id>/', adminViews.edit_user, name="edit_user"),
    path('edit_user_save/', adminViews.edit_user_save, name="edit_user_save"),
    path('delete_user/<staff_id>/', adminViews.delete_user, name="delete_user"),
 
    path('add_toolroomuser/', adminViews.add_toolroomuser, name="add_toolroomuser"),
    path('add_toolroomuser_save/', adminViews.add_toolroomuser_save, name="add_toolroomuser_save"),
    path('manage_toolroomuser/', adminViews.manage_toolroomuser, name="manage_toolroomuser"),
    path('edit_toolroomuser/<ptsuser_id>/', adminViews.edit_toolroomuser, name="edit_toolroomuser"),
    path('edit_toolroomuser_save/', adminViews.edit_toolroomuser_save, name="edit_toolroomuser_save"),
    path('delete_toolroomuser/<ptsuser_id>/', adminViews.delete_toolroomuser, name="delete_toolroomuser"),


    path('check_email_exist/', adminViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', adminViews.check_username_exist, name="check_username_exist"),
    
    path('admin_profile/', adminViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', adminViews.admin_profile_update, name="admin_profile_update"),

    
    path('add_store_data2/', adminViews.add_store_data2, name="add_store_data2"),
    path('add_store_data2_save/', adminViews.add_store_data2_save, name="add_store_data2_save"),
    path('admin_store_data2/', adminViews.admin_manage_store_data2, name="admin_manage_store_data2"),
    path('edit_store_data2/<id>', adminViews.edit_store_data2, name="edit_store_data2"),
    path('edit_store_data2_save/', adminViews.edit_store_data2_save, name="edit_store_data2_save"),

    path('add_store_data/', adminViews.add_store_data, name="add_store_data"),
    path('add_store_data_save/', adminViews.add_store_data_save, name="add_store_data_save"),
    path('admin_store_data/', adminViews.admin_manage_store_data, name="admin_manage_store_data"),
    path('edit_store_data/<id>', adminViews.edit_store_data, name="edit_store_data"),
    path('edit_store_data_save/', adminViews.edit_store_data_save, name="edit_store_data_save"),
    path('import_data1/', adminViews.import_data1, name="import_data1"),
    path('import_data2/', adminViews.import_data2, name="import_data2"),
    path('receivep91<int:receive_id>/', adminViews.receivep91, name="receivep91"),
    path('receivep91<int:receive_id>/receive_save_p91', adminViews.receive_save_p91, name="receive_save_p91"), 
    path('receivep75<int:receive_id>/', adminViews.receiveP75, name="receiveP75"),
    path('receivep75<int:receive_id>/receive_save_P75', adminViews.receive_save_P75, name="receive_save_P75"), 

    path('admin_manage_user_requests/', adminViews.admin_manage_user_requests, name="admin_manage_user_requests"),
    path('admin_manage_user_requests2/', adminViews.admin_manage_user_requests2, name="admin_manage_user_requests2"),
    path('admin_manage_issueitemsP75/', adminViews.admin_manage_issueitems2, name="admin_manage_issueitems2"),
    path('admin_manage_issueitemsP91/', adminViews.admin_manage_issueitems1, name="admin_manage_issueitems1"),
    path('admin_manage_receive_P91_data/', adminViews.admin_manage_receive_P91_data, name="admin_manage_receive_P91_data"),
    path('admin_manage_receive_P75_data/', adminViews.admin_manage_receive_P75_data, name="admin_manage_receive_P75_data"),
    path('admin_user_request_approve/<data_id>', adminViews.admin_user_request_approve, name="admin_user_request_approve"),
    path('admin_user_request_reject/<data_id>', adminViews.admin_user_request_reject, name="admin_user_request_reject"),
    path('admin_user_request2_approve/<data_id>', adminViews.admin_user_request2_approve, name="admin_user_request2_approve"),
    path('admin_user_request2_reject/<data_id>', adminViews.admin_user_request2_reject, name="admin_user_request2_reject"),
    path('tranferP91toP75<int:trans_id>/', adminViews.Tranfer_item, name="Tranfer_item"),
    path('tranferP91toP75<int:trans_id>/Tranfer_Item_Save', adminViews.Tranfer_Item_Save, name="Tranfer_Item_Save"), 
    path('tranferP75toP91<int:trans_id>/', adminViews.Tranfer_item2, name="Tranfer_item2"),
    path('tranferP75toP91<int:trans_id>/Tranfer_Item2_Save', adminViews.Tranfer_Item2_Save, name="Tranfer_Item2_Save"), 
    path('admin_manage_receive_P91_data/', adminViews.admin_manage_receive_P91_data, name="admin_manage_receive_P91_data"),
    path('admin_manage_receive_P75_data/', adminViews.admin_manage_receive_P75_data, name="admin_manage_receive_P75_data"),
    path('admin_manage_tranfer_item_P91toP75/', adminViews.admin_manage_tranfer_item_P91toP75, name="admin_manage_tranfer_item_P91toP75"),
    path('admin_manage_tranfer_item_P75toP91/', adminViews.admin_manage_tranfer_item_P75toP91, name="admin_manage_tranfer_item_P75toP91"),
    


    path('admindetails<int:request_id>/', adminViews.admin_details, name="admin_details"),
    path('admindetails<int:request_id>/admin_transferitm', adminViews.admin_transferitm, name="admin_transferitm"),  

    path('admin_issue<int:request_id>/', adminViews.admin_details2, name="admin_details2"),
    path('admin_issue<int:request_id>/admin_transferitm2', adminViews.admin_transferitm2, name="admin_transferitm2"),  


    path('admin_remark_data/<data_id>', adminViews.admin_remark_data, name="admin_remark_data"),
    path('admin_remark_data_save/', adminViews.admin_remark_data_save, name="admin_remark_data_save"),

    path('admin_remark_data2/<data_id>', adminViews.admin_remark_data2, name="admin_remark_data2"),
    path('admin_remark_data2_save/', adminViews.admin_remark_data2_save, name="admin_remark_data2_save"),

    path('admin_damage1<int:issue_id>/', adminViews.admin_damage1, name="admin_damage1"),
    path('admin_damage1<int:issue_id>/admin_damageitem1', adminViews.admin_damageitem1, name="admin_damageitem1"),
    path('admin_manage_damage_P91_data', adminViews.admin_manage_damage_P91_data, name="admin_manage_damage_P91_data"),

    path('admin_damage2<int:issue_id>/', adminViews.admin_damage2, name="admin_damage2"),
    path('admin_damage2<int:issue_id>/admin_damageitem2', adminViews.admin_damageitem2, name="admin_damageitem2"),
    path('admin_manage_damage_P75_data', adminViews.admin_manage_damage_P75_data, name="admin_manage_damage_P75_data"),

    path('admin_daterange_report', adminViews.admin_daterange_report, name="admin_daterange_report"),
    path('all_report', adminViews.all_report, name="all_report"),
    
    path('admin_daterange_report1', adminViews.admin_daterange_report1, name="admin_daterange_report1"),
    path('all_report1', adminViews.all_report1, name="all_report1"),

    path('approvel_pending_P91', adminViews.approvel_pending_P91, name="approvel_pending_P91"),
    path('issue_pending_P91', adminViews.issue_pending_P91, name="issue_pending_P91"),
    path('issued_done_P91', adminViews.issued_done_P91, name="issued_done_P91"),
    path('reject_P91', adminViews.reject_P91, name="reject_P91"),

    path('approvel_pending_P75', adminViews.approvel_pending_P75, name="approvel_pending_P75"),
    path('issue_pending_P75', adminViews.issue_pending_P75, name="issue_pending_P75"),
    path('issued_done_P75', adminViews.issued_done_P75, name="issued_done_P75"),
    path('reject_P75', adminViews.reject_P75, name="reject_P75"),
   
    path('admin_manage_issueitems1_summary', adminViews.admin_manage_issueitems1_summary, name="admin_manage_issueitems1_summary"),
    path('admin_issue_daterange_summary1', adminViews.admin_issue_daterange_summary1, name="admin_issue_daterange_summary1"),
    path('all_issue_summary1', adminViews.all_issue_summary1, name="all_issue_summary1"),
    path('admin_manage_issueitems1_summaryP75', adminViews.admin_manage_issueitems1_summaryP75, name="admin_manage_issueitems1_summaryP75"),

    path('admin_issue_daterange_summaryP75', adminViews.admin_issue_daterange_summaryP75, name="admin_issue_daterange_summaryP75"),
    path('all_issue_summaryP75', adminViews.all_issue_summaryP75, name="all_issue_summaryP75"),
        
    path('delete_StoreItems/<delete_store>', adminViews.delete_StoreItems, name="delete_StoreItems"),
    path('delete_StoreItems2/<delete_store>', adminViews.delete_StoreItems2, name="delete_StoreItems2"),

    path('final_admin_manage_issueitems1_summaryP91', adminViews.final_admin_manage_issueitems1_summaryP91, name="final_admin_manage_issueitems1_summaryP91"),








    # URLS for User
    
    path('user_home/', UserViews.user_home, name='user_home'),
    path('user-profile/', UserViews.user_profile, name='user_profile'),
    path('user-profile-update/', UserViews.user_profile_update, name="user_profile_update"),
    
    path('add_user_data/', UserViews.add_user_data, name="add_user_data"),
    path('add_user_data_save/', UserViews.add_user_data_save, name="add_user_data_save"),
    path('manage_user_data/', UserViews.manage_user_data, name="manage_user_data"),
    path('manage_store_data_user/', UserViews.manage_store_data_user, name="manage_store_data_user"),
    path('request<int:item_id>/', UserViews.request_item, name="request_item"),
    path('request<int:item_id>/request_item', UserViews.request_item_save, name="request_item_save"),

    path('manage_transaction_user/', UserViews.manage_transaction_user, name="manage_transaction_user"),
    path('manage_transaction2_user/', UserViews.manage_transaction2_user, name="manage_transaction2_user"),



    path('requestP75<int:item_id>/', UserViews.request_item2, name="request_item2"),
    path('requestP75<int:item_id>/request_item2', UserViews.request_item2_save, name="request_item2_save"),
    path('manage_user_data2/', UserViews.manage_user_data2, name="manage_user_data2"),
    path('manage_store_data2_user/', UserViews.manage_store_data2_user, name="manage_store_data2_user"),
    
    path('notification/', UserViews.notification, name="notification"),



    path('user_approvel_pending_P91', UserViews.user_approvel_pending_P91, name="user_approvel_pending_P91"),
    path('user_issue_pending_P91', UserViews.user_issue_pending_P91, name="user_issue_pending_P91"),
    path('user_issued_done_P91', UserViews.user_issued_done_P91, name="user_issued_done_P91"),
    path('user_reject_P91', UserViews.user_reject_P91, name="user_reject_P91"),

    path('user_approvel_pending_P75', UserViews.user_approvel_pending_P75, name="user_approvel_pending_P75"),
    path('user_issue_pending_P75', UserViews.user_issue_pending_P75, name="user_issue_pending_P75"),
    path('user_issued_done_P75', UserViews.user_issued_done_P75, name="user_issued_done_P75"),
    path('user_reject_P75', UserViews.user_reject_P75, name="user_reject_P75"),
 

    # Url for ToolRoom
    
    path('add-notifications/', ToolView.add_notifications, name="add_notifications"),
    
    path('manage_store_data/', ToolView.manage_store_data, name="manage_store_data"),
    path('manage_store_data2/', ToolView.manage_store_data2, name="manage_store_data2"),
    path('manage_user_requests/', ToolView.manage_user_requests, name="manage_user_requests"),
    path('manage_user_requests2/', ToolView.manage_user_requests2, name="manage_user_requests2"),
    path('manage_transaction/', ToolView.manage_transaction, name="manage_transaction"),
    
    path('user_request_approve/<data_id>', ToolView.user_request_approve, name="user_request_approve"),
    path('user_request_reject/<data_id>', ToolView.user_request_reject, name="user_request_reject"),
    path('user_request2_approve/<data_id>', ToolView.user_request2_approve, name="user_request2_approve"),
    path('user_request2_reject/<data_id>', ToolView.user_request2_reject, name="user_request2_reject"),
   



    path('remark_data/<data_id>', ToolView.remark_data, name="remark_data"),
    path('remark_data_save/', ToolView.remark_data_save, name="remark_data_save"),

    path('remark_data2/<data_id>', ToolView.remark_data2, name="remark_data2"),
    path('remark_data2_save/', ToolView.remark_data2_save, name="remark_data2_save"),


   
    path('ItemP91<int:request_id>/', ToolView.details1, name="details1"),
    path('ItemP91<int:request_id>/transferitm1', ToolView.transferitm1, name="transferitm1"),  

    path('tranferred_items_P91_to_P75/', ToolView.manage_tranfer_item_P91toP75, name="manage_tranfer_item_P91toP75"),
    path('tranferred_items_P75_to_P91/', ToolView.manage_tranfer_item_P75toP91, name="manage_tranfer_item_P75toP91"),

    path('manage_receive_P91_data/', ToolView.manage_receive_p91_data, name="manage_receive_p91_data"),
    path('manage_receive_P75_data/', ToolView.manage_receive_P75_data, name="manage_receive_P75_data"),
    
    
    path('Issue<int:request_id>/', ToolView.details2, name="details2"),
    path('Issue<int:request_id>/transferitm2', ToolView.transferitm2, name="transferitm2"),  
    path('manage_issueitems2/', ToolView.manage_issueitems2, name="manage_issueitems2"),
    
    path('summa/', ToolView.summa, name="summa"),
    
    path('damage1<int:issue_id>/', ToolView.damage1, name="damage1"),
    path('damage1<int:issue_id>/damageitem1', ToolView.damageitem1, name="damageitem1"),
    path('manage_damage_P91_data', ToolView.manage_damage_P91_data, name="manage_damage_P91_data"),
    

    path('damage2<int:issue_id>/', ToolView.damage2, name="damage2"),
    path('damage2<int:issue_id>/damageitem2', ToolView.damageitem2, name="damageitem2"),
    path('manage_damage_P75_data', ToolView.manage_damage_P75_data, name="manage_damage_P75_data"),
    
    path('tool_profile/', ToolView.tool_profile, name='tool_profile'),
    path('tool_profile_update/', ToolView.tool_profile_update, name="tool_profile_update"),
    


    path('tool_approvel_pending_P91', ToolView.tool_approvel_pending_P91, name="tool_approvel_pending_P91"),
    path('tool_issue_pending_P91', ToolView.tool_issue_pending_P91, name="tool_issue_pending_P91"),
    path('tool_issued_done_P91', ToolView.tool_issued_done_P91, name="tool_issued_done_P91"),
    path('tool_reject_P91', ToolView.tool_reject_P91, name="tool_reject_P91"),

    path('tool_approvel_pending_P75', ToolView.tool_approvel_pending_P75, name="tool_approvel_pending_P75"),
    path('tool_issue_pending_P75', ToolView.tool_issue_pending_P75, name="tool_issue_pending_P75"),
    path('tool_issued_done_P75', ToolView.tool_issued_done_P75, name="tool_issued_done_P75"),
    path('tool_reject_P75', ToolView.tool_reject_P75, name="tool_reject_P75"),
 

]


