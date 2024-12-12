#Handles System related functions
import json

class System():
    def __init__(self):
        pass

    def read_json(self,file_path):
        '''
            Params:
               file_path : file path including filename for the JSON to be read
            Output:
                JSON in dictionary format
        '''
        f    = open(file_path)
        data = json.load(f)
        return data 

    def get_access_token(self):
        '''
            Params:
               None
            Output:
                Access token : str based on `auth.json`
        '''
        return self.read_json("./FB_features/auth.json")['access_token']
        
    def get_base_url(self):
        '''
            Params:
               None
            Output:
                Base URL based on `config.json`
        '''
        config_data = self.read_json("./FB_features/config.json")
        base_url = config_data['base_url'] + config_data['API_version']
        return base_url

    def get_cooldown_limit(self):
        '''
            Params:
               None
            Output:
                cooldown_limit based on `config.json`
        '''
        return self.read_json("./FB_features/config.json")['cooldown_limit']

    def get_cooldown_timeout(self):
        '''
            Params:
               None
            Output:
                cooldown_timeout based on `config.json`
        '''
        return self.read_json("./FB_features/config.json")['cooldown_timeout']

    def get_ad_account_ids(self):
        '''
            Params:
               None
            Output:
                ad_account_ids based on `config.json`
        '''
        return ["act_"+ad_account_id for ad_account_id in self.read_json("./Fb_features/config.json")['ad_account_ids']]

    def get_aws_creds(self):
        return self.read_json("./FB_features/auth.json")['aws_access_key_id'], self.read_json("./FB_features/auth.json")['aws_secret_access_key']