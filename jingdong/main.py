__author__ = 'yangyz'


from logger import logger
import requests
import datetime


user_agent = (
      'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
)
session = requests.session()
session.headers['User-Agent'] = user_agent

##将浏览器中能看到的cookie转化为python中的字典
def get_cookie():
    with open("../cookie.txt") as f:
        cookies={}
        for line in f.read().split(';'):
            name,value=line.strip().split('=',1)
            cookies[name]=value
        return cookies

##抢优惠券
def getCoupon():
    sched_Timer="2017-06-14 20:00" ##配置抢券的时间
    ##配置要抢购的券的url  在浏览器的Network中找
    couPonUrl="https://api.m.jd.com/client.action?functionId=newBabelAwardCollection&body=%7B%22activityId%22%3A%223tPzkSJZdNRuhgmowhPn7917dcq1%22%2C%22scene%22%3A%221%22%2C%22args%22%3A%22key%3D898c3948b1a44f36b032c8619e2514eb%2CroleId%3D6983488%2Cto%3Dpro.m.jd.com%2Fmall%2Factive%2F3tPzkSJZdNRuhgmowhPn7917dcq1%2Findex.html%22%2C%22mitemAddrId%22%3A%22%22%2C%22geo%22%3A%7B%22lng%22%3A%22%22%2C%22lat%22%3A%22%22%7D%7D&client=wh5&clientVersion=1.0.0&sid=dce17971eb6cbfcc2275dded296bcb58&uuid=1506710045&area=&_=1497422307569&callback=jsonp5"
    ##配置要抢购的券的referer  在浏览器的Network中找
    referer="https://pro.m.jd.com/mall/active/3tPzkSJZdNRuhgmowhPn7917dcq1/index.html"
    while(1):
        now=datetime.datetime.now().strftime('%Y-%m-%d %H:%M');
        if now==sched_Timer:
            cj = requests.utils.cookiejar_from_dict(get_cookie())
            session.cookies = cj
            resp=session.get(
                          url=couPonUrl,
                          headers={
                         'Referer':referer ,
                       }
                        )
            logger.info(resp.text)
            break


if __name__ == '__main__':
    getCoupon()


