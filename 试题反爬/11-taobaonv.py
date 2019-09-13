import requests

# 测试图片反爬,妹子图竟然是带上了referer反爬
url1 = "https://rate.taobao.com/feedRateList.htm?auctionNumId=575740530252&userNumId=133141181&currentPageNum=1&pageSize=20&rateType=&orderType=sort_weight&attribute=&sku=&hasSku=true&folded=0&ua=098%23E1hvdvvEvbQvU9CkvvvvvjiPRFLWgjYbRLd9AjivPmPvQjn8P2sw6j3RPsSp0jYjR2K5vpvhvvmv99GCvvLMMQvvkphvC99vvOCzpuyCvv9vvUm04ixklfyCvm9vvvvvphvvvvvv9krvpvBYvvmm86Cv2vvvvUUdphvUOQvv9krvpv3FmphvLv1T89vjOezhsjZ7%2B3%2Butj7gQfut8vmxfwLZdiB%2Bm7zhlj7JecnOD7zhQ8g7EcqhQjc6%2Bul1B57OD70Oe361D7zht8gcWhcnI4mxdX9CvpvVvmvvvhCvRphvCvvvvvmjvpvhvvpvvv%3D%3D&_ksTS=1568384457084_1547&callback=jsonp_tbcrate_reviews_list"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
    "Referer": "https://item.taobao.com/item.htm?spm=a219r.lm5734.14.1.552b523cSi2MBs&id=575740530252&ns=1&abbucket=10"
}
ret = requests.get(url1, headers=header)
res_json = ret.content.decode()
print(res_json)

