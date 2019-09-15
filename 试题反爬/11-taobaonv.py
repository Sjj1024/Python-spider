import requests

# 测试淘宝评论竟然是带上了referer反爬
url1 = "https://rate.taobao.com/feedRateList.htm?auctionNumId=575740530252&userNumId=133141181&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=true&folded=0&ua=098%23E1hvQ9vEvbQvUvCkvvvvvjiPRFLpAj1PP2SUgjD2PmP9AjEbR2FyzjnvRFcZsjnviQhvChCvCCpCvpvVph9vvvvvKphv8hCvvvvvvhCvphvZ7pvvpnXvpCBXvvC2p6CvHHyvvh84phvZ7pvvpiuivpvUphvhrXfVWo8EvpvVpyUUCEK4mphvLhH0KvmFd56OVA5haBgJEctABz7Q%2BulAp169D70OjC60Ecqh08g7Ect1Bzc6%2Bul1p36Q1WQ7%2B3%2BuwAq6D46Xwo1ev0zhVTt%2BmB%2Bu0jZPvpvhvv2MMsyCvvBvpvvv3QhvChCCvvv%3D&_ksTS=1568427307551_1547&callback=jsonp_tbcrate_reviews_list"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer": "https://item.taobao.com/item.htm?spm=a219r.lm5734.14.1.552b523cSi2MBs&id=575740530252&ns=1&abbucket=10"
}
ret = requests.get(url1, headers=header)
res_json = ret.content.decode()
print(res_json)
