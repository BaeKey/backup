# -*- encoding: utf-8 -*-
import requests
from urllib import parse
from lxml import etree
import time

# 替换为自己的Bot token
token = "xxxxx"
# 替换为自己的用户ID
userid = "xxxxx"
# 替换为自己的sidyaohuo
sidyaohuo = "xxxxx"
# 刷新间隔/s
refresh_time = 60
# 关键词过滤
keywords = ["关键词1", "关键词2", "关键词3"]

# # 登录用户名
# username = ""
# # 登录密码
# password = ""

headers = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'sec-ch-ua':
    '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

cookies = {'sidyaohuo': sidyaohuo}

# # 登录获取cookies
# def get_cookies():
#     data = {
#     'logname': username,
#     'logpass': password,
#     'action': 'login',
#     'classid': '0',
#     'siteid': '1000',
#     'sid': '-3-0-0-0-0',
#     'backurl': 'bbs/list.aspx?siteid=1000&classid=201',
#     'savesid': '0',
#   }
#     url= "https://yaohuo.me/waplogin.aspx"
#     cookies=requests.post(url,headers=headers,data=data).cookies
#     return cookies


# 获取帖子内容并转换为Markdown格式
def get_content(url):
    try:
        response = requests.get(url, headers=headers, cookies=cookies)
        yaohuo_content = etree.HTML(response.content).xpath(
            '//div[@class="bbscontent"]//comment()[contains(., "listS")]/following-sibling::node()[following::comment()[contains(., "listE")]]'
        )
        # 初始化一个Markdown字符串
        markdown_content = ""
        for element in yaohuo_content:
            if isinstance(element, str):
                markdown_content += element
            elif element.tag == "br":
                markdown_content += "\n"

        return markdown_content

    except Exception as e:
        print("获取内容失败：", e)


# 发送消息
def send_message(chat_id, text):
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    text = parse.quote(text)
    post_url = f'https://api.telegram.org/bot{token}/sendMessage?parse_mode=MarkdownV2&chat_id={chat_id}&text={text}&disable_web_page_preview=true'
    try:
        requests.post(post_url, headers=headers)
    except Exception:
        print("推送失败！")
        time.sleep(3)
        try:
            requests.post(post_url, headers=headers)
        except Exception:
            pass


# 主程序
def main():
    yaohuo_list = set()
    url_yaohuo = "https://yaohuo.me/bbs/book_list.aspx?gettotal=2023&action=new"

    while True:
        try:
            response = requests.get(url_yaohuo,
                                    headers=headers,
                                    cookies=cookies)
            xml_content = etree.HTML(response.content)
            href_list = xml_content.xpath(
                '//div[contains(@class, "listdata line")]/a[1]/@href')
            reply_number = xml_content.xpath(
                '//div[contains(@class, "listdata line")]/a[2]/text()')
            href = xml_content.xpath(
                '//div[contains(@class, "listdata line")]/a[1]/text()')

            for i in range(len(reply_number)):
                if reply_number[i] == '0':
                    if str(href[i]) not in yaohuo_list:
                        yaohuo_list.add(str(href[i]))
                        name = href[i]
                        url_list = f"https://yaohuo.me/{href_list[i]}"
                        current_datetime = time.strftime(
                            "%Y/%m/%d  %H:%M:%S", time.localtime())
                        content = get_content(url_list)
                        # 检查帖子内容是否包含关键词
                        if any(keyword in content for keyword in keywords):
                            text = f'主        题：*[{name}]({url_list})*\n时        间：{current_datetime}\n内容预览：{content}'
                            send_message(userid, text)
                    else:
                        pass
                else:
                    pass
            time.sleep(refresh_time)
        except Exception as e:
            print("发生异常:", e)
            time.sleep(300)


if __name__ == "__main__":
    main()
