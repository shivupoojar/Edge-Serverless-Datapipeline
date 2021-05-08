import os
import json
from datetime import datetime
from minio import Minio
from aeneas.tools.execute_task import ExecuteTaskCLI

def write_to_file(save_path,data):
    with open(save_path,"wb") as f:
      f.write(data)

def handle(event, context):
    bucket = os.enviorn['bucket']
    file = os.enviorn['file']
    resource = '/'+bucket+'/'+file
    content_type = "application/octet-stream"
    
    date=`date -R`
    _signature='GET\n\n'+content_type+'\n'+date+'\n'+resource
    signature=os.system('echo -en'+_signature+'| openssl sha1 -hmac'+os.environ['minio_secret_key'] + '-binary | base64')
    



    dt = datetime.today()
    file = dt.minute
    write_to_file("/tmp/file.mp3",event["body"])
    mc = Minio(os.environ['minio_hostname'],
                 access_key=os.environ['minio_access_key'],
                  secret_key=os.environ['minio_secret_key'],
                  secure=False)
    mc.fget_object('aeneas', 'p001.xhtml', "/tmp/" + 'p001.xhtml')
    ExecuteTaskCLI(use_sys=False).run(arguments=[
    None, # dummy program name argument
    u"/tmp/"+file+".mp3",
    u"/tmp/p001.xhtml",
    u"task_language=eng|is_text_type=plain|os_task_file_format=json",
    u"/tmp/"+file+".json"])
    return "Hi
