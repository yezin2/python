import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

if __name__ == "__main__":
    
    # coolsms 개발 / 연동 페이지에서 발급 받은 api_key, api_secret 입력
    
    api_key = "NCS26Z08Y3IZRJPB" 
    api_secret = "APSCKPNPPBRJPGGGOEYN77ECVJGE0EAC"
    
    # # 4 params(to, from, type, text) are mandatory. must be filled
    
    params = dict() # 보내는 파라미터들을 dict에 담아 전송함 // python dict() 함수
    
    params['type'] = 'sms'  # 메세지 타입 (sms, lms, mms, ata )
    params['to'] = '01043093808'  # 수신자 번호 입력, 다중으로 보내려면 '01012341234, 01043214321' 으로 입력
    params['from'] = '01093388049'  # 발신자 번호 입력, api_key에 할당된 소유자의 번호로 입력해야 성공적으로 진행됨
    params['text'] = '테슷흐'  # 보낼 텍스트
    
    cool = Message(api_key, api_secret)  # apikey, secret 인증을 거침
    
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        
        # 보내는데 성공하면 보낸 개수만큼 Success Count : n
        # 보내는데 실패하면 보낸 개수만큼 Error Count : n
        
        if "error_list" in response:
            print("Error List : %s" % response['error_list'])
            
    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)
        sys.exit()
