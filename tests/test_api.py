
from helper.apiHelper import ApiHelper

def test_getname(run_flask):
    user_name = 'user2'
    apiobj = ApiHelper()
    user_list = apiobj.get_name()
    assert user_name in user_list, f"'user2' not found in user list: {user_list}"
